# Generated by Django 3.1.6 on 2021-02-27 20:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_auto_20210227_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='Country', max_length=2, null=True),
        ),
    ]
