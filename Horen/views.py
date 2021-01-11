from django.http import HttpResponse,HttpResponseRedirect
from Home.funktions import funktion as sv
from django.shortcuts import render
from . import randomer as random
from Auth.models import Personne
from .models import *
from Home.funktions import funktion as valide


def Horen(request):
    return render(request, 'Horen/index.html')


def modeltest1(request):
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
            if (note >= 5):
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
    audio = Track.objects.filter(modeltest_id=2)
    question = Question.objects.filter(audio__modeltest_id=2)
    choix = Choix.objects.filter(question__audio__modeltest_id=2)
    message = ""
    choixCocher = request.POST
    if (request.method == 'POST'):
        note = 0
        for reponseQuestion in question:
            for c in choixCocher:
                if (c == reponseQuestion.reponse):
                    note = note + 1
        if (note >= 5):
            message = "Vous avez validé le module"
        else:
            message = "Essayez une autre fois"
    context = {
        'audios': audio,
        'question': question,
        'choix': choix,
        'message': message
    }
    return render(request, 'Horen/modeltest2.html', context)


def modeltest3(request):
    audio = Track.objects.filter(modeltest_id=3)
    question = Question.objects.filter(audio__modeltest_id=3)
    choix = Choix.objects.filter(question__audio__modeltest_id=3)
    message = ""
    choixCocher = request.POST
    if (request.method == 'POST'):
        note = 0
        for reponseQuestion in question:
            for c in choixCocher:
                if (c == reponseQuestion.reponse):
                    note = note + 1
        if (note >= 5):
            message = "Vous avez validé le module"
        else:
            message = "Essayez une autre fois"
    context = {
        'audios': audio,
        'question': question,
        'choix': choix,
        'message': message
    }
    return render(request, 'Horen/modeltest3.html',context)

def poadcast(request):
    return render(request , 'Horen/poadcast.html')
