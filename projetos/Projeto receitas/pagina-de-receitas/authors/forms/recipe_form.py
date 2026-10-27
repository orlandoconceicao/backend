from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from recipes.models import Recipe
from utils.django_forms import add_attr
from utils.strings import is_positive_number


class AuthorsRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', 'preparation_time_unit', \
                'servings', 'servings_unit', 'preparation_steps', 'cover'

    title = forms.CharField(
        required=True,
        label='Título',
        max_length=65,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o título da receita',
        }),
        error_messages={
            'required': 'Digite o título da receita antes de enviar.',
        },
    )

    description = forms.CharField(
        required=True,
        label='Descrição',
        max_length=165,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite uma descrição para a receita',
        }),
        error_messages={
            'required': 'Digite uma descrição antes de enviar.',
        },
    )

    preparation_time = forms.IntegerField(
        required=True,
        label='Tempo de preparo',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Informe o tempo de preparo',
        }),
        error_messages={
            'required': 'Informe o tempo de preparo antes de enviar.',
            'invalid': 'Informe um número válido para o tempo de preparo.',
        },
    )

    preparation_time_unit = forms.ChoiceField(
        required=True,
        label='Unidade do tempo de preparo',
        choices=(
            ('Minutos', 'Minutos'),
            ('Horas', 'Horas'),
        ),
    )

    servings = forms.IntegerField(
        required=True,
        label='Quantidade',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Informe a quantidade',
        }),
        error_messages={
            'required': 'Informe a quantidade antes de enviar.',
            'invalid': 'Informe um número válido para a quantidade.',
        },
    )

    servings_unit = forms.ChoiceField(
        required=True,
        label='Unidade da quantidade',
        choices=(
            ('Porções', 'Porções'),
            ('Pedaços', 'Pedaços'),
            ('Pessoas', 'Pessoas'),
        ),
    )

    preparation_steps = forms.CharField(
        required=True,
        label='Modo de preparo',
        widget=forms.Textarea(attrs={
            'placeholder': 'Descreva o modo de preparo da receita',
            'class': 'span-2',
        }),
        error_messages={
            'required': 'Descreva o modo de preparo antes de enviar.',
        },
    )

    cover = forms.ImageField(
        required=True,
        label='Imagem de capa',
        widget=forms.FileInput(attrs={
            'class': 'span-2',
        }),
        error_messages={
            'required': 'Selecione uma imagem de capa antes de enviar.',
            'invalid_image': 'Envie um arquivo de imagem válido.',
        },
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ('preparation_steps', 'cover'):
            add_attr(self.fields[field_name], 'class', 'span-2')

# CLEAN

        # Guarda erros personalizados dos clean_<campo> para exibi-los juntos.
        self._my_errors = defaultdict(list)

    def clean(self, *args, **kwargs):
        # Executa primeiro as validações padrão do Django e obtém os valores válidos.
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        # Esta regra compara dois campos, por isso fica na validação geral do formulário.
        if title and description and title.casefold() == description.casefold():
            self._my_errors['title'].append('O título deve ser diferente da descrição.')
            self._my_errors['description'].append('A descrição deve ser diferente do título.')

        # Se algum clean_<campo> ou a comparação acima encontrou erro, informa o Django.
        if self._my_errors:
            raise ValidationError(dict(self._my_errors))
        return super_clean

    def clean_title(self):
        # O Django chama este método para validar especificamente o título.
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._my_errors['title'].append('O título deve conter no mínimo 5 caracteres.')
        return title

    def clean_description(self):
        # A descrição também precisa ter pelo menos 5 caracteres.
        description = self.cleaned_data.get('description')
        if len(description) < 5:
            self._my_errors['description'].append('A descrição deve conter no mínimo 5 caracteres.')
        return description

    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get(field_name)
        # A função compartilhada retorna False para valores que não sejam positivos.
        if not is_positive_number(field_value):
            self._my_errors[field_name].append('O tempo de preparo deve ser um número positivo.')
        return field_value

    def clean_servings(self):
        field_name = 'servings'
        field_value = self.cleaned_data.get(field_name)
        # A quantidade também precisa ser um número maior que zero.
        if not is_positive_number(field_value):
            self._my_errors[field_name].append('A quantidade deve ser um número positivo.')
        return field_value