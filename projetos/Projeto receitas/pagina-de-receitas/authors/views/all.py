from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from authors.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create'),
    })


def register_create(request):
    if request.method != 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST.dict()
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Seu cadastro foi criado!')

        request.session.pop('register_form_data', None)
        return redirect('recipes:home')

    return redirect('authors:register')

def login_view(request):
    form = LoginForm
    return render(request,'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })

def login_create(request):
    if request.method != 'POST':
        raise Http404()
    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is None:
            messages.error(request, 'Credenciais inválidas')
            return redirect(login_url)

        login(request, authenticated_user)
        messages.success(request, 'Você está logado.')
        return redirect('authors:dashboard')

    messages.error(request, 'Usuário ou senha incorreto')
    return redirect(login_url)

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Logout invállido')
        return redirect(reverse('authors:login'))
    
    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Usuário de logout inválido')
        return redirect(reverse('authors:login'))
    
    messages.success(request, 'Logout concedido')
    logout(request)
    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'authors/pages/dashboard.html', context={
        'recipes': recipes,
    })
    
@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_delete(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    id = POST.get('id')
        
    recipe = Recipe.objects.filter(
        is_published = False,
        author = request.user,
        pk=id).first()
    
    if not recipe:
        raise Http404()
    
    recipe.delete()
    messages.success(request, 'Receita deletada com sucesso!')
    return redirect(reverse('authors:dashboard'))