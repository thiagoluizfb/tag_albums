# Generated by Django 3.1.6 on 2021-02-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20210215_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
