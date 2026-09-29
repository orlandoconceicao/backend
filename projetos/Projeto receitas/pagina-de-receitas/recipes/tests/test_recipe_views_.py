from django.test import TestCase

from django.urls import reverse, resolve

from recipes import views

from recipes.models import Category, Recipe, User

from .test_recipe_base import RecipeTestBase
        
class RecipeViewsTest(RecipeTestBase):
    
# HOME
    # serUp executa antes de todos os tests
    def setUp(self):
        return super().setUp()
     
    # tearDown executa depois de todos tests
    def tearDown(self):
          return super().tearDown()

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'pages/home.html')
            
    def test_recipe_home_template_shows_no_recipes_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada', response.content.decode('utf-8'))
        
# FIXTURES HOME

    def test_recipe_home_template_loads_recipes(self):          
        
        response = self.client.get(reverse('recipes:home'))
        
        content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        
        response_context_recipes = response.context['recipes']
        self.assertEqual(len(response_context_recipes), 1)

# CATEGORY

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1111}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
            response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1111}))
            self.assertEqual(response.status_code, 404)

# DETAIL

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
            response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1111}))
            self.assertEqual(response.status_code, 404)