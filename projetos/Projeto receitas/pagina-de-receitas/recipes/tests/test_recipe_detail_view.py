from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


        
class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)
        
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
        self.assertIn('Recipe Preparation Steps', content)
        self.assertNotIn('ver mais...', content)

    def test_recipe_detail_template_displays_tags(self):
        recipe = self.make_recipe()
        tag = recipe.tags.create(name='Sobremesa')

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id})
        )
        content = response.content.decode('utf-8')

        self.assertContains(response, 'Tags:')
        self.assertContains(response, tag.name)
        self.assertContains(
            response,
            reverse('recipes:tag', kwargs={'slug': tag.slug}),
        )

    def test_tag_page_loads_only_recipes_with_the_selected_tag(self):
        tagged_recipe = self.make_recipe(
            title='Receita com sobremesa',
            slug='receita-com-sobremesa',
        )
        tag = tagged_recipe.tags.create(name='Sobremesa')
        other_recipe = self.make_recipe(
            title='Receita sem a tag',
            slug='receita-sem-tag',
            author_data={'username': 'other-author'},
        )

        response = self.client.get(
            reverse('recipes:tag', kwargs={'slug': tag.slug})
        )
        content = response.content.decode('utf-8')

        self.assertTemplateUsed(response, 'pages/tag.html')
        self.assertContains(response, tagged_recipe.title)
        self.assertNotContains(response, other_recipe.title)
        
    def test_recipe_detail_template_dont_load_recipe_not_published(self): 
        # Receitas não publicadas não devem aparecer nos detalhes.
        # precisa criar receita      
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        
        self.assertEqual(response.status_code, 404)
