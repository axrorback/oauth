# accounts/models/login_history.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class LoginHistory(models.Model):
    STATUS_CHOICES = (
        ("success", "Success"),
        ("failed", "Failed"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "-created_at"]),
        ]

    def __str__(self):
        return f"{self.user or 'Anonymous'} - {self.status} - {self.created_at} - {self.ip_address}"