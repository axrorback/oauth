from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from users.forms import UserUpdateForm, ProfileUpdateForm


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile_edit.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            "user_form": UserUpdateForm(instance=request.user),
            "profile_form": ProfileUpdateForm(instance=request.user.profile)
        })

    def post(self, request, *args, **kwargs):
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

        return self.render_to_response({
            "user_form": user_form,
            "profile_form": profile_form
        })