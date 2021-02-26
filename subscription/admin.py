from django.contrib import admin
from .models import Tiers, Snack


class TiersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'tier',
    )


class SnackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'f_name',
        'l_name',
        'date',
        'snack_qty',
        'total',
    )


admin.site.register(Tiers, TiersAdmin)
admin.site.register(Snack, SnackAdmin)
