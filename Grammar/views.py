from builtins import print
from Home.funktions.funktion import checkSession
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from . import models

from Grammar.models import Ubung, Essai, Quiz, Tipps, Choix


def grammarex(request):


        ubungs = Ubung.objects.all()[:10]

        if request.method == "POST":

            losung = request.POST
            cmp = 0
            erreur = {}
            for ubung in ubungs:

                    if str(losung[ubung.losung]) == str(ubung.losung):
                        cmp += 1
                    msg = "le nombre de question acuis", cmp
                    print(str(losung[ubung.losung]), 'et', str(ubung.losung))
                    print('zbi')

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
                list = []

            print(dic)
            context = {
                'dictionnaire': dic,


            }
            return render(request, 'Grammar/index.html', context)



def ubung(request):
    return render(request, 'Grammar/menuubungs.html')


def gegenteile(request):

        # checkSession(request)
        ubungs = Ubung.objects.all()[10:22]

        if request.method == "POST":
            losung = request.POST
            cmp = 0

            for ubung in ubungs:

                if str(losung[ubung.losung]) == str(ubung.losung):
                    cmp += 1
                print(str(losung[ubung.losung]), 'et', str(ubung.losung))
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
                list = []
            losung = request.GET

            context = {
                'dictionnaire': dic,

            }
            return render(request, 'Grammar/gegenteile.html', context)



def bartikel(request):
    try:
        # checkSession(request)
        ubungs = Ubung.objects.all()[22:]

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

            }
            return render(request, 'Grammar/bartikel.html', context)
    except:
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
        return render(request, 'Grammar/menu.html')
    except:
        return HttpResponseRedirect('/')


def general(request):
    try:
        # checkSession(request)
        return render(request, 'Grammar/general.html')
    except:
        return HttpResponseRedirect('/')


def artikel(request):
    try:
        # checkSession(request)
        return render(request, 'Grammar/artikelcours.html')
    except:
        return HttpResponseRedirect('/')


def pronoms(request):
    return render(request, 'Grammar/pronoms.html')


def adjektive(request):
    try:
        # checkSession(request)
        return render(request, 'Grammar/adjektive.html')
    except:
        return HttpResponseRedirect('/')


def pronomsindefinis(request):
    try:
        # checkSession(request)
        return render(request, 'Grammar/pronomsindefinis.html')
    except:
        return HttpResponseRedirect('/')


