from django.db import models
from core.models import TimeStampedModel
from django.conf import settings


class Profile(TimeStampedModel):
    """
    Profile model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
