from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val
    add_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    # Para sobrescrever digite o mesmo nome do input e colcoa o que quiser já dentro dos parenteses
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu usuário')
        add_placeholder(self.fields['email'], 'digite seu e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Orlando')
        add_placeholder(self.fields['last_name'], 'Ex.: Almeida')

    
    Senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite novamente sua senha'
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
        
        # labels = {'username': 'Digite seu usuário'} aparece em cima
        labels = {
            # CAmpo que aparece em cima do label(caixa)
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        
        # Texto de apoio aparece a baixo 
        help_texts = {
            'email': 'Digite um email valido.',
        }
        
        # Mensagem de erro
        error_messages = {
            # Mensagem de campo obrigatório
            'username': {
                'required': 'Digite seu usuário antes de enviar',
            }
        }
        
        # Adiciona classe
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Digite seu primeiro nome', 'class' : 'classe-widget' }),
            'last_name': forms.TextInput(attrs={'placeholder': 'Digite seu último nome', 'class' : 'classe-widget' }),
            
            'password': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
        }
        
        # exclude = ['email'] aparecerá todos menos esse
    