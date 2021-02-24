from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for saving photos
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(
        max_length=20, null=True, blank=True)
    user_photo = models.FileField(null=False, blank=False)

    class Meta:
        ordering = ['user']

    def __int__(self):
        return self.display_name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
        profile = UserProfile.objects.get(user=instance)
        setattr(profile, 'display_name', instance.username)
        profile.save()
    # Existing users: just save the profile
    else:
        instance.userprofile.save()
