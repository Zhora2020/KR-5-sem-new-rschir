# Generated by Django 4.1.1 on 2022-12-09 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raceclub_app', '0006_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
