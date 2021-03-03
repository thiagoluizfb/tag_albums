from django.db import models


class PhotosPreview(models.Model):
    image = models.FileField(upload_to='preview', null=False, blank=False)
    image_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.image_name
