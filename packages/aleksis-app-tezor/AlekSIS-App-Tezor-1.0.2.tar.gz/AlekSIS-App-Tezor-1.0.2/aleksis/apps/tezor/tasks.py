from aleksis.core.celery import app
from aleksis.core.util.email import send_email
from aleksis.core.util.pdf import generate_pdf_from_template

from .models.invoice import Invoice


@app.task
def email_invoice(invoice_token):
    context = {}
    invoice = Invoice.objects.get(token=invoice_token)
    context["invoice"] = invoice

    invoice_pdf, result = generate_pdf_from_template(invoice.group.template_name, context)
    result.wait(timeout=30, disable_sync_subtasks=False)
    invoice_pdf.refresh_from_db()

    send_email(
        template_name="invoice",
        from_email=invoice.group.client.email,
        recipient_list=invoice.get_billing_email_recipients(),
        context=context,
        attachments=[(invoice_pdf.file.name, invoice_pdf.file.read(), "application/pdf")],
    )
