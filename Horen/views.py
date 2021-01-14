from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from Home.funktions import funktion as valide
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    try:
            valide.checkSession(request)
            if request.method == "GET":
                    attributs = request.GET
                    try:
                        ids = attributs['id']
                    except:
                        ids = None
                    if ids ==  None:
                            personne = Personne.objects.get(username = request.session['username'])
                            models = ModelTest.objects.all()
                            reponses = ReponseHoren.objects.filter(personnes = personne)
                            checker = False
                            listmodeltest = []
                            for model in models:
                                for reponse in reponses:
                                    if reponse.modeltest == model:
                                        checker = True
                                if not checker:
                                    print("adding model",model.id)
                                    listmodeltest.append(model)
                                checker = False
                            paginator = Paginator(listmodeltest, 5)
                            page = request.GET.get('page')
                            try:
                                exe = paginator.page(page)
                            except PageNotAnInteger:
                                page = 1
                                exe = paginator.page(1)
                            except EmptyPage:
                                page = 1
                                exe = paginator.page(paginator.num_pages)

                            context = {
                                "messages":exe
                            }
                            return render(request,"Horen/index.html",context)
                    else:
                        id = int(ids)
                        audio = Track.objects.filter(modeltest_id=int(id))
                        question = Question.objects.filter(audio__modeltest_id=int(id))
                        choix = Choix.objects.filter(question__audio__modeltest_id=int(id))
                        message = ""
                        context = {
                            'audios': audio,
                            'question': question,
                            'choix': choix,
                            'message': message,
                            "id":id
                        }
                        return render(request, 'Horen/modeltest.html', context)

            else:
                    id = request.POST['id']
                    modeltest = ModelTest.objects.get(id = id)
                    audio = Track.objects.filter(modeltest_id=int(id))
                    question = Question.objects.filter(audio__modeltest_id=int(id))
                    choix = Choix.objects.filter(question__audio__modeltest_id=int(id))
                    message = ""
                    choixCocher = request.POST
                    note=0
                    for reponseQuestion in question:
                        if choixCocher[reponseQuestion.quest] == reponseQuestion.reponse :
                            note=note+1
                    if note >= 5:
                        message = "Vous avez validé le module"
                        personne = Personne.objects.filter(username=request.session['username']).first()
                        reponse = ReponseHoren(personnes = personne,modeltest = modeltest,valid=True)
                        reponse.save()
                        valide.saveSucess("succes_horen",valide.getSuccess("succes_horen",request) + 1,request)
                        return HttpResponseRedirect("/Horen")
                    else:
                        message = "Essayez une autre fois"
                        context = {
                            'audios': audio,
                            'question': question,
                            'choix': choix,
                            'message': message,
                            "id":id
                        }
                        return render(request, 'Horen/modeltest.html', context)
    except:
        return HttpResponseRedirect("/")
def poadcast(request):
    try:
        valide.checkSession(request)
        return render(request , 'Horen/poadcast.html')
    except:
        return HttpResponseRedirect("/")
