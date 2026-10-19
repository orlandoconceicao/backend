from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorLoginTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'Str0ngP@ssword1'
        User.objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.login_url = reverse('authors:login_create')

    def test_valid_credentials_log_in_and_redirect_to_home(self):
        response = self.client.post(
            self.login_url,
            {'username': self.username, 'password': self.password},
            follow=True,
        )

        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.redirect_chain, [('/', 302)])
        self.assertContains(response, 'Você está logado.')

    def test_invalid_credentials_show_error_and_redirect_to_login(self):
        response = self.client.post(
            self.login_url,
            {'username': self.username, 'password': 'wrong-password'},
            follow=True,
        )

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.redirect_chain, [('/authors/login/', 302)])
        self.assertContains(response, 'Credenciais inválidas')

    def test_logout_button_logs_out_and_redirects_to_login(self):
        user = User.objects.get(username=self.username)
        self.client.force_login(user)

        page = self.client.get(reverse('authors:login'))
        self.assertContains(
            page,
            '<form class="inline-form" action="/authors/logout/create/" method="post">',
        )
        self.assertContains(page, 'Você está logado com testuser.')
        self.assertContains(
            page,
            '<button class="plaintext-button" type="submit">clique aqui</button>',
        )

        response = self.client.post(
            reverse('authors:logout'),
            follow=True,
        )

        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.redirect_chain, [('/authors/login/', 302)])
