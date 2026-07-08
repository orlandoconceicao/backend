from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contato(request):
    return HttpResponse("Esta é a página de contato!")

def sobre(request):
    return HttpResponse("Esta é a página sobre!")