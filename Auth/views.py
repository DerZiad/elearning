from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .models import Personne
from Auth.models import temporals
import Auth.ValidEntry.sender as emailsend
import hashlib
import Auth.ValidEntry.ValidatorInscript as validator
import Auth.ValidEntry.Validator as valid
import Auth.ValidEntry.utilconverter as Converter
import Auth.ValidEntry.random as randomer
import Auth.ValidEntry.sender as send
import datetime
import json
from django.core import serializers
# Create your views here.
def index(request):
    template = loader.get_template("session/session.html")
    return HttpResponse(template.render(request = request))


def inscription(request):
    if(request.method == 'GET'):
        test = Converter.testerSession(request)
        if test == False:
            template = loader.get_template("login/signup.html")
            return HttpResponse(template.render(request = request))
        else:
            return HttpResponseRedirect("/")
    else:
        id = request.POST.get('id')
        if id=="1":
            firstpane = validator.checkFirstPanelInBase(request)
            return JsonResponse(firstpane)
        elif id=="2":
            secondpane = validator.checkSecondPaneInBase(request)
            return JsonResponse(secondpane)
        else:
            try:
                    attribut = request.POST
                    nom = attribut['nom']
                    prenom = attribut['prenom']
                    birthday = attribut['datedenaissance']
                    username = attribut['username']
                    password = attribut['password']
                    email = attribut['email']
                    sexe = attribut['sexe']
                    address = attribut['address']
                    list = []
                    for chaine in birthday.split('-'):
                        list.append(chaine)
                    valid.validNom(nom)
                    valid.validPrenom(prenom)
                    valid.validSexe(sexe)
                    valid.validAdress(address)
                    valid.validEmail(email)
                    valid.validinfo(email,username)
                    cpassword = hashlib.md5(password.encode())
                    personneG = Personne(nom=nom,prenom=prenom,datedenaissance=datetime.date(year=int(list[2]), month=int(list[1]), day=int(list[0])),username=username,password = cpassword.hexdigest(),
                        email = email,Sexe = sexe,Address = address)
                    personneG.save()
                    context = {
                        "error":"",
                        "email":personneG.email
                    }
                    codeG = randomer.generateRandom()
                    temporal = temporals(personne = personneG, code = codeG)
                    temporal.save()
                    infos = {
                        'address':email,
                        'text':"Votre code de confirmation est {}".format(codeG),
                        'subject':"Confirmation de votre compte deutsch lernen"
                    }
                    send.sendEmail(infos,request)
                    return HttpResponse(render(request,"letter/confirm.html",context))
            except ValueError:
                    return HttpResponse("You re trying to hack")
def seconnecter(request):
    if(request.method == 'POST'):
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = hashlib.md5(password.encode())
        users = Personne.objects.filter(email = username,password = cpassword.hexdigest())
        if len(users) != 0:
            Converter.converttodata(request,users[0])
            return HttpResponseRedirect("/")
        else:
            test = Converter.testerSession(request)
            if test == True:
                return HttpResponseRedirect("/")
            else:
                template = loader.get_template("login/signin.html")
                erreurs = {"erreur":"Username ou mot de passe est non valide"}
                return render(request,"login/signin.html",erreurs)
    else:
        template = loader.get_template("login/signin.html")
        return HttpResponse(template.render(request= request))
def confirm(request):
    if(request.method=='POST'):
        confirm = request.POST
        code = confirm['code']
        email = confirm['email']
        personne = Personne.objects.get(email = email)
        tempo = temporals.objects.get(personne = personne)
        if(tempo != None and personne != None):
            if(code == str(tempo.code)):
                tempo.delete()
                personne.save()
                Converter.converttodata(request,personne)
                return HttpResponseRedirect("/")
            else:
                context = {
                    "codeerror":"Votre code est erroné"
                }
                return render(request,"letter/confirm.html",context)
        else:
            context = {
                "codeerror": "Vous êtes introuvable"
            }
            return render(request, "letter/confirm.html", context)



def disconnect(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect("/")
