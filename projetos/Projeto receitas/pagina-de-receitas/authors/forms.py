from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):

    # Campo de primeiro nome
    first_name = forms.CharField(
        required=True,
        label='Primeiro nome',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Orlando',
            'class': 'classe-widget',
        }),
        error_messages={
            'required': 'Digite seu primeiro nome antes de enviar.',
        }
    )

    # Campo de último nome
    last_name = forms.CharField(
        required=True,
        label='Último nome',
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Almeida',
            'class': 'classe-widget',
        }),
        error_messages={
            'required': 'Digite seu sobrenome antes de enviar.',
        }
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
            'unique': 'Este nome de usuário já está em uso.',
            'min_length': 'O nome de usuário deve ter no minimo 4 caracteres.',
            'max_length': 'O nome de usuário deve ter no máximo 150 caracteres.',
        },
        min_length=4,
        max_length=150,
    )

    # Campo de e-mail
    email = forms.EmailField(
        required=True,
        label='E-mail',
        help_text='Informe um e-mail válido para contato.',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu e-mail',
        }),
        error_messages={
            'required': 'Digite seu e-mail antes de enviar.',
            'invalid': 'Digite um endereço de e-mail válido.',
        }
    )

    # Campo de senha
    password = forms.CharField(
        required=True,
        label='Senha',
        help_text='Use pelo menos 8 caracteres, com letra maiúscula, minúscula e número.',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
        }),
        validators=[strong_password],
        error_messages={
            'required': 'Digite sua senha antes de enviar.',
        }
    )

    # Campo para confirmar a senha
    password2 = forms.CharField(
        required=True,
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite novamente sua senha',
        }),
        error_messages={
            'required': 'Confirme sua senha antes de enviar.',
        }
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

    # Tornar o email unico
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email=email).exists():
            raise ValidationError('User e-mail is already is use',code='invalid',)

        return email
    
    
    # Validação conjunta para comparar as duas senhas
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error(
                'password2',
                'As senhas informadas não coincidem.'
            )

        return cleaned_data

    # Salva o usuário com a senha protegida por hash
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user