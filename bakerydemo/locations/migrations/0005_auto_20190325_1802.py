# Generated by Django 2.1.7 on 2019-03-25 18:02

from django.db import migrations

from wagtail_i18n.bootstrap import BootstrapTranslatableModel


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20190314_1747'),
    ]

    operations = [
        BootstrapTranslatableModel('locations.LocationsIndexPage'),
        BootstrapTranslatableModel('locations.LocationPage'),
    ]
