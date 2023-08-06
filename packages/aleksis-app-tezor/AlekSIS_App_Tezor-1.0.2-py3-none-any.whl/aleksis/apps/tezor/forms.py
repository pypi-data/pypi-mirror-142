from material import Layout, Row

from aleksis.core.mixins import ExtensibleForm

from .models.base import Client
from .models.invoice import InvoiceGroup


class EditClientForm(ExtensibleForm):
    """Form to create or edit clients."""

    layout = Layout("name")

    class Meta:
        model = Client
        exclude = []


class EditInvoiceGroupForm(ExtensibleForm):

    layout = Layout(Row("name", "template_name"))

    class Meta:
        model = InvoiceGroup
        exclude = ["client"]
