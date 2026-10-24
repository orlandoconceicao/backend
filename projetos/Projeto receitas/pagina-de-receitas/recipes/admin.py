from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # funciona com (), [], apenas separando com , 
    # campos encima ihual excel
    list_display = 'id', 'title', 'created_at', 'is_published', 'author',
    # se tornam clicaveis por link
    list_display_links = 'title', 'created_at',
    # adiciona eles na barra de pesquisa
    search_fields = 'id', 'title', 'description', 'slug', 'preparation_steps',
    #a diciona filtro na direita
    list_filter = 'category', 'author', 'is_published', 'preparation_steps_is_html',
    # itens por pagina
    list_per_page = 10
    # ter opção de ligar ou deligar no nosso caso publicar ou nao a receita
    # precisa existir no campo list_display
    # tem que existir virgula no final por se tartar de tupla
    list_editable = 'is_published',
    ordering = '-id',
    
admin.site.register(Category, CategoryAdmin)