def save(request):
    ubung1 = Ubung(frage="' ........ 'ist diese Frau ?Das ist meine Mutter", losung="wer")
    ubung1.save()
    ubung2 = Ubung(frage="' .......... 'bist du in Deutschland? Ich möchte Deutsch lernen.", losung="warum")
    ubung2.save()
    ubung3 = Ubung(frage="'....... 'hast du Geburtstag ? Am 10Januar", losung="wann")
    ubung3.save()
    ubung4 = Ubung(frage="' .......... ' ist mein neues Buch? Es liegt auf dem Tisch.", losung="wo")
    ubung4.save()
    ubung5 = Ubung(frage="'........ 'heisst du ? Ich heisse Ayman", losung="wie")
    ubung5.save()
    ubung6 = Ubung(frage="'....... '  wohnst du? Ich wohne in Berlin", losung="wo")
    ubung6.save()
    ubung7 = Ubung(frage="' ......... 'machst du morgen ?Ich werde meine Mutter besuchen", losung="was")
    ubung7.save()
    ubung8 = Ubung(frage="'......' alt bist du ? Ich bin 18 Jahre alt", losung="wie")
    ubung8.save()
    ubung9 = Ubung(frage="'........'bist du  ? Ich bin der neue Schüler", losung="wer")
    ubung9.save()
    ubung10 = Ubung(frage="'......' ist dein Hobby ? Ich spiele Fussball", losung="was")
    ubung10.save()
    ubung11 = Ubung(frage="dick -- '?'", losung="dünn")
    ubung11.save()
    ubung12 = Ubung(frage="voll--'?'", losung="leer")
    ubung12.save()
    ubung13 = Ubung(frage="alt--'?'", losung="jung")
    ubung13.save()
    ubung14 = Ubung(frage="hungrig--'?'", losung="satt")
    ubung14.save()
    ubung15 = Ubung(frage="jung--'?'", losung="alt")
    ubung15.save()
    ubung16 = Ubung(frage="schwach--'?'", losung="stark")
    ubung16.save()
    ubung17 = Ubung(frage="billig--'?'", losung="teuer")
    ubung17.save()
    ubung18 = Ubung(frage="arm--'?'", losung="reich")
    ubung18.save()
    ubung19 = Ubung(frage="langsam--'?'", losung="schnell")
    ubung19.save()
    ubung20 = Ubung(frage="warm--'?'", losung="kalt")
    ubung20.save()
    ubung21 = Ubung(frage="leicht--'?'", losung="schwer")
    ubung21.save()
    ubung22 = Ubung(frage="sauber--'?'", losung="schmutzig")
    ubung22.save()
    ubung23 = Ubung(frage="'?' Mann", losung="der")
    ubung23.save()
    ubung24 = Ubung(frage="'?' Frau", losung="die")
    ubung24.save()
    ubung25 = Ubung(frage="'?'--Kind", losung="das")
    ubung25.save()
    ubung26 = Ubung(frage="'?'--Bruder", losung="das")
    ubung26.save()
    ubung27 = Ubung(frage="'?'--Schwester", losung="die")
    ubung27.save()
    ubung28 = Ubung(frage="'?'--Eltern", losung="die")
    ubung28.save()
    ubung29 = Ubung(frage="'?'--Vater", losung="der")
    ubung29.save()
    ubung30 = Ubung(frage="'?'--Mutter", losung="die")
    ubung30.save()
    ubung31 = Ubung(frage="'?'--Freund", losung="der")
    ubung31.save()
    ubung32 = Ubung(frage="'?'--Haus", losung="das")
    ubung32.save()
    ubung33 = Ubung(frage="'?'--Wohnung", losung="die")
    ubung33.save()
    ubung34 = Ubung(frage="'?'--Auto", losung="das")
    ubung34.save()
    essai1 = Essai(choix="was", numf=ubung1)
    essai1.save()
    essai2 = Essai(choix="wo", numf=ubung1)
    essai2.save()
    essai3 = Essai(choix="wie", numf=ubung1)
    essai3.save()
    essai1 = Essai(choix="was", numf=ubung2)
    essai1.save()
    essai2 = Essai(choix="wie", numf=ubung2)
    essai2.save()
    essai3 = Essai(choix="wo", numf=ubung2)
    essai3.save()
    essai1 = Essai(choix="wer", numf=ubung3)
    essai1.save()
    essai2 = Essai(choix="warum", numf=ubung3)
    essai2.save()
    essai3 = Essai(choix="was", numf=ubung3)
    essai3.save()
    essai1 = Essai(choix="was", numf=ubung4)
    essai1.save()
    essai2 = Essai(choix="wie", numf=ubung4)
    essai2.save()
    essai3 = Essai(choix="warum", numf=ubung4)
    essai3.save()
    essai1 = Essai(choix="was", numf=ubung5)
    essai1.save()
    essai2 = Essai(choix="warum", numf=ubung5)
    essai2.save()
    essai3 = Essai(choix="wer", numf=ubung5)
    essai3.save()
    essai1 = Essai(choix="wie", numf=ubung6)
    essai1.save()
    essai2 = Essai(choix="warum", numf=ubung6)
    essai2.save()
    essai3 = Essai(choix="was", numf=ubung6)
    essai3.save()
    essai1 = Essai(choix="wie", numf=ubung7)
    essai1.save()
    essai2 = Essai(choix="warum", numf=ubung7)
    essai2.save()
    essai3 = Essai(choix="wer", numf=ubung7)
    essai3.save()
    essai1 = Essai(choix="was", numf=ubung8)
    essai1.save()
    essai2 = Essai(choix="wo", numf=ubung8)
    essai2.save()
    essai3 = Essai(choix="wer", numf=ubung8)
    essai3.save()
    essai1 = Essai(choix="wo", numf=ubung9)
    essai1.save()
    essai2 = Essai(choix="was", numf=ubung9)
    essai2.save()
    essai3 = Essai(choix="wie", numf=ubung9)
    essai3.save()
    essai1 = Essai(choix="wer", numf=ubung10)
    essai1.save()
    essai2 = Essai(choix="wo", numf=ubung10)
    essai2.save()
    essai3 = Essai(choix="wann", numf=ubung10)
    essai3.save()
    essai1 = Essai(choix="billig", numf=ubung11)
    essai1.save()
    essai2 = Essai(choix="gesund", numf=ubung11)
    essai2.save()
    essai3 = Essai(choix="schnell", numf=ubung11)
    essai3.save()
    essai4 = Essai(choix="billig", numf=ubung11)
    essai4.save()
    essai5 = Essai(choix="gesund", numf=ubung11)
    essai5.save()
    essai1 = Essai(choix="leicht", numf=ubung12)
    essai1.save()
    essai2 = Essai(choix="billig", numf=ubung12)
    essai2.save()
    essai3 = Essai(choix="krank", numf=ubung12)
    essai3.save()
    essai1 = Essai(choix="dünn", numf=ubung13)
    essai1.save()
    essai2 = Essai(choix="kurz", numf=ubung13)
    essai2.save()
    essai3 = Essai(choix="dick", numf=ubung13)
    essai3.save()
    essai1 = Essai(choix="voll", numf=ubung14)
    essai1.save()
    essai2 = Essai(choix="dick", numf=ubung14)
    essai2.save()
    essai3 = Essai(choix="gut", numf=ubung14)
    essai3.save()
    essai1 = Essai(choix="schlecht", numf=ubung15)
    essai1.save()
    essai2 = Essai(choix="neu", numf=ubung15)
    essai2.save()
    essai3 = Essai(choix="kalt", numf=ubung15)
    essai3.save()
    essai1 = Essai(choix="neu", numf=ubung16)
    essai1.save()
    essai2 = Essai(choix="heiss", numf=ubung16)
    essai2.save()
    essai3 = Essai(choix="glücklich", numf=ubung16)
    essai3.save()
    essai1 = Essai(choix="treu", numf=ubung17)
    essai1.save()
    essai2 = Essai(choix="gut", numf=ubung17)
    essai2.save()
    essai3 = Essai(choix="gesund", numf=ubung17)
    essai3.save()
    essai1 = Essai(choix="gesund", numf=ubung18)
    essai1.save()
    essai2 = Essai(choix="glücklich", numf=ubung18)
    essai2.save()
    essai3 = Essai(choix="stark", numf=ubung18)
    essai3.save()
    essai1 = Essai(choix="spannend", numf=ubung19)
    essai1.save()
    essai2 = Essai(choix="gross", numf=ubung19)
    essai2.save()
    essai3 = Essai(choix="heiss", numf=ubung19)
    essai3.save()
    essai1 = Essai(choix="spannend", numf=ubung20)
    essai1.save()
    essai2 = Essai(choix="gut", numf=ubung20)
    essai2.save()
    essai3 = Essai(choix="hoch", numf=ubung20)
    essai3.save()
    essai1 = Essai(choix="satt", numf=ubung21)
    essai1.save()
    essai2 = Essai(choix="reich", numf=ubung21)
    essai2.save()
    essai3 = Essai(choix="arm", numf=ubung21)
    essai3.save()
    essai1 = Essai(choix="langsam", numf=ubung22)
    essai1.save()
    essai2 = Essai(choix="alt", numf=ubung22)
    essai2.save()
    essai3 = Essai(choix="langweilig", numf=ubung22)
    essai3.save()
    essai1 = Essai(choix="die", numf=ubung23)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung23)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung24)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung24)
    essai2.save()
    essai1 = Essai(choix="die", numf=ubung25)
    essai1.save()
    essai2 = Essai(choix="der", numf=ubung25)
    essai2.save()
    essai1 = Essai(choix="die", numf=ubung26)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung26)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung27)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung27)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung28)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung28)
    essai2.save()
    essai1 = Essai(choix="die", numf=ubung29)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung29)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung30)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung30)
    essai2.save()
    essai1 = Essai(choix="die", numf=ubung31)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung31)
    essai2.save()
    essai1 = Essai(choix="die", numf=ubung32)
    essai1.save()
    essai2 = Essai(choix="der", numf=ubung32)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung33)
    essai1.save()
    essai2 = Essai(choix="das", numf=ubung33)
    essai2.save()
    essai1 = Essai(choix="der", numf=ubung34)
    essai1.save()
    essai2 = Essai(choix="die", numf=ubung34)
    essai2.save()


def pronompersonnels(request):
    return render(request, 'Grammar/pronompersonnels.html')


def adverbs(request):
    return render(request, 'Grammar/adverbs.html')


def numeraux(request):
    return render(request, 'Grammar/numeraux.html')

def quiz(request):
    quizat = Quiz.objects.all()
    tipps = Tipps.objects.all()
    essais =Choix.objects.all()
    context ={
        'quizat':quizat,
        'tipps':tipps,
        'essais':essais
    }

    return render(request,'Grammar/quiz.html',context)