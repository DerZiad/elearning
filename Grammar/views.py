from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects
    losung = request.GET.get('losung')
    context={
        'questions':questions
    }
    if losung == "wo":
         print("gut")
    return render(request, 'Grammar/index.html', context)
