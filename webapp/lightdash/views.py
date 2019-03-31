from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError
from django.urls import resolve, reverse
from django.conf import settings
from lightdash.models import *
from django.forms import ModelForm
from django.db.models import Count
import json

if(Settings.objects.all().count() == 0):
    print("Initialize Settings...")
    currentSettings = Settings(id=1,abonnementHPHC = True,tarifHP = 0.1579,tarifHC = 0.1228,debutHC = datetime.time(22,0),finHC = datetime.time(6,0),freqPaiement='m',jourPaiement=14)
    currentSettings.save()

# Create your views here.

def index(request):
    all_data = LinkyData.objects.all()
    currentSettings = Settings.objects.get(id=1)
    tarifHPwh= currentSettings.tarifHP
    conso = LinkyData.objects.latest('date').base - LinkyData.objects.get(id=1).base
    consoTotal = LinkyData.objects.latest('date').base
    prix = round((conso/1000)*tarifHPwh,2)
    return render(request, '_index_clean.html', locals())

def settings(request):
    currentSettings = Settings.objects.get(id=1)
    print(SettingsForm)
    if request.method == 'POST':
        form = SettingsForm(request.POST,instance=currentSettings)
        if form.is_valid():
            dataSettings = form.cleaned_data
            currentSettings.abonnementHPHC = dataSettings['abonnementHPHC']
            currentSettings.tarifHP = dataSettings['tarifHP']
            currentSettings.tarifHC = dataSettings['tarifHC']
            currentSettings.debutHC = dataSettings['debutHC']
            currentSettings.finHC = dataSettings['finHC']
            currentSettings.freqPaiement = dataSettings['freqPaiement']
            currentSettings.jourPaiement = dataSettings['jourPaiement']
            currentSettings.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = SettingsForm(instance=currentSettings)
    return render(request, 'settings.html', locals())

def advanced(request):
    return render(request, 'advanced.html', locals())