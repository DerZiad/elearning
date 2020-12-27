from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models

from Grammar.models import Ubung,Essai
ubung = Ubung(frage= "'ist diese Frau ? Das ist meine Mutter",losung = "wer")
ubung.save()
moglich = Essai(choix="wo",numf=ubung)
moglich.save()
moglich = Essai(choix="wo1",numf=ubung)
moglich.save()
moglich = Essai(choix="wo2",numf=ubung)
moglich.save()
moglich = Essai(choix="wo3",numf=ubung)
moglich.save()

def grammarex(request):

    ubungs = Ubung.objects.all()

    if(request.method == "POST"):
        losung = request.POST
        cmp = 0

        for ubung in ubungs:
            print(losung[ubung.frage],"et",ubung.losung)
            if str(losung[ubung.frage]) == str(ubung.losung):
              cmp += 1
        msg ="le nombre de question acuis",cmp
        moglichkeit = Essai.objects.all()

        dic = {
        }
        i = 1
        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list =[]
        context = {
            'ubungs': ubungs,
            'message':msg,
            'dictionnaire':dic ,
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
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            print(list)
            print("test",dic)
            list =[]
        losung = request.GET

        context = {
            'dictionnaire':dic

        }
        return render(request, 'Grammar/index.html', context)
def cours(request):
    return render(request,'Grammar/menucours.html')
