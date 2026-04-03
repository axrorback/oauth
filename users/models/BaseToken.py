from django.db import models
from django.conf import settings
import uuid
from datetime import timedelta
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class BaseToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=["token"]),
        ]