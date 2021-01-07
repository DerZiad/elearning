from django.shortcuts import render
from Schreiben.Fonctions import piocher as pioche
from django.http import HttpResponseRedirect
from Home.funktions.funktion import checkSession
from .models import Excercice,Reponse,Personne,Correction
from Auth.ValidEntry.sender import sendEmail
# Create your views here.

def index(request):
    try:
        checkSession(request)
        if request.method == "GET":
            try:
                exercice = pioche.getSchreiben(request)
            except:
                context = {
                    "error": "Nous nous somme désolé , nous avons pas encore d'excercices de schreiben"
                }
                return render(request, "errorpagesession.html", context)
            context = {
                "exercice":exercice
            }
            return render(request,"index.html",context)
        else:
            text = request.POST['schreiben']
            id = request.POST['id']
            reponse = Reponse(rep=text,personne = Personne.objects.get(username = request.session['username']),excercice = Excercice.objects.get(id=int(id)))
            reponse.save()
            reponses = Reponse.objects.all()
            list = []
            for rep in reponses:
                if reponse != rep:
                    list.append(rep)
            try:
                reponse = list[0]
            except:
                context = {
                    "error": "Nous nous sommes désolé , nous ne avons pas autre client pour que vous corrigé"
                }
                return render(request, "errorpagesession.html", context)
            context = {
                "reponse":list[0],
                "reponseperso":reponse
            }
            return render(request,"reponse.html",context)
    except IndexError:
        return HttpResponseRedirect("/")
def correction(request):
    try:
            checkSession(request)
            if request.method == "POST":
                textcorr = request.POST['correction']
                remarque = request.POST['remarque']
                idperso = request.POST['idperso']
                reponse = Reponse.objects.get(id=int(idperso))
                etrresponse = Reponse.objects.get(id=int(request.POST['id']))
                if len(textcorr) < 20 or len(remarque) < 10:
                    context = {
                        "error":"Les champs ne respectent pas les condition",
                        "reponseperso":reponse,
                        "reponse": etrresponse
                    }
                    return render(request,"reponse.html",context)
                else:
                    reponse.legal = True
                    etrresponse.corrected= True

                    if reponse.corrected:
                        correction = Correction.objects.get(reponse = reponse)
                        info = {
                            "address" : reponse.personne.email,
                            "text": correction.text +'\n Remarques \n' + correction.remarque,
                            "subject":"Correction d'excercice" + correction.reponse.excercice.sujet
                        }
                        print("sending1")
                        sendEmail(info)
                    if etrresponse.legal:
                        print("sending2")
                        correction1 = Correction(text = textcorr,remarque = remarque,reponse = etrresponse)
                        info = {
                            "address": etrresponse.personne.email,
                            "text": correction.text + '\n Remarques \n' + correction1.remarque,
                            "subject": "Correction d'excercice" + correction1.reponse.excercice.sujet
                        }
                        sendEmail(info)
                    context = {
                        "keyword":"success",
                        "success":"Votre corrigé a été bien reçu, vous allez reçevoir votre correction sur votre email"
                    }
                    return render(request,"success.html",context)
            else:
                context = {
                    "keyword": "error",
                    "error": "n'essaye pas de pirater"
                }
                return render(request,"errorpagesession.html",context)
    except:
        return HttpResponseRedirect("/")

