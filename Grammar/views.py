from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects.filter(losung=3)
    msg=["<li>{}</li>".format(beispiel.frage) for beispiel in questions]
    message = """<ul>{}</ul>""".format("\n".join(msg))
    template = loader.get_template('Grammar/base.html')
    return HttpResponse(template.render(request=request))
