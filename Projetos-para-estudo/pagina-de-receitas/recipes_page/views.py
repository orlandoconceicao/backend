from django.http import HttpResponse


def home(request):
    return HttpResponse("Bem-vindo à página de receitas!")

def contato(request):
    return HttpResponse("Esta é a página de contato!")

def sobre(request):
    return HttpResponse("Esta é a página sobre!")