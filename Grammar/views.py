from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models

from Grammar.models import Ubung,Essai


def grammarex(request):

    ubungs = Ubung.objects.all()

    if(request.method == "POST"):
        losung = request.POST
        cmp = 0

        for ubung in ubungs:
            print(losung[ubung.frage],"et",ubung.losung)
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
        if len(losung)!=0 :
         msg ="le nombre de question acuis",cmp
         context = {
            'ubungs': ubungs,
            'message':msg
         }
         return render(request, 'Grammar/index.html', context)
        else :
            context = {
                'ubungs': ubungs,

            }
        return render(request, 'Grammar/index.html', context)
    else:

        moglichkeit = Essai.objects.all()

        dic = {
        }
        i = 1
        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            for mog in moglichkeit:
                if mog.ayman == ubung:
                    list.append(mog.test)
            dic[str(ubung.frage)] = list
            print(list)
            print("le se",dic)
            list =[]
        losung = request.GET

        context = {
            'dictionnaire':dic

        }
        return render(request, 'Grammar/index.html', context)
