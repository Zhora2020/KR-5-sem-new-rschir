# Generated by Django 4.1.1 on 2022-12-07 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raceclub_app', '0004_alter_raceclub_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raceclub',
            name='car_drive_unit',
            field=models.CharField(choices=[('Задний', 'Задний'), ('Полный', 'Полный'), ('Передний', 'Передний')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='raceclub',
            name='car_price',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='raceclub',
            name='car_rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='raceclub',
            name='car_transmission',
            field=models.CharField(choices=[('Механика', 'Механика'), ('Автомат', 'Автомат'), ('Робот', 'Робот'), ('Редуктор', 'Редуктор')], default='', max_length=40),
        ),
    ]
