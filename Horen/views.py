from django.shortcuts import render
from django.http import HttpResponse



def Horen(request):
    return render(request, 'Horen/base.html')


def modeltest1(request):
    return render(request, 'Horen/modeltest1.html')


def modeltest2(response):
    return HttpResponse('<h1> ModelTest 1</h1>')


def modeltest3(response):
    return HttpResponse('<h1> ModelTest 1</h1>')


def poadcast(response):
    return HttpResponse('<h1>Poadcast</h1>')
