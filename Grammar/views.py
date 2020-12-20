from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects.filter(losung="3")
    context = {
        'questions': questions
    }
    return render(request, 'Grammar/index.html', context)
