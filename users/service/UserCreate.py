from django.db import transaction
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.service import TokenService
from users.models import EmailVerificationToken
from users.tasks import send_verification_email

User = get_user_model()

class UserService:

    @staticmethod
    @transaction.atomic
    def create_user(username: str, email: str, password: str, base_url: str):
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )

        token = TokenService.registration_token()
        token_hash = TokenService.hash(token)

        EmailVerificationToken.objects.create(
            user=user,
            token=token_hash
        )

        path = reverse('verify')
        verify_link = f"{base_url}{path}?token={token}"
        email = email
        transaction.on_commit(lambda: send_verification_email.delay(email, verify_link))
        return user

