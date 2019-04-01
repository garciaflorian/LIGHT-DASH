from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError
from django.urls import resolve, reverse
from django.conf import settings
from lightdash.models import *
from django.forms import ModelForm
from django.db.models import Count
from datetime import timedelta
import json

if(Settings.objects.all().count() == 0):
    print("Initialize Settings...")
    currentSettings = Settings(id=1,abonnementHPHC = True,tarifHP = 0.1579,tarifHC = 0.1228,debutHC = datetime.time(22,0),finHC = datetime.time(6,0),freqPaiement='m',jourPaiement=14,debutBimestre='j')
    currentSettings.save()

# Create your views here.

def index(request):
    #all_data = LinkyData.objects.all()
    consoTotal = LinkyData.objects.latest('date').base
    currentSettings = Settings.objects.get(id=1)
    tarifHP = currentSettings.tarifHP
    
    now = LinkyData.objects.latest('date').date
    delta24h = now - timedelta(hours=24)
    last24h_data = LinkyData.objects.filter(date__gte=delta24h)
    
    if(currentSettings.freqPaiement == 'm'):
        currentMonth_date = LinkyData.objects.filter(date__day=currentSettings.jourPaiement).latest('date').date
        month_data = LinkyData.objects.filter(date__gte=currentMonth_date)
        conso = LinkyData.objects.latest('date').base - month_data.first().base
        if(currentSettings.abonnementHPHC):
            tarifHC = currentSettings.tarifHC
            
            debutHC = currentSettings.debutHC
            finHC = currentSettings.finHC
            
            consoHC = 0
            consoHP = 0
            prec_data = month_data.first()
            for curr_data in month_data:
                if(curr_data != prec_data):
                    if(curr_data.date.time()>=debutHC or curr_data.date.time()<finHC):
                        consoHC = consoHC + curr_data.base - prec_data.base
                        prec_data = curr_data
                    else:
                        consoHP = consoHP + curr_data.base - prec_data.base
                        prec_data = curr_data
            
            prix = round((consoHP/1000)*tarifHP,2)+round((consoHC/1000)*tarifHC,2)
            
        else:
            prix = round((conso/1000)*tarifHP,2)
    else:
        """
        DON'T USE !
        
        currentBimonthly_date = LinkyData.objects.filter(date__day=currentSettings.jourPaiement)[0].date
        print(currentBimonthly_date)
        bimonthly_data = LinkyData.objects.filter(date__gte=currentBimonthly_date)
        
        if(currentSettings.abonnementHPHC):
            tarifHC = currentSettings.tarifHC
        else:
            conso = LinkyData.objects.latest('date').base - bimonthly_data.first().base
            prix = round((conso/1000)*tarifHP,2)
        """
            
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
            currentSettings.debutBimestre = dataSettings['debutBimestre']
            currentSettings.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = SettingsForm(instance=currentSettings)
    return render(request, 'settings.html', locals())

def advanced(request):
    return render(request, 'advanced.html', locals())

def bimestre(mois):
    currentSettings = Settings.objects.get(id=1)
    if currentSettings.debutBimestre == 'j':
        if(mois == 1):
            return [1,2]   
        elif(mois%2 == 0):
            return [mois-1,mois]
        else:
            return [mois,mois+1]
    else:
        if(mois == 12):
            return [12,1]   
        elif(mois%2 == 0):
            return [mois,mois+1]
        else:
            return [mois-1,mois]
