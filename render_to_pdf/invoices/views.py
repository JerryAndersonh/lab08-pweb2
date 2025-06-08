import datetime
from django.http import Http404
from render_to_pdf import renderers

def pdf_view(request):
    data = {
        'invoice_number': 1234,
        'customer_name': 'Jhon Doe',
        'amount': 300.75,
        'date': datetime.date.today(),
        'pdf_title': 'Factura #1234'
    }
    return renderers.render_to_pdf('pdf/invoice.html', data)
