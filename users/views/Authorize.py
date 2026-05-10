from oauth2_provider.views import AuthorizationView
from users.mixins import ReCaptchaV3Mixin


class CustomAuthorizeView(ReCaptchaV3Mixin, AuthorizationView):
    template_name = "oauth/authorize.html"

    recaptcha_action = "oauth_authorize"
    recaptcha_min_score = 0.5

    def form_valid(self, form):
        if not self.verify_recaptcha():
            form.add_error(None, "Captcha failed")
            return self.form_invalid(form)

        return super().form_valid(form)