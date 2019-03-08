from django.db import models
import datetime

# Create your models here.
class TestData(models.Model): #this will house the data sample
    Horodate = models.DateTimeField(primary_key=True)
    Valeur = models.IntegerField(default=0) 
    # no one consumes terawatts

class Settings(models.Model):
    abonnementHPHC = models.BooleanField(default=True)
    tarifHP = models.FloatField(default=0.1579)
    tarifHC = models.FloatField(default=0.1228)
    debutHC = models.TimeField(default=datetime.time(22,0))
    finHC = models.TimeField(default=datetime.time(6,0))