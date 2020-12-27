from django.shortcuts import render
from django.http import HttpResponse

def Horen(request):
    return render(request, 'Horen/index.html')


def modeltest1(request):
    return render(request, 'Horen/modeltest1.html')


def modeltest2(request):
    return render(request, 'Horen/modeltest2.html')


def modeltest3(request):
    return render(request, 'Horen/modeltest3.html')


def poadcast(request):
    return render(request,'Horen/poadcast.html')
