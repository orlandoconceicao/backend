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