from django.shortcuts import render, get_list_or_404, get_object_or_404

from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects, category__id=category_id, is_published=True
    ).order_by("-id")

    return render(
        request,
        "pages/category.html",
        context={
            "recipes": recipes,
            "title": f"{recipes[0].category.name} - Category | ",
        },
    )


def recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(
        request,
        "pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_pages": True,
        },
    )
