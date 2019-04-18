from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError, JsonResponse, StreamingHttpResponse
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
    #print("count : "+str(LinkyData.objects.count()))
    
    if( LinkyData.objects.count() > 1 ):
        consoTotal = LinkyData.objects.latest('date').base
        currentSettings = Settings.objects.get(id=1)
        tarifHP = currentSettings.tarifHP

        now = LinkyData.objects.last().date
        #print(LinkyData.objects.last().base)
        delta24h = now - timedelta(hours=23) # 24h of data
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

                prix = round((consoHP/1000)*tarifHP+(consoHC/1000)*tarifHC,2)

            else:
                prix = round((conso/1000)*tarifHP,2)
        else:
            currentBimonthly_date = LinkyData.objects.filter(date__day=currentSettings.jourPaiement).latest('date').date
            bim = bimestre(currentBimonthly_date.month,currentBimonthly_date.year)
            #print("______________")
            #print(currentBimonthly_date)

            bimonthly_date =  currentBimonthly_date.replace(month=bim[0][0],year=bim[0][1])
            #print(bimonthly_date)
            bimonthly_data = LinkyData.objects.filter(date__gte=bimonthly_date)
            conso = LinkyData.objects.latest('date').base - bimonthly_data.first().base

            if(currentSettings.abonnementHPHC):
                tarifHC = currentSettings.tarifHC

                debutHC = currentSettings.debutHC
                finHC = currentSettings.finHC

                consoHC = 0
                consoHP = 0
                prec_data = bimonthly_data.first()
                for curr_data in bimonthly_data:
                    if(curr_data != prec_data):
                        if(curr_data.date.time()>=debutHC or curr_data.date.time()<finHC):
                            consoHC = consoHC + curr_data.base - prec_data.base
                            prec_data = curr_data
                        else:
                            consoHP = consoHP + curr_data.base - prec_data.base
                            prec_data = curr_data

                prix = round((consoHP/1000)*tarifHP+(consoHC/1000)*tarifHC,2)

            else:
                prix = round((conso/1000)*tarifHP,2)
            
    return render(request, '_index_clean.html', locals())

def jsonData24h(request):
    now = LinkyData.objects.latest('date').date
    delta24h = now - timedelta(hours=23) # 24h of data
    last24h_data = LinkyData.objects.filter(date__gte=delta24h)
    last24h_json = list(last24h_data.values())
    return JsonResponse(last24h_json, safe=False)

def jsonAllData(request):
    def jsonFixDatetime(o):
        if(isinstance(o, datetime.datetime)):
            return o.__str__()
    
    allData = LinkyData.objects
    allData_list = list(allData.values())
    allData_json = json.dumps(allData_list,default=jsonFixDatetime)
    response = HttpResponse(allData_json,content_type='text/json')
    response['Content-Disposition'] = 'attachment; filename="LinkyData.json"'
    return response

def settings(request):
    currentSettings = Settings.objects.get(id=1)
    #print(SettingsForm)
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

def bimestre(mois,annee):
    currentSettings = Settings.objects.get(id=1)
    if currentSettings.debutBimestre == 'j':
        if(mois == 1 or mois == 2):
            return [[1,annee],[2,annee]]
        elif(mois%2 == 0):
            return [[mois-1,annee],[mois,annee]]
        else:
            return [[mois,annee],[mois+1,annee]]
    else:
        if(mois == 12 or mois == 1):
            return [[12,annee-1],[1,annee]]
        elif(mois%2 == 0):
            return [[mois,annee],[mois+1,annee]]
        else:
            return [[mois-1,annee],[mois,annee]]
