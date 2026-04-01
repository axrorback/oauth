from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="oauth/image/", blank=True, null=True)

    def __str__(self):
        return f"{self.user} profile"