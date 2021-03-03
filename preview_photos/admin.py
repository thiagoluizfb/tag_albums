from django.contrib import admin
from .models import PhotosPreview


class PhotosPreviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )


admin.site.register(PhotosPreview, PhotosPreviewAdmin)
