from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
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
    