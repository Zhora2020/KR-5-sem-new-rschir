# Generated by Django 4.1.1 on 2022-12-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raceclub_app', '0005_alter_raceclub_car_drive_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
