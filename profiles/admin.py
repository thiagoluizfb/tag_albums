from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'display_name',
        'user_photo',
    )


admin.site.register(UserProfile, UserProfileAdmin)
