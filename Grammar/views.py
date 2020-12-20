from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects.filter(frage="hh")
    msg=["<li>{}</li>".format(beispiel.frage) for beispiel in questions]
    message = """<ul>{}</ul>""".format("\n".join(msg))
    context ={
        'questions':questions
    }
    return render(request,'Grammar/index.html',context)
