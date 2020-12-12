from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template("Auth/connection.html")
    return HttpResponse(template.render(request = request))


def inscription(request):
    template = loader.get_template("Connection/inscription.html")
    return HttpResponse(template.render(request = request))

def seconnecter(request):
    template = loader.get_template("Connection/connection.html")
    return HttpResponse(template.render(request= request))