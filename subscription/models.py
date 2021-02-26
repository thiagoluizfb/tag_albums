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


class Snack(models.Model):
    f_name = models.CharField(max_length=50, null=False, blank=False)
    l_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    snack_qty = models.IntegerField(null=False, default=0)
    total = models.IntegerField(null=False, default=0)

    class Meta:
        ordering = ['f_name']

    def __str__(self):
        return self.f_name
