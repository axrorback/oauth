from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class User2FA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="twofa")
    secret = models.CharField(max_length=32)
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"2FA for {self.user}"