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
        questions = Question.objects.filter(audio__modeltest_id=1)
        dic = {}
        dictrack = {}
        for question in questions:
            list = []
            choix = Choix.objects.filter(question = question)
            for ch in choix:
                list.append(ch)
            list.insert(random.generateRandom(),question.reponse)
            dic[question.quest] = list
            dictrack[question.quest] = question.audio

        context = {
            'audios':dictrack,
            'questions':dic,
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
