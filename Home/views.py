from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def principale(request):
    template = loader.get_template("session/session.html")
    return HttpResponse(template.render(request = request))

