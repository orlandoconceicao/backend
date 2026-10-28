from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from recipes.models import Recipe
from authors.forms.recipe_form import AuthorsRecipeForm


class DashboardRecipe(View):
    def get(self, request):
        recipe = get_object_or_404(Recipe, author=request.user, pk=id)
        
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
            return redirect('authors:dashboard_recipe_edit', id=id)
    
        return render(request, 'authors/pages/dashboard-recipe.html', context={
            'form': form,
            'form_action': reverse('authors:dashboard_recipe_edit', args=[id]),
        })