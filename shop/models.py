from django.db import models

# Create your models here.

class Vehicle(models.Model):

    name=models.CharField(max_length=200)

    brand=models.CharField(max_length=200)

    price=models.PositiveIntegerField()

    color=models.CharField(max_length=200)

    fuel_type=models.CharField(max_length=200)

    image=models.ImageField(upload_to="vehicleimages",default="vehicleimages/default_car.png")


    def __str__(self):
        
        return self.name

    
