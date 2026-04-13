from django.db import models
from django.conf import settings
import uuid
from users.models import User

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="oauth/images/", blank=True, null=True)

    def __str__(self):
        return f"{self.user} profile"