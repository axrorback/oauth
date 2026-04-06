from django.contrib.auth import user_logged_in
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile , LoginHistory
from users.service import get_device , get_client_ip , parse_user_agent


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(
            lambda: Profile.objects.get_or_create(user=instance)
        )

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ua_string = request.META.get("HTTP_USER_AGENT")
    ip_address = get_client_ip(request)
    device = get_device(ua_string)

    LoginHistory.objects.create(
        user=user,
        user_agent=ua_string,
        device=device,
        ip_address=ip_address,
        status="success"
    )