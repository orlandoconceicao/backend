from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from .models import Recipe
from django.core.paginator import Paginator
from utils.pagination import make_pagination
import os


# variáveis em letra maiúsculas são constantes indica que não pode ser editada
PER_PAGE = int(os.environ.get('PER_PAGE', 3))

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(
        request,"pages/home.html", 
        context={
            "recipes": page_object,
            "pagination_range": pagination_range,
        })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.order_by("-id"),
        category__id=category_id,
        is_published=True,
    )
    
    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    return render(
        request,"pages/category.html",
        context={
            "recipes": page_object,
            "pagination_range": pagination_range,
            "title": f"{recipes[0].category.name} - Category",
        },
    )


def recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request,"pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_pages": True,
        },
    )


def search(request):
    search_term = request.GET.get("q", "").strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")
    
    page_object, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(
        request,"pages/search.html",
        {
            "page_title": f'Search for "{search_term}"',
            "search_term": search_term,
            "recipes": page_object,
            "pagination_range": pagination_range,
            "additional_url_query" : f'&q={search_term}',
        },
    )
