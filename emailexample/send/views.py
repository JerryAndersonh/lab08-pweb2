from django.shortcuts import render
from django.core.mail import send_mail


def index(request):

    send_mail('Hello from JerryAndersonMail', 
    'Hello there, this is a test email from JerryAndersonMail.',
    '959e87ce89652e',
    ['dopox28863@adrewire.com'],
    fail_silently=False)

    return render(request, 'send/index.html')