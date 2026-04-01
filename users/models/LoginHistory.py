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
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.user} - {self.status} - {self.created_at}"