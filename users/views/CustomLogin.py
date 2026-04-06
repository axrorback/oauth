from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, f"Salom, {form.get_user().username}! Siz muvaffaqiyatli login qildingiz.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Login yoki parol noto'g'ri.")
        return super().form_invalid(form)