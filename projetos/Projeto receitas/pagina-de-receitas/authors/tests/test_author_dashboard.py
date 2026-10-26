from io import BytesIO
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from PIL import Image
from recipes.models import Recipe
from recipes.tests.test_recipe_base import RecipeMixing


class AuthorDashboardTest(TestCase, RecipeMixing):
    def test_dashboard_shows_all_recipes_owned_by_logged_in_author(self):
        published_recipe = self.make_recipe(
            title='Published recipe',
            slug='published-recipe',
            author_data={'username': 'orlando'},
        )
        author = published_recipe.author
        draft_recipe = self.make_recipe(
            title='Draft recipe',
            slug='draft-recipe',
            author_data={'username': 'orlando-draft'},
            is_published=False,
        )
        draft_recipe.author = author
        draft_recipe.save(update_fields=['author'])
        self.make_recipe(
            title='Another author recipe',
            slug='another-author-recipe',
            author_data={'username': 'another-author'},
        )
        self.client.force_login(author)

        response = self.client.get(reverse('authors:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published recipe')
        self.assertContains(response, 'Draft recipe')
        self.assertNotContains(response, 'Another author recipe')
        self.assertEqual(len(response.context['recipes']), 2)

    def test_edit_page_loads_for_logged_in_recipe_author(self):
        recipe = self.make_recipe(
            title='Recipe to edit',
            slug='recipe-to-edit',
            author_data={'username': 'recipe-author'},
            is_published=False,
        )
        self.client.force_login(recipe.author)

        response = self.client.get(
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard Recipe')
        self.assertEqual(response.context['form'].instance, recipe)
        self.assertEqual(
            response.context['form_action'],
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk]),
        )

    def test_edit_page_updates_recipe_on_post(self):
        recipe = self.make_recipe(
            title='Original recipe title',
            slug='original-recipe-title',
            author_data={'username': 'recipe-editor'},
            is_published=False,
        )
        self.client.force_login(recipe.author)

        response = self.client.post(
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk]),
            {
                'title': 'Updated recipe title',
                'description': recipe.description,
                'preparation_time': recipe.preparation_time,
                'preparation_time_unit': recipe.preparation_time_unit,
                'servings': recipe.servings,
                'servings_unit': recipe.servings_unit,
                'preparation_steps': recipe.preparation_steps,
            },
        )

        self.assertRedirects(
            response,
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk]),
        )
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, 'Updated recipe title')

    def test_edit_page_does_not_allow_editing_another_authors_recipe(self):
        recipe = self.make_recipe(
            title='Other authors recipe',
            slug='other-authors-recipe',
            author_data={'username': 'recipe-owner'},
            is_published=False,
        )
        other_author = self.make_author(username='other-editor')
        self.client.force_login(other_author)

        response = self.client.get(
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk])
        )

        self.assertEqual(response.status_code, 404)

    def test_new_recipe_page_loads_with_create_url_as_form_action(self):
        author = self.make_author(username='recipe-creator')
        self.client.force_login(author)

        response = self.client.get(reverse('authors:dashboard_recipe_new'))

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['form'].instance.pk)
        self.assertEqual(
            response.context['form_action'],
            reverse('authors:dashboard_recipe_new'),
        )

    def test_new_recipe_page_creates_recipe_for_logged_in_author(self):
        author = self.make_author(username='recipe-creator')
        self.client.force_login(author)
        image_buffer = BytesIO()
        Image.new('RGB', (1, 1)).save(image_buffer, format='PNG')
        cover = SimpleUploadedFile(
            'cover.png',
            image_buffer.getvalue(),
            content_type='image/png',
        )

        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.post(
                    reverse('authors:dashboard_recipe_new'),
                    {
                        'title': 'New recipe',
                        'description': 'A description',
                        'preparation_time': 10,
                        'preparation_time_unit': 'Minutos',
                        'servings': 2,
                        'servings_unit': 'Porções',
                        'preparation_steps': 'Prepare the recipe',
                        'cover': cover,
                    },
                )

        recipe = Recipe.objects.get(title='New recipe')
        self.assertRedirects(
            response,
            reverse('authors:dashboard_recipe_edit', args=[recipe.pk]),
        )
        self.assertEqual(recipe.author, author)
        self.assertEqual(recipe.slug, 'new-recipe')
        self.assertFalse(recipe.is_published)
        self.assertFalse(recipe.preparation_steps_is_html)
