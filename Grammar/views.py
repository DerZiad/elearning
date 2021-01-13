from builtins import print

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from Home.funktions.funktion import checkSession,getSuccess,saveSucess
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.template import loader
from . import models
from Auth.models import Personne
from .random import generateRandom
from Grammar.models import Ubung, Essai,Reponse


def grammarex(request):
   try :
        checkSession(request)
        c = Ubung.objects.filter(type="frage")
        if request.method == "POST":
            losung = request.POST
            ubungs = []
            for frage,losung in losung.items():
                for ubung in c:
                    if ubung.frage == frage:
                        ubungs.append(Ubung.objects.get(frage = frage,type="frage"))
            if len(ubungs) == 6:
                    losung = request.POST
                    cmp = 0
                    validator = {}
                    reponsejuste = {}
                    erreurfausse = {}
                    msg = ""
                    personne = Personne.objects.get(username = request.session['username'])
                    for ubung in ubungs:
                       try:
                            if str(losung[ubung.frage]) == str(ubung.losung):
                                reponse = Reponse(ubung=ubung, valide=True, pers=personne)
                                reponse.save()
                                cmp += 1
                                validator[ubung.frage] = True
                                reponsejuste[ubung.frage] = losung[ubung.frage]
                                msg = "le nombre de question Juste est ", cmp
                            else:
                                validator[ubung.frage] = False
                                erreurfausse[ubung.frage] = losung[ubung.frage]
                                reponsejuste[ubung.frage] = ubung.losung
                       except :
                            context = {
                                "error": "Veuillez selectionner tous les choix "
                            }
                            return render(request, "Grammar/errorpage.html", context)
                    saveSucess('succes_grammar',getSuccess('succes_grammar',request) + cmp,request)
                    dic = {
                    }

                    list = []
                    for ubung in ubungs:
                        list.append(ubung.losung)
                        moglichkeit = Essai.objects.filter(numf=ubung)
                        for mog in moglichkeit:
                            if mog.numf == ubung:
                                list.append(mog.choix)
                        dic[str(ubung.frage)] = list
                        list = []

                    context = {
                        'ubungs': ubungs,
                        'dictionnaire': dic,
                        'erreurs': erreurfausse,
                        'reponses':reponsejuste,
                        'validator':validator,
                        'message': msg
                    }
                    return render(request, 'Grammar/index.html', context)
            else:
                context = {
                    "error": "Veuillez selectionner tous les choix "
                }
                return render(request, "Grammar/errorpage.html", context)

        else:
            ubungse = Ubung.objects.filter(type="frage")
            personne = Personne.objects.get(username = request.session['username'])
            ubungs = []
            for ubung in ubungse:
                reponse = Reponse.objects.filter(ubung=ubung,pers=personne)
                if len(reponse) == 0:
                    ubungs.append(ubung)
            if len(ubungs) != 0:
                    dic = {
                    }
                    i = 1
                    list = []
                    paginator=Paginator(ubungs,6)
                    page=request.GET.get('page')
                    try:
                        exe = paginator.page(page)
                    except PageNotAnInteger:
                        page = 1
                        exe = paginator.page(1)
                    except EmptyPage:
                        page = 1
                        exe= paginator.page(paginator.num_pages)

                    for ubung in ubungs:
                        moglichkeit = Essai.objects.filter(numf=ubung)
                        for mog in moglichkeit:
                            if mog.numf == ubung:
                                list.append(mog.choix)
                        list.insert(generateRandom(),ubung.losung)
                        dic[str(ubung.frage)] = list
                        list = []
                    jo = {}
                    for ubung in paginator.page(page).object_list:
                        jo[ubung.frage] = dic[str(ubung.frage)]

                    print(dic)
                    context = {
                        'ubungs': ubungs,
                        'paginator': True,
                        'messages': exe,
                        'dictionnaire': jo
                    }
                    return render(request, 'Grammar/index.html', context)
            else:
                return render(request, "Grammar/success")
   except:
        return HttpResponseRedirect('/')

def ubung(request):
   try :
    checkSession(request)
    return render(request, 'Grammar/menuubungs.html')
   except :
    return HttpResponseRedirect('/')

