from django import forms
from recipes.models import Recipe
from utils.django_forms import add_attr


class AuthorsRecipeForm(forms.ModelForm):
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

    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', 'preparation_time_unit', \
                'servings', 'servings_unit', 'preparation_steps', 'cover'