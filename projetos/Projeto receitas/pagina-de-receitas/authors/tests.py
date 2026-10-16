from django.test import TestCase
from django.urls import reverse

from .forms import RegisterForm


class RegisterViewTests(TestCase):
    def test_register_form_posts_to_create_view(self):
        response = self.client.get(reverse('authors:register'))

        self.assertContains(
            response,
            f'<form action="{reverse("authors:create")}" method="POST">',
        )

    def test_register_title_includes_site_name(self):
        response = self.client.get(reverse('register'))

        self.assertContains(response, '<title>Register | Recipes</title>')

    def test_name_placeholders_are_not_duplicated(self):
        form = RegisterForm()

        self.assertEqual(
            form.fields['first_name'].widget.attrs['placeholder'],
            'Ex.: Orlando',
        )
        self.assertEqual(
            form.fields['last_name'].widget.attrs['placeholder'],
            'Ex.: Almeida',
        )

    def test_register_shows_error_when_passwords_differ(self):
        response = self.client.post(
            reverse('authors:create'),
            {
                'first_name': 'Orlando',
                'last_name': 'Almeida',
                'username': 'orlando',
                'email': 'orlando@example.com',
                'password': 'password-one',
                'password2': 'password-two',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'As senhas devem ser iguais.')
