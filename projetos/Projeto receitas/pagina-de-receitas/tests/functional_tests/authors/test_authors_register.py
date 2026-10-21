from .base import AuthorBaseTest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthorRegisterTest(AuthorBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(By.XPATH, f'.//input[@placeholder="{placeholder}"]')

    def fill_form_email20_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def get_form(self):
        return self.browser.find_element(By.XPATH, '/html/body/main/div[2]/form')

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register')
        form = self.get_form()
        self.fill_form_email20_data(form)
        form.find_element(By.NAME, 'email').send_keys('email20@email.com')
        callback(form)

    def test_empty_first_name_error_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: Orlando')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Digite seu primeiro nome antes de enviar.', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Almeida')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Digite seu último nome antes de enviar.', form.text)
        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form):
            username_field = self.get_by_placeholder(form, 'Digite seu usuário')
            username_field.clear()
            username_field.send_keys(' ' * 4)
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Digite seu usuário antes de enviar.', form.text)
        self.form_field_test_with_callback(callback)

    def test_username_already_in_use_error_message(self):
        User.objects.create_user(
            username='existing_user',
            email='existing_user@example.com',
            password='StrongPass1',
        )

        def callback(form):
            username_field = self.get_by_placeholder(form, 'Digite seu usuário')
            username_field.clear()
            username_field.send_keys('existing_user')
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Este nome de usuário já está em uso.', form.text)
        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form):
            email_field = form.find_element(By.NAME, 'email')
            email_field.clear()
            email_field.send_keys('email@invalid')
            self.browser.execute_script('arguments[0].submit()', form)
            form = self.get_form()
            self.assertIn('Digite um endereço de e-mail válido.', form.text)
        self.form_field_test_with_callback(callback)

    def test_email_already_in_use_error_message(self):
        User.objects.create_user(
            username='existing_email',
            email='existing_email@example.com',
            password='StrongPass1',
        )

        def callback(form):
            email_field = form.find_element(By.NAME, 'email')
            email_field.clear()
            email_field.send_keys('existing_email@example.com')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('User e-mail is already is use', form.text)
        self.form_field_test_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            password_field = form.find_element(By.NAME, 'password')
            password2_field = form.find_element(By.NAME, 'password2')
            password_field.clear()
            password2_field.clear()
            password_field.send_keys('StrongPass1')
            password2_field.send_keys('DifferentPass1')
            password2_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('As senhas informadas não coincidem.', form.text)
        self.form_field_test_with_callback(callback)

    def test_weak_password_error_message(self):
        def callback(form):
            password_field = form.find_element(By.NAME, 'password')
            password_field.clear()
            password_field.send_keys('abc12')
            password_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn(
                'A senha deve conter pelo menos uma letra maiúscula, '
                'uma letra minúscula e um número. Deve ter no mínimo 8 caracteres.',
                form.text,
            )
        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register')
        form = self.get_form()
        self.get_by_placeholder(form, 'Ex.: Orlando').send_keys('Orlando')
        self.get_by_placeholder(form, 'Ex.: Almeida').send_keys('Conceição')
        self.get_by_placeholder(form, 'Digite seu usuário').send_keys('orlando_test')
        self.get_by_placeholder(form, 'Digite seu e-mail').send_keys('orlando_test@example.com')
        self.get_by_placeholder(form, 'Digite sua senha').send_keys('StrongPass1')
        self.get_by_placeholder(form, 'Digite novamente sua senha').send_keys('StrongPass1')
        form.submit()
        self.assertIn('Seu cadastro foi criado!', self.browser.find_element(By.TAG_NAME, 'body').text,)