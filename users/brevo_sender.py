import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from django.conf import settings


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = settings.BREVO_API_KEY


def send_brevo_email(
    to_email: str,
    subject: str,
    html_content: str,
):
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    sender = {
        "name": "Coderboys Auth",
        "email": settings.BREVO_SENDER_EMAIL,
    }

    to = [{"email": to_email}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content,
    )

    try:
        response = api_instance.send_transac_email(
            send_smtp_email
        )
        return response

    except ApiException as e:
        print("Brevo API Error:", e)
        raise