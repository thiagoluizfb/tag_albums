# Generated by Django 3.1.6 on 2021-02-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20210215_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
