from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase


class AuthorLogoutTest(TestCase):
    def test_user_tries_to_logout_using_get_method(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        response = self.client.get(reverse('authors:logout'),follow=True)
        self.assertIn('Logout invállido', response.content.decode('utf-8'))
        
    def test_user_tries_to_logout_another_user(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        response = self.client.post(
            reverse('authors:logout'),
            data={'username': 'nouser'},
            follow=True
            )
        self.assertIn('Usuário de logout inválido', response.content.decode('utf-8'))
        
    def test_user_can_logout_seccessfully(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        response = self.client.post(
            reverse('authors:logout'),
            data={'username': 'username'},
            follow=True
            )
        self.assertIn('Logout concedido', response.content.decode('utf-8'))