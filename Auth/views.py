from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .models import Personne
import Auth.ValidEntry.sender as emailsend
import hashlib
import Auth.ValidEntry.ValidatorInscript as validator
import Auth.ValidEntry.Validator as valid
import Auth.ValidEntry.utilconverter as Converter
import Auth.ValidEntry.random as randomer
import Auth.ValidEntry.sender as send
import datetime
from Home.funktions import funktion as checker
import json
from django.core import serializers
# Create your views here.
def index(request):
    try:
        checker.checkSession(request)
    except IndexError:
        template = loader.get_template("session/session.html")
        return HttpResponse(template.render(request = request))



def inscription(request):
    try:
        checker.checkSession(request)
    except IndexError:
        if request.method == 'GET':
            test = Converter.testerSession(request)
            if not test:
                template = loader.get_template("login/signup.html")
                return HttpResponse(template.render(request=request))
            else:
                return HttpResponseRedirect("/")
        else:
            id = request.POST.get('id')
            if id == "1":
                firstpane = validator.checkFirstPanelInBase(request)
                return JsonResponse(firstpane)
            elif id == "2":
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
                    valid.validinfo(email, username)
                    cpassword = hashlib.md5(password.encode())
                    print("1")
                    personneG = Personne(nom=nom, prenom=prenom,
                                         datedenaissance=datetime.date(year=int(list[2]), month=int(list[1]),
                                                                       day=int(list[0])), username=username,
                                         password=cpassword.hexdigest(),
                                         email=email, Sexe=sexe, Address=address)
                    personneG.save()
                    context = {
                        "error": "",
                        "email": personneG.email
                    }
                    codeG = randomer.generateRandom()
                    request.session['codeG'] = codeG
                    infos = {
                        'address': email,
                        'text': "Votre code de confirmation est {}".format(codeG),
                        'subject': "Confirmation de votre compte deutsch lernen"
                    }
                    send.sendEmail(infos, request)
                    return HttpResponse(render(request, "letter/notvalid.html", context))
                except ValueError:
                    return HttpResponse("You re trying to hack")
def seconnecter(request):
    try:
            checker.checkSession(request)
    except IndexError:
            if request.method == 'POST':
                username = request.POST.get('email')
                password = request.POST.get('password')
                cpassword = hashlib.md5(password.encode())
                user = Personne.objects.filter(email=username, password=cpassword.hexdigest())
                if len(user) != 0:
                    users = user[0]
                    if users.valid:
                        Converter.converttodata(request, users)
                        return HttpResponseRedirect("/")
                    else:
                        codeG = randomer.generateRandom()
                        request.session['codeG'] = codeG
                        infos = {
                            'address': users.email,
                            'text': "Votre code de confirmation est {}".format(codeG),
                            'subject': "Confirmation de votre compte deutsch lernen"
                        }
                        send.sendEmail(infos, request)
                        context = {
                            "email":user[0].email
                        }
                        return render(request,"login/notvalid.html",context)
                else:
                    template = loader.get_template("login/signin.html")
                    erreurs = {"erreur": "Username ou mot de passe est non valide"}
                    return render(request, "login/signin.html", erreurs)
            else:
                test = Converter.testerSession(request)
                if test:
                    return HttpResponseRedirect("/")
                else:
                    template = loader.get_template("login/signin.html")
                    return HttpResponse(template.render(request=request))

def confirm(request):
    try:
        checker.checkSession(request)
    except IndexError:
        if request.method == 'POST':
            confirm = request.POST
            code = confirm['code']
            email = confirm['email']
            print("your email is ",email)
            personne = Personne.objects.get(email=email)
            codeG = request.session['codeG']
            if code != None and personne != None :
                if code == str(codeG):
                    personne.valid = True
                    personne.save()
                    Converter.converttodata(request,personne)
                    return HttpResponseRedirect("/")
                else:
                    context = {
                        "codeerror":"Votre code est erroné"
                    }
                    return render(request,"login/notvalid.html",context)
            else:
                context = {
                    "codeerror": "Vous êtes introuvable"
                }
                return render(request, "login/notvalid.html", context)



def disconnect(request):
    try:
        checker.checkSession(request)
        request.session.flush()
        request.session.clear_expired()
        return HttpResponseRedirect("/")
    except:
        return  HttpResponseRedirect("/")
def suprimerNotValid(request):
    email = request.POST['email']
    personne = Personne.objects.get(email = email)
    personne.delete()

def recoverPassword(request):
    if request.method == "GET":
        try:
            id = request.GET['id']
            if id == None:
                raise IndexError
            if id == request.session['codeh']:
                context = {
                    "id" : id
                }
                return  render(request,"recover/password.html",context)

        except:
            return render(request,"recover/recoverpassword.html")
    else:
        code = randomer.generateRandom()
        email = request.POST['email']
        link = "http://127.0.0.1:8000/recover?id=" + code
        request.session['codeh'] = str(code)
        request.session['email'] = email
        info = {
            'address': email,
            'text': "Votre lien de récuperation de mot de passe est : " + link,
            'subject': "Recuperer le mot de passe"
        }
        send.sendEmail(info,request)
        return render(request,"recover/message.html")
