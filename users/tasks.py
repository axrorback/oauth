from celery import shared_task
from django.template.loader import render_to_string
from users.brevo_sender import send_brevo_email


@shared_task(name="send_verification_email")
def send_verification_email(email, verify_url):

    subject = "Emailni Tasdiqlang !"

    context = {
        "verify_url": verify_url
    }

    html_message = render_to_string(
        "emails/verify.html",
        context
    )

    send_brevo_email(
        to_email=email,
        subject=subject,
        html_content=html_message,
    )

    return f"Verification email sent to {email}"