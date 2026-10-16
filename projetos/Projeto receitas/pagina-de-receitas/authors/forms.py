from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re


# Adiciona atributos ao campo sem apagar os existentes
def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


# Define o texto de exemplo dentro do campo
def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


# Validação de senha forte com expressão regular
def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'A senha deve conter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. Deve ter no mínimo 8 caracteres.',
            code='invalid'
        )


class RegisterForm(forms.ModelForm):

    # Campo de primeiro nome
    first_name = forms.CharField(
        required=True,
        label='Primeiro nome',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Orlando',
            'class': 'classe-widget',
        })
    )

    # Campo de último nome
    last_name = forms.CharField(
        required=True,
        label='Último nome',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Almeida',
            'class': 'classe-widget',
        })
    )

    # Campo de nome de usuário
    username = forms.CharField(
        required=True,
        label='Usuário',
        help_text='Escolha um nome de usuário único.',
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário',
        }),
        error_messages={
            'required': 'Digite seu usuário antes de enviar.',
        }
    )

    # Campo de e-mail
    email = forms.EmailField(
        required=True,
        label='E-mail',
        help_text='Informe um e-mail válido para contato.',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu e-mail',
        })
    )

    # Campo de senha
    password = forms.CharField(
        required=True,
        label='Senha',
        help_text='Use pelo menos 8 caracteres, com letra maiúscula, minúscula e número.',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
        }),
        validators=[strong_password]
    )

    # Campo para confirmar a senha
    password2 = forms.CharField(
        required=True,
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite novamente sua senha',
        })
    )

    class Meta:
        model = User

        # Define os campos do modelo utilizados no formulário
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    # Validação individual do campo senha
    def clean_password(self):
        data = self.cleaned_data.get('password')    

        if data and 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo senha.',
                code='invalid',
                params={'pipoca': '"atenção"'},
            )

        return data

    # Validação individual do primeiro nome
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if data and 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo primeiro nome.',
                code='invalid',
                params={'value': '"John Doe"'},
            )

        return data

    # Validação conjunta para comparar as duas senhas
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error(
                'password2',
                'As senhas devem ser iguais.'
            )

        return cleaned_data

    # Salva o usuário com a senha protegida por hash
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user