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
        succes_grammar = request.session['succes_lesen']
        succes_schreiben = request.session['succes_schreiben']
        succes_horen = request.session['succes_horen']
        succes_lesen = request.session['succes_lesen']
        total = int((succes_lesen + succes_horen + succes_schreiben + succes_grammar) / 4)
        context = {
            'total':total
        }
        return render(request,"session/session.html",context)

