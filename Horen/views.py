from django.http import HttpResponse,HttpResponseRedirect
from Home.funktions import funktion as sv
from django.shortcuts import render
from . import randomer as random
from Auth.models import Personne
from .models import *



def Horen(request):
    return render(request, 'Horen/index.html')


def modeltest1(request):
        #personne = Personne.objects.filter(username=request.session['Username'])
        #request.session['succes_horen']
        audio= Track.objects.filter(modeltest_id=1)
        question= Question.objects.filter(audio__modeltest_id=1)
        choix= Choix.objects.filter(question__audio__modeltest_id=1)
        message = ""
        choixCocher = request.POST
        if (request.method =='POST'):
            note=0
            for reponseQuestion in question:
                for c in choixCocher:
                    if(c==reponseQuestion.reponse):
                            note=note+1
            if (note >=1):
                message = "Vous avez validé le module"
            else:
                message = "Essayez une autre fois"
        context = {
            'audios': audio,
            'question': question,
            'choix': choix,
            'message': message
        }
        return render(request, 'Horen/modeltest1.html', context)


def modeltest2(request):
    return render(request, 'Horen/modeltest2.html')


def modeltest3(request):
    personne = Personne.objects.filter(username = request.session['Username'])
    request.session['succes_horen']
    return render(request, 'Horen/modeltest3.html')


def poadcast(request):
    return render(request , 'Horen/poadcast.html')
