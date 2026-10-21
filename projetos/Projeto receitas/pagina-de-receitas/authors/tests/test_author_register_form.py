from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse


class AuthorRegisterFormUnitTest(TestCase): 
    @parameterized.expand([
        ('first_name', 'Ex.: Orlando'),
        ('last_name', 'Ex.: Almeida'),
        ('username', 'Digite seu usuário'),
        ('email', 'Digite seu e-mail'),
        ('password', 'Digite sua senha'),
        ('password2', 'Digite novamente sua senha'),
    ])
    
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
        
    @parameterized.expand([
        ('username', 'Escolha um nome de usuário único.'),
        ('email', 'Informe um e-mail válido para contato.'),
        ('password', 'Use pelo menos 8 caracteres, com letra maiúscula, minúscula e número.'),
    ])
    
    def test_fields_help_text(self, field, help_text):
        form = RegisterForm()
        current_help_text = form[field].help_text
        self.assertEqual(current_help_text, help_text)
        
    @parameterized.expand([
        ('first_name', 'Primeiro nome'),
        ('last_name', 'Último nome'),
        ('username', 'Usuário'),
        ('email', 'E-mail'),
        ('password', 'Senha'),
        ('password2', 'Confirme sua senha'),
    ])
    
    def test_fields_label(self, field, label):
        form = RegisterForm()
        current_label = form[field].label
        self.assertEqual(current_label, label)
        
        
class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': 'Str0ngP@ssword1',
            'password2': 'Str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('first_name', 'Digite seu primeiro nome antes de enviar.'),
        ('last_name', 'Digite seu último nome antes de enviar.'),
        ('username', 'Digite seu usuário antes de enviar.'),
        ('email', 'Digite seu e-mail antes de enviar.'),
        ('password', 'Digite sua senha antes de enviar.'),
        ('password2', 'Confirme sua senha antes de enviar.'),
    ])

    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))


    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = 'abc'
        url = reverse('authors:register_create')
        msg = 'O nome de usuário deve ter no minimo 4 caracteres.'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))


    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = 'A' * 151
        url = reverse('authors:register_create')
        msg = 'O nome de usuário deve ter no máximo 150 caracteres.'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))


    def test_password_field_have_lower_upper_case_letters_and_numbers_invalid(self):
        self.form_data['password'] = 'abc12'
        url = reverse('authors:register_create')
        msg = (
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. Deve ter no mínimo 8 caracteres.'
        )
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('password'))
        
    def test_password_field_have_lower_upper_case_letters_and_numbers_valid(self):
        self.form_data['password'] = '577643121Aa.'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertNotIn(
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. Deve ter no mínimo 8 caracteres.',
            response.context['form'].errors.get('password', [])
        )
        
    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '577643121Aa.'
        self.form_data['password2'] = '577643121Aa.2'
        url = reverse('authors:register_create')
        msg = 'As senhas informadas não coincidem.'
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.context['form'].errors.get('password2', []))
        
    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('authors:register_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_email_field_must_be_unique(self):
        url = reverse('authors:register_create')
        msg = 'User e-mail is already is use'
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg,response.context['form'].errors.get('email'))
        self.assertIn(msg, response.content.decode('utf-8'))
        
    def test_author_create_can_login(self):
        url = reverse('authors:register_create')
        self.form_data.update({
            'username': 'testuser',
            'email': 'email1@gmail.com',
            'password': '577643121Aa.',
            'password2': '577643121Aa.'
        })
        self.client.post(url, data=self.form_data, follow=True)
        is_authenticated = self.client.login(
            username=self.form_data['username'],
            password=self.form_data['password'],
        )
        self.assertTrue(is_authenticated)