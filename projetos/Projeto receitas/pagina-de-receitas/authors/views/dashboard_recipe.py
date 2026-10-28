from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from recipes.models import Recipe
from authors.forms.recipe_form import AuthorsRecipeForm


class DashboardRecipe(View):
    def get_recipe(self, id=None):
        recipe = None
        if id is not None:
            recipe = get_object_or_404(Recipe, author=self.request.user, pk=id)
                    
            return recipe
    
    def render_recipe(self, form):
        recipe_id = self.kwargs.get('id')
        form_action = (
            reverse('authors:dashboard_recipe_edit', args=[recipe_id])
            if recipe_id is not None
            else reverse('authors:dashboard_recipe_new')
        )
        return render(self.request, 'authors/pages/dashboard-recipe.html', context={
                    'form': form,
                    'form_action': form_action,
                })
        
    def get(self, request, id=None):
        recipe = self.get_recipe(id)
        form = AuthorsRecipeForm(instance=recipe)
        return self.render_recipe(form)
    
    def post(self, request, id=None):
        recipe = self.get_recipe(id)
        
        form = AuthorsRecipeForm(
            request.POST or None,
            request.FILES or None,
            instance=recipe,
        )
        
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False
            recipe.save()
            messages.success(request, 'Receita atualizada com sucesso!')
            return redirect('authors:dashboard_recipe_edit', recipe.id)
    
        return self.render_recipe(form)