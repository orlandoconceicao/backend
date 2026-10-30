from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe
from utils.pagination import make_pagination
from django.views.generic import ListView
import os


# variáveis em letra maiúsculas são constantes indica que não pode ser editada
PER_PAGE = int(os.environ.get("PER_PAGE", 3))


class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = "recipes"
    paginate_by = None
    ordering = ["-id"]
    template_name = "pages/home.html"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_object, pagination_range = make_pagination(
            self.request, ctx.get("recipes"), PER_PAGE
        )
        ctx.update({"recipes": page_object, "pagination_range": pagination_range})
        return ctx


class RecipeListViewHome(RecipeListViewBase):
    template_name = "pages/home.html"


class RecipeListViewCategory(RecipeListViewBase):
    template_name = "pages/category.html"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(category__id=self.kwargs.get("category_id"))
        if not qs.exists():
            raise Http404()
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update(
            {
                "title": f"Categoria - {ctx.get('recipes')[0].category.name}",
            }
        )
        return ctx


class RecipeListViewSearch(RecipeListViewBase):
    template_name = "pages/search.html"

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get("q", "")
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) | Q(description__icontains=search_term),
            ),
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get("q", "")
        ctx.update(
            {
                "page_title": f'Search for "{search_term}"',
                "search_term": search_term,
                "additional_url_query": f"&q={search_term}",
            }
        )
        return ctx



def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(
        request,
        "pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_pages": True,
        },
    )


class RecipeDetail()