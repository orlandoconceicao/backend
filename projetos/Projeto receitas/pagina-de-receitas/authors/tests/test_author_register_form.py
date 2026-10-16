from django.test import TestCase

from authors.forms import RegisterForm

from parameterized import parameterized

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
        ('username', 'Escolha um nome de usuário único para acessar sua conta.'),
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
        