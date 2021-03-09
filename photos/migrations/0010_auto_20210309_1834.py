# Generated by Django 3.1.6 on 2021-03-09 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_user_photo'),
        ('photos', '0009_auto_20210224_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='profiles.userprofile'),
        ),
    ]
