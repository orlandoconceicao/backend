from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_title_includes_site_name(self):
        response = self.client.get(reverse('register'))

        self.assertContains(response, '<title>Register | Recipes</title>')
