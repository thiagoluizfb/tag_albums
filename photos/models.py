from django.db import models
from profiles.models import UserProfile


class Photos(models.Model):
    owner = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='photos')
    upload_date = models.DateTimeField()
    image = models.FileField(null=False, blank=False)

    class Meta:
        ordering = ['upload_date']

    def __str__(self):
        return self.owner


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, null=True, blank=True)
    tag_photos = models.ManyToManyField(Photos)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name
