from django.shortcuts import render ,redirect , reverse
from django.views.generic import FormView
from users.forms import RegisterForm
from users.service import TokenService
from users.models import EmailVerificationToken
from users.tasks import EmailTask

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/check-email/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        raw_token = TokenService.registration_token()
        hashed_token = TokenService.hash(raw_token)

        EmailVerificationToken.objects.create(
            user=user,
            token=hashed_token
        )

        verification_link = self.request.build_absolute_uri(reverse('verify')) + f'?token={raw_token}'
        EmailTask.delay(user.email, verification_link)
        print(verification_link)
        return super().form_valid(form)
