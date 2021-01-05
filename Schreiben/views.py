from django.shortcuts import render
from Schreiben.Fonctions import piocher as pioche
from django.http import HttpResponse
from .models import Excercice,Reponse,Personne,Correction
from Auth.ValidEntry.sender import sendEmail
# Create your views here.

def index(request):
    if request.method == "GET":
        exercice = pioche.getSchreiben(request)
        context = {
            "exercice":exercice
        }
        return render(request,"index.html",context)
    else:
        text = request.POST['schreiben']
        id = request.POST['id']
        reponse = Reponse(rep=text,personne = Personne(username = request.session['username']),excercice = Excercice.objects.get(id=int(id)))
        reponse.save()
        reponses = Reponse.objects.all()
        reponses.remove(reponse)
        context = {
            "reponse":reponses[0],
            "reponseperso":reponse
        }
        return render(request,"response.html",context)
def correction(request):
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
            return render(request,"responste.html",context)
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
                sendEmail(info)
            if etrresponse.legal:
                correction1 = Correction(text = textcorr,remarque = remarque,reponse = etrresponse)
                info = {
                    "address": etrresponse.personne.email,
                    "text": correction.text + '\n Remarques \n' + correction1.remarque,
                    "subject": "Correction d'excercice" + correction1.reponse.excercice.sujet
                }
                sendEmail(info)
            return HttpResponse("good")


