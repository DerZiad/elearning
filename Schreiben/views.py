#from django.shortcuts import render
from .models import TexT
from django.http import HttpResponse
# Create your views here.

def index(request):
    texts = TexT.titre.filter(available=True)
    fromatted_texts = ["<li>{}</li>".format(TexT.titre) for text in texts]
    message = """<ul>{}</ul>""".format("\n".join (fromatted_texts))
    return HttpResponse(message)


def details(request,titre_id):
    titres = titre.objects.get(pk=titre_id)
    corpss = " ".join([TexT.corps for text in TexT.corps])
    message = """<ul>{},{}</ul>""".format("\n".join(titre_id, TexT.corps))
    return HttpResponse(message)