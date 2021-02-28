from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'display_name',
    )


admin.site.register(UserProfile, UserProfileAdmin)
