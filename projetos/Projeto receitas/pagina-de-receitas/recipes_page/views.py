from django.shortcuts import render

from utils.recipes.factory import make_recipe

def home(request): return render(request, 'page/home.html', context={'recipes': [make_recipe() for _ in range(10)],})

def recipes(request, id): return render(request, 'page/recipe-view.html', context={'recipe': make_recipe(),})
