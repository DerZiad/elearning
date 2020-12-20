from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects.filter(losung=3)
    msg=["<li>{}</li>".format(beispiel.title) for beispiel in questions]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))

    return HttpResponse()
