from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, '_index_clean.html', locals())