from django.utils.translation import gettext_lazy as _

from dynamic_preferences.preferences import Section
from dynamic_preferences.types import BooleanPreference, StringPreference

from aleksis.core.registries import site_preferences_registry

payments = Section("payments", verbose_name=_("Payments"))


@site_preferences_registry.register
class PublicPayments(BooleanPreference):
    """Allow payments to be made by anyone, not only invoice recipient."""

    section = payments
    name = "public_payments"
    verbose_name = _("Public payments")
    help_text = _(
        "Allow anyone (including guests) to make payments. "
        "Basic invoice information will be visible to anyone who knows the invoice token."
    )
    default = True
    required = False


@site_preferences_registry.register
class SofortAPIID(StringPreference):
    """Sofort payment backend - API ID."""

    section = payments
    name = "sofort_api_id"
    verbose_name = _("Sofort / Klarna - API ID")
    default = ""
    required = False


@site_preferences_registry.register
class SofortAPIKey(StringPreference):
    """Sofort payment backend - API key."""

    section = payments
    name = "sofort_api_key"
    verbose_name = _("Sofort / Klarna - API Key")
    default = ""
    required = False


@site_preferences_registry.register
class SofortProjectID(StringPreference):
    """Sofort payment backend - project ID."""

    section = payments
    name = "sofort_project_id"
    verbose_name = _("Sofort / Klarna - Project ID")
    default = ""
    required = False


@site_preferences_registry.register
class PaypalClientID(StringPreference):
    """PayPal payment backend - client ID."""

    section = payments
    name = "paypal_client_id"
    verbose_name = _("PayPal - Client ID")
    default = ""
    required = False


@site_preferences_registry.register
class PaypalSecret(StringPreference):
    """PayPal payment backend - secret."""

    section = payments
    name = "paypal_secret"
    verbose_name = _("PayPal - Secret")
    default = ""
    required = False


@site_preferences_registry.register
class PaypalCapture(BooleanPreference):
    """PayPal payment backend - use Authorize & Capture."""

    section = payments
    name = "paypal_capture"
    verbose_name = _("PayPal - Use Authorize & Capture")
    default = False
    required = False


@site_preferences_registry.register
class EnablePledge(BooleanPreference):
    """Payment pledge payment backend - enable or not."""

    section = payments
    name = "pledge_enabled"
    verbose_name = _("Enable pledged payments")
    default = False
    required = False


@site_preferences_registry.register
class SDDCreditor(StringPreference):
    """SEPA direct debit backend - creditor name."""

    section = payments
    name = "sdd_creditor"
    verbose_name = _("SEPA Direct Debit - Creditor name")
    default = ""
    required = False


@site_preferences_registry.register
class SDDCreditorIdentifier(StringPreference):
    """SEPA direct debit backend - creditor identifier."""

    section = payments
    name = "sdd_creditor_identifier"
    verbose_name = _("SEPA Direct Debit - Creditor identifier")
    default = ""
    required = False
