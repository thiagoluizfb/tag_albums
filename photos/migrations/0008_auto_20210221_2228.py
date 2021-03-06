# Generated by Django 3.1.6 on 2021-02-21 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('photos', '0007_auto_20210217_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='photos',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='profiles.userprofile'),
        ),
    ]