def gegenteile(request):
  try :
    checkSession(request)
    c = Ubung.objects.filter(type="gegen")
    if request.method == "POST":
        losung = request.POST
        ubungs = []
        for frage, losung in losung.items():
            for ubung in c:
                if ubung.frage == frage:
                    ubungs.append(Ubung.objects.get(frage=frage, type="gegen"))
        losung = request.POST
        cmp = 0
        validator = {}
        reponsejuste = {}
        erreurfausse = {}
        msg = "le nombre de question Juste est ", 0
        personne = Personne.objects.get(username=request.session['username'])
        for ubung in ubungs:
            reponse = Reponse(ubung=ubung, valide=True, pers=personne)
            reponse.save()
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
                validator[ubung.frage] = True
                reponsejuste[ubung.frage] = losung[ubung.frage]
                msg = "le nombre de question Juste est ", cmp
            else:
                validator[ubung.frage] = False
                erreurfausse[ubung.frage] = losung[ubung.frage]
                reponsejuste[ubung.frage] = ubung.losung
        saveSucess('succes_grammar', getSuccess('succes_grammar', request) + cmp, request)
        dic = {
        }

        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list = []

        context = {
            'ubungs': ubungs,
            'paginator': True,

            'dictionnaire': dic,
            'erreurs': erreurfausse,
            'reponses': reponsejuste,
            'validator': validator,
            'message': msg
        }
        return render(request, 'Grammar/index.html', context)

    else:
        ubungse = Ubung.objects.filter(type="gegen")
        personne = Personne.objects.get(username=request.session['username'])
        ubungs = []
        for ubung in ubungse:
            reponse = Reponse.objects.filter(ubung=ubung, pers=personne)
            if len(reponse) == 0:
                ubungs.append(ubung)

        dic = {
        }
        i = 1
        list = []
        paginator = Paginator(ubungs, 6)
        page = request.GET.get('page')
        try:
            exe = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            exe = paginator.page(1)
        except EmptyPage:
            page = 1
            exe = paginator.page(paginator.num_pages)

        for ubung in ubungs:
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            list.insert(generateRandom(), ubung.losung)
            dic[str(ubung.frage)] = list
            list = []
        jo = {}
        for ubung in paginator.page(page).object_list:
            jo[ubung.frage] = dic[str(ubung.frage)]

        print(dic)
        context = {
            'ubungs': ubungs,
            'paginator': True,
            'messages': exe,
            'dictionnaire': jo
        }
        return render(request, 'Grammar/gegenteile.html', context)
  except :
     return HttpResponseRedirect('/')
def bartikel(request):
  try :
    checkSession(request)
    c = Ubung.objects.filter(type="ba")
    if request.method == "POST":
        losung = request.POST
        ubungs = []
        for frage, losung in losung.items():
            for ubung in c:
                if ubung.frage == frage:
                    ubungs.append(Ubung.objects.get(frage=frage, type="ba"))
        losung = request.POST
        cmp = 0
        validator = {}
        reponsejuste = {}
        erreurfausse = {}
        msg = "le nombre de question Juste est ", 0
        personne = Personne.objects.get(username=request.session['username'])
        for ubung in ubungs:
            reponse = Reponse(ubung=ubung, valide=True, pers=personne)
            reponse.save()
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
                validator[ubung.frage] = True
                reponsejuste[ubung.frage] = losung[ubung.frage]
                msg = "le nombre de question Juste est ", cmp
            else:
                validator[ubung.frage] = False
                erreurfausse[ubung.frage] = losung[ubung.frage]
                reponsejuste[ubung.frage] = ubung.losung
        saveSucess('succes_grammar', getSuccess('succes_grammar', request) + cmp, request)
        dic = {
        }

        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list = []

        context = {
            'ubungs': ubungs,
            'paginator': True,

            'dictionnaire': dic,
            'erreurs': erreurfausse,
            'reponses': reponsejuste,
            'validator': validator,
            'message': msg
        }
        return render(request, 'Grammar/bartikel.html', context)

    else:
        ubungse = Ubung.objects.filter(type="ba")
        personne = Personne.objects.get(username=request.session['username'])
        ubungs = []
        for ubung in ubungse:
            reponse = Reponse.objects.filter(ubung=ubung, pers=personne)
            if len(reponse) == 0:
                ubungs.append(ubung)

        dic = {
        }
        i = 1
        list = []
        paginator = Paginator(ubungs, 6)
        page = request.GET.get('page')
        try:
            exe = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            exe = paginator.page(1)
        except EmptyPage:
            page = 1
            exe = paginator.page(paginator.num_pages)

        for ubung in ubungs:
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            list.insert(generateRandom(), ubung.losung)
            dic[str(ubung.frage)] = list
            list = []
        jo = {}
        for ubung in paginator.page(page).object_list:
            jo[ubung.frage] = dic[str(ubung.frage)]

        print(dic)
        context = {
            'ubungs': ubungs,
            'paginator': True,
            'messages': exe,
            'dictionnaire': jo
        }
        return render(request, 'Grammar/bartikel.html', context)
  except :
    return HttpResponseRedirect('/')

