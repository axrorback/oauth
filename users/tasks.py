# users/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

@shared_task(name="send_verification_email")
def send_verification_email(email, verify_url):
    subject = 'CODERBOYS OAuth2.0 Server Verification'
    context = {'verify_url': verify_url}
    html_message = render_to_string('emails/verify.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html_message
    )
    return f'Email sent to {email}'