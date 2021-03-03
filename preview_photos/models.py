from django.db import models


class PhotosPreview(models.Model):
    image = models.FileField(upload_to='preview', null=False, blank=False)

    def __int__(self):
        return self.id