def test(request):
        ubungs = Ubung.objects.all()
        dic = {}
        for ubung in ubungs:
            lists = Essai.objects.filter(numf=ubung)
            dic[ubung.frage] = lists
        list = []
        i = 1
        for ubung in ubungs:
            list.append("ubung" + str(i) + '= Ubung(frage=\"' + ubung.frage + '\",losung=\"' + ubung.losung + '\")')
            list.append("ubung" + str(i) + ".save()")
            i += 1
        listp = []
        i = 1
        for ubung in ubungs:
            essai = dic[ubung.frage]
            p = 1
            for ess in essai:
                listp.append("essai" + str(p) + " =" + 'Essai(choix = \"' + ess.choix + '\",numf=ubung' + str(i) + ')')
                listp.append("essai" + str(p) + ".save()")
                p += 1
            i += 1

        f = open("base.py", "w", encoding='utf-8')
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
    try:
        # checkSession(request)
        return render(request, 'Grammar/cours_alphabet.html')
    except:
        return HttpResponseRedirect('/')


def menu(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/menu.html')
    except:
        return HttpResponseRedirect('/')


def general(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/general.html')
    except:
        return HttpResponseRedirect('/')


def artikel(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/artikelcours.html')
    except:
        return HttpResponseRedirect('/')


def pronoms(request):
    return render(request, 'Grammar/pronoms.html')


def adjektive(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/adjektive.html')
    except:
        return HttpResponseRedirect('/')


def pronomsindefinis(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/pronomsindefinis.html')
    except:
        return HttpResponseRedirect('/')


def pronompersonnels(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/pronompersonnels.html')
    except:
        return HttpResponseRedirect("/")


def adverbs(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/adverbs.html')
    except:
        return HttpResponseRedirect("/")


def numeraux(request):
    try:
        checkSession(request)
        return render(request, 'Grammar/numeraux.html')
    except:
        return HttpResponseRedirect("/")



def ua(request):
  try :
    checkSession(request)
    c = Ubung.objects.filter(type="ua")
    if request.method == "POST":
        losung = request.POST
        ubungs = []
        for frage, losung in losung.items():
            for ubung in c:
                if ubung.frage == frage:
                    ubungs.append(Ubung.objects.get(frage=frage, type="ua"))
        losung = request.POST
        cmp = 0
        validator = {}
        reponsejuste = {}
        erreurfausse = {}
        msg = "le nombre de question Juste est ", 0
        personne = Personne.objects.get(username=request.session['username'])
        for ubung in ubungs:
            reponse = Reponse(ubung=ubung, valide=True, pers=personne)
            reponse.save()
            if str(losung[ubung.frage]) == str(ubung.losung):
                cmp += 1
                validator[ubung.frage] = True
                reponsejuste[ubung.frage] = losung[ubung.frage]
                msg = "le nombre de question Juste est ", cmp
            else:
                validator[ubung.frage] = False
                erreurfausse[ubung.frage] = losung[ubung.frage]
                reponsejuste[ubung.frage] = ubung.losung
        saveSucess('succes_grammar', getSuccess('succes_grammar', request) + cmp, request)
        dic = {
        }

        list = []
        for ubung in ubungs:
            list.append(ubung.losung)
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            dic[str(ubung.frage)] = list
            list = []

        context = {
            'ubungs': ubungs,
            'paginator': True,

            'dictionnaire': dic,
            'erreurs': erreurfausse,
            'reponses': reponsejuste,
            'validator': validator,
            'message': msg
        }
        return render(request, 'Grammar/ua.html', context)

    else:
        ubungse = Ubung.objects.filter(type="ua")
        personne = Personne.objects.get(username=request.session['username'])
        ubungs = []
        for ubung in ubungse:
            reponse = Reponse.objects.filter(ubung=ubung, pers=personne)
            if len(reponse) == 0:
                ubungs.append(ubung)

        dic = {
        }
        i = 1
        list = []
        paginator = Paginator(ubungs, 6)
        page = request.GET.get('page')
        try:
            exe = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            exe = paginator.page(1)
        except EmptyPage:
            page = 1
            exe = paginator.page(paginator.num_pages)

        for ubung in ubungs:
            moglichkeit = Essai.objects.filter(numf=ubung)
            for mog in moglichkeit:
                if mog.numf == ubung:
                    list.append(mog.choix)
            list.insert(generateRandom(), ubung.losung)
            dic[str(ubung.frage)] = list
            list = []
        jo = {}
        for ubung in paginator.page(page).object_list:
            jo[ubung.frage] = dic[str(ubung.frage)]

        print(dic)
        context = {
            'ubungs': ubungs,
            'paginator': True,
            'messages': exe,
            'dictionnaire': jo
        }
        return render(request, 'Grammar/ua.html', context)
  except :
        return HttpResponseRedirect('/')