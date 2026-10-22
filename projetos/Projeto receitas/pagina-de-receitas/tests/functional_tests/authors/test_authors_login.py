from .base import AuthorBaseTest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from django.urls import reverse
import pytest

@pytest.mark.functional_test # pytest -m 'functional_test' > apenas o selecionado
class AuthorsLoginTest(AuthorBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = '577643121Aa.'
        user = User.objects.create_user(username='username192', password=string_password)
        # usuario abre a página de login
        self.browser.get(self.live_server_url + reverse('authors:login'))
        # usuario ve o fomrulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Ex.: Orlando')
        password_field = self.get_by_placeholder(form, 'Digite sua senha')
        # usuario digita seu usuario e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)
        # usuario envia o formulario
        form.submit()
        # usuario ve a mensagem de login concluido e seu nome
        body_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertIn('Você está logado.', body_text)

        self.browser.get(self.live_server_url + reverse('authors:login'))
        body_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertIn(f'Você está logado como {user.username}.', body_text)
        # fim do test
        self.sleep(5)

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url + reverse('authors:login_create'))
        self.assertIn('Not Found', self.browser.find_element(By.TAG_NAME, 'body').text)
        
    def test_form_login_is_invalid(self):
        # usuario abre a pagina de login
        self.browser.get(self.live_server_url + reverse('authors:login'))
        # usuario ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        # tenta enviar valorez vazios
        username = self.get_by_placeholder(form, 'Ex.: Orlando')
        password = self.get_by_placeholder(form, 'Digite sua senha')
        username.send_keys(' ')
        password.send_keys(' ')
        # envia o formulario
        form.submit()
        # ve uma mensagem de erro na tela
        self.assertIn(
            'Usuário ou senha incorreto',
            self.browser.find_element(By.TAG_NAME, 'body').text)
        
    def test_form_login_is_invalid_credentials(self):
        # usuario abre a pagina de login
        self.browser.get(self.live_server_url + reverse('authors:login'))
        # usuario ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        # tenta enviar valorez com dados que não correspondem
        username = self.get_by_placeholder(form, 'Ex.: Orlando')
        password = self.get_by_placeholder(form, 'Digite sua senha')
        username.send_keys('invalid_user')
        password.send_keys('invalid_password')
        # envia o formulario
        form.submit()
        # ve uma mensagem de erro na tela
        self.assertIn(
            'Credenciais inválidas',
            self.browser.find_element(By.TAG_NAME, 'body').text)
