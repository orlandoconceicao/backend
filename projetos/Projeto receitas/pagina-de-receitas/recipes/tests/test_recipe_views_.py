from django.urls import reverse, resolve

from recipes import views

from .test_recipe_base import RecipeTestBase

#from unittest import skip 
# faz que o test seja ignorado #@skip('WIP') work in problems
# nas aspas e a mensagem que vai aparecer nao o padrao
        
class RecipeViewsTest(RecipeTestBase):
    

    
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
    
    def test_recipe_home_template_shows_no_recipes_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Nenhuma receita encontrada', response.content.decode('utf-8'))
        
# FIXTURES HOME

    def test_recipe_home_template_loads_recipes(self):    
        # precisa criar receita      
        self.make_recipe()
        
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        
        self.assertIn('Recipe Title', content)
        
        response_context_recipes = response.context['recipes']
        self.assertEqual(len(response_context_recipes), 1)
        
    def test_recipe_home_template_dont_load_recipes_not_published(self): 
        # testing recipe is_published false dont show
        # precisa criar receita      
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:home'))
        
        self.assertIn('Nenhuma receita encontrada', response.content.decode('utf-8'))

# CATEGORY

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1111}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1111}))
        self.assertEqual(response.status_code, 404)
            
    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'this is a category' 
        # precisa criar receita          
        self.make_recipe(title=needed_title)
    
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
        
    def test_recipe_category_template_dont_load_recipes_not_published(self): 
        # testing recipe is_published false dont show
        # precisa criar receita      
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
        
        self.assertEqual(response.status_code, 404)

# DETAIL

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)
        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1111}))
        self.assertEqual(response.status_code, 404)
            
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'this is a detail page - it load one recipe' 
        # precisa criar receita          
        self.make_recipe(title=needed_title)
    
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)
        
    def test_recipe_detail_template_dont_load_recipe_not_published(self): 
        # testing recipe is_published false dont show
        # precisa criar receita      
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        
        self.assertEqual(response.status_code, 404)