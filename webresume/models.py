from django.db import models
from django.conf import settings
from django.utils import timezone

class Upload(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        Self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
