from django.http import HttpResponse
from django.shortcuts import render

from Grammar.models import Ubung


def grammarex(request):
    questions = Ubung.objects
    context={
        'questions':questions,
    }
    return render(request,'Grammar/test.html',context)
