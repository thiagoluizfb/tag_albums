from django.contrib import admin
from .models import Photos, Tags


class PhotosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'upload_date',
        'image',
    )


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'tag_name',
    )


admin.site.register(Photos, PhotosAdmin)
admin.site.register(Tags, TagsAdmin)
