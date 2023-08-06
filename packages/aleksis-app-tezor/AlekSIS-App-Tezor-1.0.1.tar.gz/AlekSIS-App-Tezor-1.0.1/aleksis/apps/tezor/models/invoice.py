from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from payments import PaymentStatus, PurchasedItem
from payments.models import BasePayment

from aleksis.core.mixins import ExtensibleModel, PureDjangoModel
from aleksis.core.models import Person

from ..tables import PurchasedItemsTable, TotalsTable
from .base import Client


class InvoiceGroup(ExtensibleModel):
    name = models.CharField(verbose_name=_("Invoice group name"), max_length=255)
    client = models.ForeignKey(
        Client,
        verbose_name=_("Linked client"),
        related_name="invoice_groups",
        on_delete=models.SET_NULL,
        null=True,
    )

    template_name = models.CharField(
        verbose_name=_("Template to render invoices with as PDF"), blank=True, max_length=255
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["client", "name"], name="group_uniq_per_client")
        ]


class Invoice(BasePayment, PureDjangoModel):
    VARIANT_DISPLAY = {
        "paypal": (_("PayPal"), "logos:paypal"),
        "sofort": (_("Klarna / Sofort"), "simple-icons:klarna"),
        "pledge": (_("Payment pledge / manual payment"), "mdi:hand-coin"),
        "sdd": (_("SEPA Direct Debit"), "mdi:bank-transfer"),
    }
    STATUS_ICONS = {
        PaymentStatus.WAITING: "mdi:cash-lock-open",
        PaymentStatus.INPUT: "mdi:cash-lock-open",
        PaymentStatus.PREAUTH: "mdi:cash-lock",
        PaymentStatus.CONFIRMED: "mdi:cash-check",
        PaymentStatus.REFUNDED: "mdi:cash-refund",
        PaymentStatus.REJECTED: "mdi:cash-remove",
        PaymentStatus.ERROR: "mdi:cash-remove",
    }

    group = models.ForeignKey(
        InvoiceGroup,
        verbose_name=_("Invoice group"),
        related_name="invoices",
        on_delete=models.SET_NULL,
        null=True,
    )

    number = models.CharField(verbose_name=_("Invoice number"), max_length=255)
    due_date = models.DateField(verbose_name=_("Payment due date"), null=True)

    for_content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, null=True, blank=True
    )
    for_object_id = models.PositiveIntegerField(null=True, blank=True)
    for_object = GenericForeignKey("for_content_type", "for_object_id")

    # For manual invoicing
    person = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        verbose_name=_("Invoice recipient (person)"),
        blank=True,
        null=True,
    )
    items = models.ManyToManyField("InvoiceItem", verbose_name=_("Invoice items"))

    def save(self, *args, **kwargs):
        if self.person:
            person = self.person
        elif self.for_object and getattr(self.for_object, "person", None):
            person = self.for_object.person
        else:
            person = None

        if person:
            if not self.billing_last_name:
                self.billing_last_name = person.last_name
            if not self.billing_first_name:
                self.billing_first_name = person.first_name
            if not self.billing_address_1:
                self.billing_address_1 = f"{person.street} {person.housenumber}"
            if not self.billing_city:
                self.billing_city = person.place
            if not self.billing_postcode:
                self.billing_postcode = person.postal_code

        super().save(*args, **kwargs)

    @classmethod
    def get_variant_choices(cls):
        choices = []
        for variant in settings.PAYMENT_VARIANTS.keys():
            choices.append((variant, cls.VARIANT_DISPLAY[variant][0]))
        return choices

    def get_variant_name(self):
        return self.__class__.VARIANT_DISPLAY[self.variant][0]

    def get_variant_icon(self):
        return self.__class__.VARIANT_DISPLAY[self.variant][1]

    def get_status_icon(self):
        return self.__class__.STATUS_ICONS[self.status]

    def get_purchased_items(self):
        if self.items.count():
            for item in self.items.all():
                yield item.as_purchased_item()
        else:
            for item in self.for_object.get_purchased_items():
                yield item

    def get_person(self):
        if self.person:
            return self.person
        elif hasattr(self.for_object, "person"):
            return self.for_object.person
        elif hasattr(self.for_object, "get_person"):
            return self.for_object.get_person()

        return None

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["number", "group"], name="number_uniq_per_group"),
            models.CheckConstraint(
                check=(
                    (Q(for_object_id__isnull=True) & Q(person__isnull=False))
                    | (Q(for_object_id__isnull=False) & Q(person__isnull=True))
                ),
                name="object_or_person",
            ),
        ]
        permissions = (("send_invoice_email", _("Can send invoice by email")),)

    def get_billing_email_recipients(self):
        if hasattr(self.for_object, "get_billing_email_recipients"):
            return self.for_object.get_billing_email_recipients()
        else:
            return [self.billing_email]

    @property
    def purchased_items_table(self):
        items = [i._asdict() for i in self.get_purchased_items()]
        return PurchasedItemsTable(items)

    @property
    def totals_table(self):
        tax_amounts = {}
        for item in self.get_purchased_items():
            tax_amounts.setdefault(item.tax_rate, 0)
            tax_amounts[item.tax_rate] += item.price / (item.tax_rate + 100) * item.tax_rate

        values = []
        for tax_rate, total in tax_amounts.items():
            values.append(
                {
                    "name": _("Included VAT {} %").format(tax_rate),
                    "value": total,
                    "currency": self.currency,
                }
            )

        values.append(
            {
                "name": _("Gross total"),
                "value": self.total,
                "currency": self.currency,
            }
        )

        return TotalsTable(values)

    def get_absolute_url(self):
        return reverse("invoice_by_token", kwargs={"slug": self.token})

    def get_success_url(self):
        return self.get_absolute_url()

    def get_failure_url(self):
        return self.get_absolute_url()


class InvoiceItem(ExtensibleModel):
    sku = models.CharField(max_length=255, verbose_name=_("Article no."), blank=True)
    description = models.CharField(max_length=255, verbose_name=_("Purchased item"))
    price = models.DecimalField(
        verbose_name=_("Item gross price"), max_digits=9, decimal_places=2, default="0.0"
    )
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    tax_rate = models.DecimalField(
        verbose_name=_("Tax rate"), max_digits=4, decimal_places=1, default="0.0"
    )

    def as_purchased_item(self):
        return PurchasedItem(
            name=self.description,
            quantity=1,
            price=self.price,
            currency=self.currency,
            sku=self.sku,
            tax_rate=self.tax_rate,
        )
