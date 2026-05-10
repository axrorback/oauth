from django.conf import settings

class ReCaptchaContextMixin:

    def get_recaptcha_context(self):
        return {
            "SITE_KEY": settings.RECAPTCHA_PUBLIC_KEY,
            "recaptcha_action": getattr(self, "recaptcha_action", "submit"),
        }