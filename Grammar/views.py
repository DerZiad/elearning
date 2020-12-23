from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models

from Grammar.models import Ubung


def grammarex(request):

    ubungs = Ubung.objects.all()

    if(request.method == "POST"):
        losung = request.POST
        cmp = 0
        context = {
            'ubungs': ubungs
        }
        for ubung in ubungs:
            print(ubung)
            print("ziad",losung[ubung.frage])
            print(ubung.losung)
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
        print("le nombre de question acuis",cmp)
        return render(request, 'Grammar/index.html', context)
    else:
        losung = request.GET

        context = {
            'ubungs': ubungs
        }
        return render(request, 'Grammar/index.html', context)
