from django.db import models


class Photos(models.Model):
    owner = models.CharField(max_length=254, null=True, blank=True)
    upload_date = models.DateTimeField()
    image = models.FileField(null=True, blank=True)

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
