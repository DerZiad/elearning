from builtins import print

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Grammar.models import Ubung, Essai


def grammarex(request):
    ubungs = Ubung.objects.all()[:10]

    if (request.method == "POST"):

        losung = request.POST
        cmp = 0
        erreur = {}
        for ubung in ubungs:
            try:
                if str(losung[ubung.frage]) == str(ubung.losung):
                    cmp += 1
                msg = "le nombre de question acuis", cmp

            except:
                msg = "veuillez selectionner tous les choix "
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

            'dictionnaire': dic,
            'erreur': erreur,
            'message': msg,
        }
        return render(request, 'Grammar/index.html', context)

    else:
        paginator = Paginator(ubungs, 3)
        seit = request.GET.get('page')
        try:
            exer = paginator.page(seit)

        except PageNotAnInteger:
            exer = paginator.page(1)

        except EmptyPage:
            exer = paginator.page(paginator.num_pages)
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
            'paginate': True,
            'exer': exer
        }
        return render(request, 'Grammar/index.html', context)


def ubung(request):
    return render(request, 'Grammar/menuubungs.html')


def gegenteile(request):
    ubungs = Ubung.objects.all()[10:22]
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
            try:
                if str(losung[ubung.frage]) == str(ubung.losung):
                    cmp += 1
                msg = "le nombre de question acuis", cmp
            except:
                msg = "veuillez selectionner tous les choix "
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

        moglichkeit = Essai.objects.all()[32:70]

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


def bartikel(request):
    ubungs = Ubung.objects.all()[22:]
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
            try:
                if str(losung[ubung.frage]) == str(ubung.losung):
                    cmp += 1
                msg = "le nombre de question acuis", cmp
            except:
                msg = "veuillez selectionner tous les choix "
        moglichkeit = Essai.objects.all()[70:]

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
        return render(request, 'Grammar/bartikel.html', context)

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
        return render(request, 'Grammar/bartikel.html', context)


def test(request):
    ubungs = Ubung.objects.all()
    dic = {}
    for ubung in ubungs:
        lists = Essai.objects.filter(numf=ubung)
        dic[ubung.frage] = lists
    list = []
    i = 1
    for ubung in ubungs:
        list.append("ubung" + str(i) + '= Ubung(frage="' + ubung.frage + '",losung="' + ubung.losung + '")')
        list.append("ubung" + str(i) + ".save()")
        i += 1
    listp = []
    i = 1
    for ubung in ubungs:
        essai = dic[ubung.frage]
        p = 1
        for ess in essai:
            listp.append("essai" + str(p) + " =" + 'Essai(choix = "' + ess.choix + '",numf=ubung' + str(i) + ')')
            listp.append("essai" + str(p) + ".save()")
            p += 1
        i += 1

    f = open("base.py", "w")
    f.write("import os \n")
    f.write('from Grammar.models import Essai,Ubung \n')
    f.write('os.system("python manage.py shell") \n')
    for ele in list:
        f.write(ele + '\n')
    for ele in listp:
        f.write(ele + '\n')
    return HttpResponse("ok")


#### ziad ###
def alphabet(request):
    return render(request, 'Grammar/cours_alphabet.html')


def menu(request):
    return render(request, 'Grammar/menu.html')


def general(request):
    return render(request, 'Grammar/general.html')


def artikel(request):
    return render(request, 'Grammar/artikelcours.html')


def pronoms(request):
    return render(request, 'Grammar/pronoms.html')

def adjektive(request):
    return  render(request,'Grammar/adjektive.html')

def pronomsindefinis(request):
    return render(request,'Grammar/pronomsindefinis.html')