from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(
            lambda: Profile.objects.get_or_create(user=instance)
        )