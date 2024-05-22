from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Feedback(models.Model):
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.IntegerField()


class User(models.Model):
    user_login = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_email = models.EmailField()

    def __str__(self):
        return f'{self.user_login} - {self.user_password}'


class Characteristic(models.Model):
    car_body = models.CharField(max_length=100)
    car_number_of_doors = models.IntegerField()
    rudder_position = models.CharField(max_length=100)
    car_release = models.DateField()
    producing_country = models.CharField(max_length=100)
    horsepower = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.producing_country} - {self.car_release} - {self.car_body}'


class RaceClub(models.Model):
    Rear = 'Задний'
    Four_wheel = 'Полный'
    Front_wheel = 'Передний'
    CAR_DRIVE_UNIT_CHOISES = [
        (Rear, 'Задний'),
        (Four_wheel, 'Полный'),
        (Front_wheel, 'Передний'),
    ]

    Mechanics = 'Механика'
    Automatic = 'Автомат'
    Robot = 'Робот'
    Reducer = 'Редуктор'
    CAR_TRANSMISSION_CHOISES = [
        (Mechanics, 'Механика'),
        (Automatic, 'Автомат'),
        (Robot, 'Робот'),
        (Reducer, 'Редуктор'),
    ]

    car_name = models.CharField(max_length=40)
    car_price = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(10)])
    car_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    car_overclocking = models.CharField(max_length=40, default='')
    car_drive_unit = models.CharField(max_length=40, default='', choices=CAR_DRIVE_UNIT_CHOISES)
    car_transmission = models.CharField(max_length=40, default='', choices=CAR_TRANSMISSION_CHOISES)
    slug = models.SlugField(default='', null=False, db_index=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.PROTECT, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.car_name)
        super(RaceClub, self).save(*args, **kwargs)



    def get_url(self):
        return reverse('car-detail', args=[self.slug])

    def __str__(self):
        return f'{self.car_name} - {self.car_price}%'

 #from raceclub_app.models import RaceClub