from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def principale(request):
    StringUser = request.session.get('username')
    if(StringUser == None or len(StringUser) == 0):
        template = loader.get_template("Home.html")
        return HttpResponse(template.render(request=request))
    else:
        succes_grammar = request.session['succes_lesen']
        succes_schreiben = request.session['succes_schreiben']
        succes_horen = request.session['succes_horen']
        succes_lesen = request.session['succes_lesen']
        total = int((succes_lesen + succes_horen + succes_schreiben + succes_grammar) / 4)
        context = {
            'total': total
        }
        return render(request, "session/session.html", context)

def afficherProfil(request):
    user = request.session['username']
    if(user == None or len(user) <= 0):
        return HttpResponseRedirect("/")
    else:
        template = loader.get_template("afficher/profil.html")
        return HttpResponse(template.render(request = request))

def impressum(request):
    template = loader.get_template("impressum.html")
    return HttpResponse(template.render())
def informationsgerman(request):
    template = loader.get_template("Info/German.html")
    return HttpResponse(template.render())
def informationsautriche(request):
    template = loader.get_template("Info/Autriche.html")
    return HttpResponse(template.render())
def infos(request):
    try:
        id = request.POST['id']
        if(id == '1'):
            informationsgerman(request)
        elif(id == '2'):
            informationsautriche(request)
        else:
            return render(request,"Info/info.html")
    except:
        return render(request, "Info/info.html")
