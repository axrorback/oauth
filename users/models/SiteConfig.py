from django.db import models

class SiteConfig(models.Model):
    key = models.CharField(max_length=255)
    value = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.key}: {self.value}"