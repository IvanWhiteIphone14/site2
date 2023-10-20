from django.db import models

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    short_info = models.TextField(default='short info')
    year = models.IntegerField()
    main_photo = models.ImageField(upload_to='taciki/', default='default_photo.jpg')
    type = models.CharField(max_length=100, default='Coupe')

    def __str__(self):
        return f"{self.brand} {self.model} {self.type}({self.year})"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='car_photos/')

# Create your models here.
