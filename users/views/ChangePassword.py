from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.mixins import ReCaptchaV3Mixin

class ChangePasswordView(LoginRequiredMixin,ReCaptchaV3Mixin,PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('change_password_done')