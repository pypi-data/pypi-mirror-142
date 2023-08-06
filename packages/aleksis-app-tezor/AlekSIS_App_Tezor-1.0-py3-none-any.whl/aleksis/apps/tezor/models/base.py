from django.db import models
from django.utils.translation import gettext_lazy as _

from aleksis.core.mixins import ExtensibleModel


class Client(ExtensibleModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "site"], name="uniq_client_per_site")
        ]

    def __str__(self) -> str:
        return self.name
