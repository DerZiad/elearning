from django.http import HttpResponse
from django.shortcuts import render
from Auth.models import Personne
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials


def Horen(request):
    return render(request, 'Horen/index.html')


def modeltest1(request):
    personne = Personne.objects.filter(username=request.session['Username'])
    request.session['succes_horen']
    return render(request, 'Horen/modeltest1.html')


def modeltest2(request):
    return render(request, 'Horen/modeltest2.html')


def modeltest3(request):
    personne = Personne.objects.filter(username = request.session['Username'])
    request.session['succes_horen']
    return render(request, 'Horen/modeltest3.html')


def poadcast(request):
    return render(request , 'Horen/poadcast.html')
