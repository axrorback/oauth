from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from users.models import EmailVerificationToken
from users.service import TokenService
from django.utils import timezone
from datetime import timedelta


class VerifyView(TemplateView):
    template_name = 'users/verify.html'
    TOKEN_EXPIRY_MINUTES = 10

    def get(self, request, *args, **kwargs):
        raw_token = request.GET.get('token')

        if not raw_token:
            messages.error(request, "Token topilmadi.")
            return redirect('login')

        hashed_token = TokenService.hash(raw_token)

        token_obj = EmailVerificationToken.objects.filter(
            token=hashed_token,
            is_used=False
        ).first()

        if not token_obj:
            messages.error(request, "Token yaroqsiz yoki allaqachon ishlatilgan.")
            return redirect('login')

        expiry_limit = token_obj.created_at + timedelta(minutes=self.TOKEN_EXPIRY_MINUTES)
        if expiry_limit < timezone.now():
            token_obj.is_used = True
            token_obj.save()
            messages.error(request, "Token muddati tugagan.")
            return redirect('login')

        user = token_obj.user
        user.is_active = True
        user.save()

        token_obj.is_used = True
        token_obj.save()

        messages.success(request, "Sizning emailingiz tasdiqlandi. Endi tizimga kirishingiz mumkin.")
        return redirect('login')