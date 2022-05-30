from django.core.mail import send_mail
from decouple import config
from .models import Ticket


def add_to_request_data(request_data, key, value):
    request_data._mutable = True
    request_data[key] = value
    request_data._mutable = False
    return request_data


def send_email_about_status_change(status, user_email):
    sender = 'Support'
    mail_text = f'Hi! Status of your ticket has been changed to {status}. Check out your ticket!'
    sender_email = config('EMAIL_HOST_USER')
    send_mail(sender, mail_text, sender_email, [user_email])


def get_ticket_user_email(pk):
    ticket = Ticket.objects.get(pk=pk)
    user_email = ticket.user.email
    return user_email

