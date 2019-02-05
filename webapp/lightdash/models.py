from django.db import models

# Create your models here.
class TestData(models.Model): #this will house the data sample
    
    Horodate = models.DateTimeField(primary_key=True)
    Valeur = models.IntegerField(default=0) 
    # no one consumes terawatts

    