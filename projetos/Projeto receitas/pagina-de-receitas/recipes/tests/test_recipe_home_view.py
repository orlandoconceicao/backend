from unittest.mock import patch

from django.conf import settings
from django.contrib.messages import constants
from django.urls import reverse, resolve

from recipes import views

from .test_recipe_base import RecipeTestBase

from unittest.mock import patch

#from unittest import skip 
# faz que o test seja ignorado #@skip('WIP') work in problems
# nas aspas e a mensagem que vai aparecer nao o padrao
        
class RecipeHomeViewsTest(RecipeTestBase):
    

    
# HOME
    # serUp executa antes de todos os tests
    # def setUp(self):
        #return super().setUp()
     
    # tearDown executa depois de todos tests
    
    # def tearDown(self):
          #return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_recipe_home_title_includes_site_name(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertContains(response, '<title>Home | Recipes</title>')
    
    def test_recipe_home_template_shows_no_recipes_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada', response.content.decode('utf-8'))

    def test_recipe_home_success_message_uses_matching_style_class(self):
        self.assertEqual(
            settings.MESSAGE_TAGS[constants.SUCCESS],
            'message-success',
        )
        
# FIXTURES HOME

    def test_recipe_home_template_loads_recipes(self):    
        # precisa criar receita      
        self.make_recipe()
        
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        
        self.assertIn('Recipe Title', content)
        
        response_context_recipes = response.context['recipes']
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_shows_page_number_with_nine_recipes(self):
        for recipe_number in range(9):
            self.make_recipe(
                slug=f'recipe-{recipe_number}',
                author_data={'username': f'user-{recipe_number}'},
            )

        with patch('recipes.views.PER_PAGES', 9):
            response = self.client.get(reverse('recipes:home'))

        self.assertContains(
            response,
            '<a class="page-link page-item page-current" href="?page=1">1</a>',
            html=True,
        )

    def test_recipe_home_page_two_shows_tenth_recipe(self):
        for recipe_number in range(10):
            self.make_recipe(
                title=f'Recipe {recipe_number}',
                slug=f'recipe-{recipe_number}',
                author_data={'username': f'user-{recipe_number}'},
            )

        with patch('recipes.views.PER_PAGES', 9):
            first_page = self.client.get(reverse('recipes:home'))
            self.assertContains(
                first_page,
                '<a class="page-link page-item" href="?page=2">2</a>',
                html=True,
            )

            second_page = self.client.get(reverse('recipes:home'), {'page': '2'})

        self.assertEqual(second_page.status_code, 200)
        self.assertEqual(len(second_page.context['recipes']), 1)
        self.assertEqual(second_page.context['recipes'][0].slug, 'recipe-0')

    def test_recipe_home_template_dont_load_recipes_not_published(self): 
        # testing recipe is_published false dont show
        # precisa criar receita      
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:home'))
        
        self.assertIn('Nenhuma receita encontrada', response.content.decode('utf-8'))
    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGES', new=3):
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(2)), 3)
        self.assertEqual(len(paginator.get_page(3)), 2)
