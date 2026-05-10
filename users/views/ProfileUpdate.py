from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from users.forms import UserUpdateForm, ProfileUpdateForm
from users.mixins import ReCaptchaV3Mixin
from django.conf import settings

class ProfileUpdateView(LoginRequiredMixin, ReCaptchaV3Mixin, View):

    recaptcha_action = "submit"
    recaptcha_min_score = 0.5
    template_name = "users/profile_edit.html"

    def get_context(self, request):

        return {
            "user_form": UserUpdateForm(instance=request.user),
            "profile_form": ProfileUpdateForm(instance=request.user.profile),
            "SITE_KEY": settings.RECAPTCHA_PUBLIC_KEY,
            "recaptcha_action": self.recaptcha_action,
        }

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context(request))

    def post(self, request, *args, **kwargs):

        if not self.verify_recaptcha():
            messages.error(request, "Captcha xato")

            return render(
                request,
                self.template_name,
                self.get_context(request)
            )

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

        return render(request, self.template_name, {
            **self.get_context(request),
            "user_form": user_form,
            "profile_form": profile_form,
        })