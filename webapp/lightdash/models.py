from django.db import models
from django import forms
from django.forms import ModelForm
import datetime

# Create your models here.
class TestData(models.Model): #this will house the data sample
    Horodate = models.DateTimeField(primary_key=True)
    Valeur = models.IntegerField(default=0) 
    # no one consumes terawatts

class Settings(models.Model):
    abonnementHPHC = models.BooleanField(default=True)
    tarifHP = models.FloatField(default=0.1579)
    tarifHC = models.FloatField(default=0.1228,null=True)
    debutHC = models.TimeField(default=datetime.time(22,0),null=True)
    finHC = models.TimeField(default=datetime.time(6,0),null=True)
    
class SettingsForm(ModelForm):
    abonnementHPHC = forms.BooleanField(label='Abonement HPHC',required=False)
    tarifHP = forms.FloatField(label='Tarif Heures Pleines', widget=forms.NumberInput(attrs={'step': "0.0001"}))
    tarifHC = forms.FloatField(initial=0.1228,label='Tarif Heures Creuses', widget=forms.NumberInput(attrs={'step': "0.0001"}),required=False)
    debutHC = forms.TimeField(initial=datetime.time(22,0),label='Début Heures Creuses',required=False)
    finHC = forms.TimeField(initial=datetime.time(6,0),label='Fin Heures Creuses',required=False)
    
    class Meta:
        model = Settings
        fields = ['abonnementHPHC','tarifHP','tarifHC','debutHC','finHC']