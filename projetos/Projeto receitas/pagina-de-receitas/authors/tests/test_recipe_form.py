from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase
from PIL import Image

from authors.forms.recipe_form import AuthorsRecipeForm


class AuthorsRecipeFormTest(SimpleTestCase):
    def setUp(self):
        self.data = {
            'title': 'Valid recipe title',
            'description': 'A delicious recipe description',
            'preparation_time': 15,
            'preparation_time_unit': 'Minutos',
            'servings': 4,
            'servings_unit': 'Porções',
            'preparation_steps': 'Mix the ingredients and cook.',
        }

    def make_cover(self):
        image_buffer = BytesIO()
        Image.new('RGB', (1, 1)).save(image_buffer, format='PNG')
        return SimpleUploadedFile(
            'cover.png',
            image_buffer.getvalue(),
            content_type='image/png',
        )

    def make_form(self, data=None, cover=None):
        return AuthorsRecipeForm(
            data=data or self.data,
            files={'cover': cover or self.make_cover()},
        )

    def test_valid_recipe_data_passes_validation(self):
        form = self.make_form()

        self.assertTrue(form.is_valid(), form.errors)

    def test_all_fields_are_required(self):
        for field in (
            'title',
            'description',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'servings_unit',
            'preparation_steps',
            'cover',
        ):
            with self.subTest(field=field):
                data = self.data.copy()
                files = {'cover': self.make_cover()}
                if field == 'cover':
                    files = {}
                else:
                    data[field] = ''

                form = AuthorsRecipeForm(data=data, files=files)

                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_title_must_contain_at_least_five_characters(self):
        data = self.data.copy()
        data['title'] = 'Cake'
        form = self.make_form(data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_description_must_contain_at_least_five_characters(self):
        data = self.data.copy()
        data['description'] = 'Nice'
        form = self.make_form(data)

        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test_title_and_description_must_be_different(self):
        data = self.data.copy()
        data['title'] = 'Same recipe text'
        data['description'] = 'same recipe text'
        form = self.make_form(data)

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)

    def test_preparation_time_and_servings_must_be_positive(self):
        for field in ('preparation_time', 'servings'):
            with self.subTest(field=field):
                data = self.data.copy()
                data[field] = 0
                form = self.make_form(data)

                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_unit_fields_only_accept_available_choices(self):
        for field in ('preparation_time_unit', 'servings_unit'):
            with self.subTest(field=field):
                data = self.data.copy()
                data[field] = 'Invalid unit'
                form = self.make_form(data)

                self.assertFalse(form.is_valid())
                self.assertIn(field, form.errors)

    def test_cover_must_be_a_valid_image(self):
        invalid_cover = SimpleUploadedFile(
            'cover.txt',
            b'not an image',
            content_type='text/plain',
        )
        form = self.make_form(cover=invalid_cover)

        self.assertFalse(form.is_valid())
        self.assertIn('cover', form.errors)
