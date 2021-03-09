# Generated by Django 3.1.6 on 2021-03-09 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0010_auto_20210309_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiers',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tier', to=settings.AUTH_USER_MODEL),
        ),
    ]
