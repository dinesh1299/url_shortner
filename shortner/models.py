from django.db import models
from datetime import datetime
# Create your models here.


class url(models.Model):
    original_url = models.TextField()
    shortend_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @property
    def is_expired(self):
        return "Active" if self.expires_at.replace(tzinfo=None) > datetime.now() else "Link expired"


class analytics(models.Model):
    shortend_url = models.ForeignKey(url, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(default="", max_length=15)
