from django.db import models
from django import forms
from django.forms import ModelForm
import datetime
from schedulers import test



choixPaiement = ('m','Mensuelle'),('b','Bimestrielle')
choixDebutBim = ('j','Janvier'),('f','Février')

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
    freqPaiement = models.CharField(max_length=12, choices=choixPaiement)
    jourPaiement = models.IntegerField()
    debutBimestre = models.CharField(max_length=7, choices=choixDebutBim)
    
class LinkyData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    base = models.IntegerField()
    papp = models.IntegerField()
    
class LinkyData10min(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    base = models.IntegerField()
    papp = models.IntegerField()
    prea = models.IntegerField()

class LinkyDataHour(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    base = models.IntegerField()
    papp = models.IntegerField()
    prea = models.IntegerField()
    
class LinkyDataWeek(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    base = models.IntegerField()
    papp = models.IntegerField()
    prea = models.IntegerField()
    
class LinkyDataMonth(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    base = models.IntegerField()
    papp = models.IntegerField()
    prea = models.IntegerField()
    
class SettingsForm(ModelForm):
    abonnementHPHC = forms.BooleanField(label='Abonement HPHC',required=False)
    tarifHP = forms.FloatField(label='Tarif Heures Pleines', widget=forms.NumberInput(attrs={'step': "0.0001"}))
    tarifHC = forms.FloatField(initial=0.1228,label='Tarif Heures Creuses', widget=forms.NumberInput(attrs={'step': "0.0001",'placeholder':'0.1228'}),required=False)
    debutHC = forms.TimeField(initial=datetime.time(22,0),label='Début Heures Creuses',widget=forms.TextInput(attrs={'placeholder':'22:00:00'}),required=False)
    finHC = forms.TimeField(initial=datetime.time(6,0),label='Fin Heures Creuses',widget=forms.TextInput(attrs={'placeholder':'06:00:00'}),required=False)
    freqPaiement = forms.ChoiceField(choices=choixPaiement,label='Fréquences de paiement',required=True)
    jourPaiement = forms.IntegerField(min_value=1,max_value=28,label='Jour de la facturation',required=True)
    debutBimestre = forms.ChoiceField(choices=choixDebutBim,label='Début de facturation',required=False)
    
    class Meta:
        model = Settings
        fields = ['abonnementHPHC','tarifHP','tarifHC','debutHC','finHC','freqPaiement','jourPaiement','debutBimestre']

        
#Test apscheduler
#test.start()