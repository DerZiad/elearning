from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Home.funktions.funktion import checkSession
from Lesen.models import Text
from .models import Ubung,Essai,Personne,Reponse
from Home.funktions.funktion import saveSucess,getSuccess
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Lesen import random as randomer

def generateText(request):
    try:
        checkSession(request)
        if request.method == "POST":
            losung = request.POST
            text = Text.objects.get(id = int(losung['id']))
            ubungs = Ubung.objects.filter(type="frage",numtext = text)
            losung = request.POST
            cmp = 0
            validator = {}
            reponsejuste = {}
            erreurfausse = {}
            msg = "le nombre de question Juste est ", 0
            personne = Personne.objects.get(username=request.session['username'])
            cmp = 0
            for ubung in ubungs:
                try:
                    str(losung[ubung.frage])
                    cmp += 1
                except:
                    pass
            if cmp ==4:
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
                        saveSucess('succes_lesen', getSuccess('succes_lesen', request) + cmp, request)
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
                        text = ubungs[0].numtext
                        context = {
                            'ubungs': ubungs,
                            'paginator': True,
                            'textf':text,
                            'dictionnaire': dic,
                            'erreurs': erreurfausse,
                            'reponses': reponsejuste,
                            'validator': validator,
                            'message': msg
                        }
                        return render(request, 'Lesen/ubungs.html', context)
            else:
                context = {
                    "error":"Veuillez insérer tous les questions"
                }
                return render(request,"errorpagesession.html",context)

        else:
            ubungse = Ubung.objects.filter(type="frage")
            personne = Personne.objects.get(username=request.session['username'])
            ubungso = []
            for ubung in ubungse:
                reponse = Reponse.objects.filter(ubung=ubung, pers=personne)
                print(reponse)
                if len(reponse) == 0:
                    ubungso.append(ubung)
            if len(ubungso) != 4:
                            textop = randomer.getRandomText(ubungso,request)
                            ubungs = Ubung.objects.filter(numtext = textop)
                            dic = {
                            }
                            i = 1
                            list = []
                            paginator = Paginator(ubungs, 4)
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
                                list.insert(randomer.generateRandom(), ubung.losung)
                                dic[str(ubung.frage)] = list
                                list = []
                            jo = {}
                            for ubung in paginator.page(page).object_list:
                                jo[ubung.frage] = dic[str(ubung.frage)]
                            context = {
                                'ubungs': ubungs,
                                'textf':textop,
                                'paginator': True,
                                'messages': exe,
                                'dictionnaire': jo
                            }
                            return render(request, 'Lesen/ubungs.html', context)
    except:
        return HttpResponseRedirect("/")
