from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Grammar.models import Ubung, Essai


def grammarex(request):
    ubungs = Ubung.objects.all()[:7]

    if (request.method == "POST"):
        paginator = Paginator(ubungs, 3)
        seit = request.POST.get('page')
        try:
            exer = paginator.page(seit)

        except PageNotAnInteger:
            exer = paginator.page(1)

        except EmptyPage:
            exer = paginator.page(paginator.num_pages)
        losung = request.POST
        cmp = 0

        for ubung in ubungs:

            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
        msg = "le nombre de question acuis", cmp
        moglichkeit = Essai.objects.all()[:32]

        dic = {
        }

        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list = []
        context = {
            'ubungs': ubungs,
            'message': msg,
            'dictionnaire': dic,
            'paginate': True

        }
        return render(request, 'Grammar/index.html', context)

    else:

        moglichkeit = Essai.objects.all()[:32]

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
            print("test", dic)
            list = []
        losung = request.GET

        context = {
            'dictionnaire': dic,
            'paginate': True
        }
        return render(request, 'Grammar/index.html', context)


def cours(request):
    return render(request, 'Grammar/menucours.html')


def gegenteile(request):
    ubungs = Ubung.objects.all()[7:]
    paginator = Paginator(ubungs, 3)
    seit = request.POST.get('page')
    try:
        exer = paginator.page(seit)

    except PageNotAnInteger:
        exer = paginator.page(1)

    except EmptyPage:
        exer = paginator.page(paginator.num_pages)
    if (request.method == "POST"):
        losung = request.POST
        cmp = 0

        for ubung in ubungs:
            print(losung[ubung.frage], "et", ubung.losung)
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
        msg = "le nombre de question acuis", cmp
        moglichkeit = Essai.objects.all()[32:]

        dic = {
        }

        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list = []
        context = {
            'ubungs': ubungs,
            'message': msg,
            'dictionnaire': dic,
            'paginate': True

        }
        return render(request, 'Grammar/gegenteile.html', context)

    else:

        moglichkeit = Essai.objects.all()[32:]

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
            print("test", dic)
            list = []
        losung = request.GET

        context = {
            'dictionnaire': dic,
            'paginate': True
        }
        return render(request, 'Grammar/gegenteile.html', context)

