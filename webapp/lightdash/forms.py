from django import forms
from django.forms import ModelForm
from lightdash.models import *
from datetime import datetime
    
class SettingsForm(forms.Form):
    abonnementHPHC = forms.BooleanField(label='Abonement HPHC ?',default=True)
    tarifHP = forms.FloatField(label='Tarif Heures Pleines',default=0.1579)
    tarifHC = forms.FloatField(label='Tarif Heures Creuses',default=0.1228)
    debutHC = forms.TimeField(label='Début Heures Creuses',default=datetime.time(22,0))
    finHC = forms.TimeField(label='Fin Heures Creuses',default=datetime.time(6,0))