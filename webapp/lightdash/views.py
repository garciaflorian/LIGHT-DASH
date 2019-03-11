from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.conf import settings
from lightdash.models import *
from django.db.models import Count


if(Settings.objects.all().count() == 0):
    print("Initialize Settings...")
    currentSettings = Settings(id=1,abonnementHPHC = True,tarifHP = 0.1579,tarifHC = 0.1228,debutHC = datetime.time(22,0),finHC = datetime.time(6,0))
    currentSettings.save();
else:
    print("Get Settings...")
    currentSettings = get_object_or_404(Settings, id=1)
    

# Create your views here.

def index(request):
    return render(request, '_index_clean.html', locals())

def settings(request):
    return render(request, 'settings.html', locals())

def advanced(request):
    return render(request, 'advanced.html', locals())