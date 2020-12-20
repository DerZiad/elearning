from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def principale(request):
    StringUser = request.session.get('username')
    if(StringUser == None or len(StringUser) == 0):
        template = loader.get_template("Home.html")
        return HttpResponse(template.render(request=request))
    else:
        template = loader.get_template("session/session.html")
        return HttpResponse(template.render(request = request))

