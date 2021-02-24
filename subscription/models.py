from django.db import models
from profiles.models import UserProfile


class Tiers(models.Model):
    """
    Tiers model for subscription
    """
    user = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='tier', default=6)
    tier = models.BooleanField(default=False)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.tier
