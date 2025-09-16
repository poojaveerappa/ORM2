from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name = models.CharField()  
    car_no = models.IntegerField()
    release_date = models.DateField()
    car_colour = models.CharField()
    

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name','car_no','release_date','car_colour')