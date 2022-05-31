from SupportAPI.celery import app
from decouple import config
from django.core.mail import send_mail


@app.task()
def send_status_mail(status, user_email):
    sender = 'Support'
    mail_text = f'Hi! Status of your ticket has been changed to {status}. Check out your ticket!'
    sender_email = config('EMAIL_HOST_USER')
    send_mail(sender, mail_text, sender_email, [user_email])
