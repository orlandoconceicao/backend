from django.http import Http404
from django.db.models import Q
from .models import Recipe
from utils.pagination import make_pagination
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
from django.forms.models import model_to_dict
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
        qs = qs.select_related("author", "category")
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


class RecipeListViewHomeAPI(RecipeListViewBase):
    template_name = "pages/home.html"
    
    def render_to_response(self, context, **response_kwargs):
        recipes = self.get_context_data()['recipes']
        recipes_list = recipes.object_list.values()                
        return JsonResponse(list(recipes_list), safe=False)


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
        search_term = self.request.GET.get("q", "").strip()
        if not search_term:
            raise Http404()
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


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "pages/recipe-view.html"
    pk_url_kwarg = "id"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update({"is_detail_page": True})
        return ctx


class RecipeDetailAPI(RecipeDetail):
    pk_url_kwarg = "pk"

    def render_to_response(self, context, **response_kwargs):
        recipe = self.get_context_data()['recipe']
        recipe_dict = model_to_dict(recipe)
        recipe_dict['created_at'] = str(recipe.created_at)
        recipe_dict['updated_at'] = str(recipe.updated_at)
        
        if recipe_dict.get('cover'):
            recipe_dict['cover'] = self.request.build_absolute_uri(recipe_dict["cover"].url)
        else:
            recipe_dict['cover'] = ''
        
        del recipe_dict['is_published']
        del recipe_dict['preparation_steps']
        del recipe_dict['preparation_steps_is_html']
        
        return JsonResponse(recipe_dict, safe=False)