from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .models import Personne
import Auth.ValidEntry.sender as emailsend
import hashlib
import Auth.ValidEntry.ValidatorInscript as validator
import Auth.ValidEntry.utilconverter as Converter
import Auth.ValidEntry.random as randomer
import Auth.ValidEntry.sender as send
import json
from django.core import serializers
# Create your views here.
personneG = Personne()
codeG = ""
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
            attiribut = request.POST
            nom = attiribut['nom']
            prenom = attiribut['prenom']
            birthday = attiribut['datedenaissance']
            username = attiribut['username']
            password = attiribut['password']
            email = attiribut['email']
            telephone = attiribut['telephone']
            cpassword = hashlib.md5(password.encode())
            personneG = Personne(nom=nom,prenom=prenom,datedenaissance=birthday,username=username,password = cpassword.hexdigest(),
                email = email,telephone = telephone)
            context = {
                "error":""
            }
            codeG = randomer.generateRandom()
            infos = {
                'address':email,
                'text':"Votre code de confirmation est {}".format(codeG),
                'subject':"Confirmation de votre compte deutsch lernen"
            }
            send.sendEmail(infos,request)
            return HttpResponse(render(request,"letter/confirm.html",context))
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
        if(code == str(codeG)):
            personneG.save()
            Converter.converttodata(request,personneG)
            return HttpResponseRedirect("/")
        else:
            context = {
                "codeerror":"Votre code est erroné"
            }
            return render(request,"letter/letter.html",context)



def disconnect(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect("/")
