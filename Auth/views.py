from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import Personne,User
import Auth.ValidEntry.ValidatorInscript as validator
# Create your views here.

def index(request):
    template = loader.get_template("Auth/connection.html")
    return HttpResponse(template.render(request = request))


def inscription(request):
    if(request.method == 'GET'):
        template = loader.get_template("login/signup.html")
        return HttpResponse(template.render(request = request))
    else:
        id = request.POST.get('id')
        if(id=="1"):
            firstpane = validator.checkFirstPanelInBase(request)
            return JsonResponse(firstpane)
        elif(id=="2"):
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
            personne = User(nom=nom,prenom=prenom,datedenaissance=birthday,username=username,password = password,
                email = email,telephone = telephone)
            personne.save()
            #return HttpResponse("<h1>Good</h1>")
            firstpane = validator.checkFirstPanelInBase(request)
            return JsonResponse(firstpane)
def seconnecter(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username = username,password = password)
        if(len(users) != 0):
            return
        else:
            return JsonResponse()
    else:
        template = loader.get_template("login/signin.html")
        return HttpResponse(template.render(request= request))