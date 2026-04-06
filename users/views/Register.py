from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView , TemplateView
from users.forms import RegisterForm
from users.service import UserService
from users.models import SiteConfig
class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('check_email')

    def dispatch(self, request, *args, **kwargs):
        config = SiteConfig.objects.filter(key='registration_open').first()

        if not config or not config.value:
            return redirect('register_closed')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        data = form.cleaned_data

        base_url = self.request.build_absolute_uri('/')[:-1]

        UserService.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            base_url=base_url
        )

        self.request.session['check_email'] = {
            'allowed': True,
            'email': data['email']
        }

        return super().form_valid(form)