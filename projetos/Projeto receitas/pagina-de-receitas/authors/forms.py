from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(
        required=True,
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite novamente sua senha',
        })
    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }

        help_texts = {
            'email': 'Digite um e-mail válido.',
        }

        error_messages = {
            'username': {
                'required': 'Digite seu usuário antes de enviar.',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex.: Orlando',
                'class': 'classe-widget',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ex.: Almeida',
                'class': 'classe-widget',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(
            self.fields['username'],
            'Digite seu usuário'
        )

        add_placeholder(
            self.fields['email'],
            'Digite seu e-mail'
        )

    # clean_field == clean_nome do campo
    def clean_password(self):
        data = self.cleaned_data.get('password')

        if data and 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo senha.',
                code='invalid',
                params={'pipoca': '"atenção"'},
            )

        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if data and 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo primeiro nome.',
                code='invalid',
                params={'value': '"John Doe"'},
            )

        return data

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
