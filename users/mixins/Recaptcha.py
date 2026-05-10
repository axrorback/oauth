import requests
from django.conf import settings
from django.contrib import messages


class ReCaptchaV3Mixin:

    recaptcha_action = "submit"
    recaptcha_min_score = 0.5

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["SITE_KEY"] = settings.RECAPTCHA_PUBLIC_KEY
        context["recaptcha_action"] = self.recaptcha_action

        return context

    def verify_recaptcha(self):

        token = self.request.POST.get(
            "g-recaptcha-response"
        )

        if not token:
            return False

        data = {
            "secret": settings.RECAPTCHA_PRIVATE_KEY,
            "response": token,
            "remoteip": self.request.META.get(
                "REMOTE_ADDR"
            ),
        }

        try:

            response = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=data,
                timeout=3
            )

            result = response.json()

            success = result.get("success", False)
            score = result.get("score", 0)
            action = result.get("action")

            if not success:
                return False

            if score < self.recaptcha_min_score:
                return False

            if (
                self.recaptcha_action
                and action != self.recaptcha_action
            ):
                return False

            return True

        except requests.RequestException:
            return False

    def form_valid(self, form):

        if not self.verify_recaptcha():

            messages.error(
                self.request,
                "Xavfsizlik tekshiruvi muvaffaqiyatsiz."
            )

            return self.form_invalid(form)

        return super().form_valid(form)