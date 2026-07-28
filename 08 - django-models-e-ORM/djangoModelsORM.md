# Programação Orientada a Objetos, Models, QuerySets e Recursos do Django

## Introdução

Ao desenvolver aplicações Django, é importante entender como o framework utiliza **Programação Orientada a Objetos (POO)** para representar dados através de Models.

Os Models permitem:

- Representar dados da aplicação através de classes Python.
- Criar tabelas no banco de dados.
- Definir atributos e tipos de dados.
- Realizar consultas utilizando QuerySets.
- Criar, atualizar e excluir registros.
- Integrar os dados com o Django Admin.
- Utilizar os dados reais do banco nas Views.
- Filtrar registros.
- Trabalhar com relacionamentos.
- Criar páginas de listagem e detalhes.
- Tratar páginas inexistentes com respostas 404.
- Utilizar atalhos como `get_list_or_404()` e `get_object_or_404()`.

---

# Programação Orientada a Objetos (POO)

A **Programação Orientada a Objetos (POO)** é um paradigma de programação baseado na utilização de **objetos**.

Em Python, os objetos são criados a partir de **classes**.

Exemplo:

```python
class Recipe:
    pass

Podemos criar um objeto:

recipe = Recipe()

Nesse caso:

Classe
  │
  ▼
Recipe
  │
  ▼
Objeto
  │
  ▼
recipe
Classes

Uma classe funciona como um modelo para criação de objetos.

Exemplo:

class Person:
    name = "Orlando"
    age = 20

Podemos criar um objeto:

person = Person()

E acessar seus atributos:

print(person.name)
print(person.age)
Atributos

Atributos representam características de um objeto.

Exemplo:

class Recipe:
    title = "Lasanha"
    description = "Uma receita de lasanha"

Nesse caso:

title
description

são atributos.

Métodos

Métodos são funções definidas dentro de uma classe.

Exemplo:

class Recipe:

    def show_title(self):
        return "Lasanha"

Utilização:

recipe = Recipe()

print(recipe.show_title())
POO no Django

O Django utiliza POO em diversas partes do framework.

Um exemplo importante são os Models.

Um Model Django é uma classe Python que representa uma estrutura de dados.

Exemplo:

from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)

Aqui:

class Recipe(models.Model):

define uma classe chamada Recipe.

Essa classe herda de:

models.Model

Portanto, Recipe é um Model Django.

Django Models

Um Model é uma representação Python dos dados que serão armazenados no banco de dados.

Exemplo:

from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

O Django utiliza essa classe para construir a estrutura correspondente no banco de dados.

Podemos pensar:

Classe Python
      │
      ▼
Django Model
      │
      ▼
Migração
      │
      ▼
Banco de Dados
Criando o primeiro Model

No arquivo:

recipes/models.py

Podemos criar:

from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
Campos do Model

Cada atributo definido dentro do Model normalmente representa um campo da tabela.

Exemplo:

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

Temos:

Recipe
│
├── title
└── description
CharField

O CharField é utilizado para armazenar textos curtos.

Exemplo:

title = models.CharField(max_length=200)

O parâmetro:

max_length=200

define o tamanho máximo do campo.

TextField

O TextField é utilizado para textos maiores.

Exemplo:

description = models.TextField()

É adequado para campos como:

Descrição.
Ingredientes.
Modo de preparo.
Observações.
Outros campos comuns

Alguns campos frequentemente utilizados:

models.CharField()
models.TextField()
models.IntegerField()
models.BooleanField()
models.DateField()
models.DateTimeField()
models.EmailField()
models.ImageField()
models.ForeignKey()

Exemplo:

class Recipe(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    preparation_time = models.IntegerField()

    is_published = models.BooleanField(default=False)
Criando um Model mais completo

Um Model de receitas pode possuir:

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparation_time = models.IntegerField()
    is_published = models.BooleanField(default=False)
Migrações do Django

Depois de criar ou alterar um Model, precisamos informar ao Django que a estrutura do banco de dados mudou.

Para isso existem as migrações.

As principais etapas são:

Model
  │
  ▼
makemigrations
  │
  ▼
Arquivo de migração
  │
  ▼
migrate
  │
  ▼
Banco de dados
makemigrations

O comando:

python manage.py makemigrations

analisa as alterações feitas nos Models e cria arquivos de migração.

Exemplo:

python manage.py makemigrations

O Django poderá informar algo semelhante a:

Migrations for 'recipes':
  recipes/migrations/0001_initial.py
migrate

Depois de criar a migração, executamos:

python manage.py migrate

Esse comando aplica as migrações no banco de dados.

Diferença entre makemigrations e migrate
makemigrations

Cria o plano de alteração do banco.

python manage.py makemigrations
migrate

Aplica as alterações no banco.

python manage.py migrate

Fluxo:

Alteração no Model
       │
       ▼
makemigrations
       │
       ▼
Migration
       │
       ▼
migrate
       │
       ▼
Banco de dados atualizado
Recomendação: Django Model Field Reference

A documentação oficial do Django possui uma referência completa sobre os campos disponíveis nos Models.

É importante consultar a documentação quando houver dúvidas sobre:

Tipos de campos.
Opções dos campos.
Valores padrão.
Relacionamentos.
Validações.
Comportamentos específicos.
Registrando Category no Django Admin

O Django possui uma área administrativa chamada Django Admin.

Para disponibilizar um Model no Admin, podemos registrá-lo no arquivo:

recipes/admin.py

Exemplo:

from django.contrib import admin

from .models import Category


admin.site.register(Category)

Depois de registrar, o Model poderá aparecer no painel administrativo.

Registrando Recipe no Django Admin

Também podemos registrar Recipe.

from django.contrib import admin

from .models import Category, Recipe


admin.site.register(Category)
admin.site.register(Recipe)

Agora os dois Models podem ser manipulados pelo Django Admin.

Criando um Superusuário

Para acessar o Django Admin, normalmente criamos um superusuário.

Comando:

python manage.py createsuperuser

O Django solicitará informações como:

Username
Email
Password

Depois podemos iniciar o servidor:

python manage.py runserver

E acessar:

/admin/
Django Shell

O Django Shell permite executar código Python utilizando o ambiente do projeto Django.

Para abrir:

python manage.py shell

Depois podemos importar os Models:

from recipes.models import Recipe
Criando registros pelo Django Shell

Podemos criar uma receita:

recipe = Recipe.objects.create(
    title="Lasanha",
    description="Receita de lasanha",
)

O Django cria o registro no banco.

Consultando registros

Podemos utilizar:

Recipe.objects.all()

Esse comando retorna todos os registros de Recipe.

QuerySet

Um QuerySet representa uma coleção de objetos obtidos através de uma consulta ao banco de dados.

Exemplo:

recipes = Recipe.objects.all()

Podemos visualizar:

Banco de dados
      │
      ▼
QuerySet
      │
      ├── Recipe
      ├── Recipe
      ├── Recipe
      └── Recipe
objects

O atributo:

Recipe.objects

é o Manager utilizado para realizar consultas no Model.

Exemplos:

Recipe.objects.all()
Recipe.objects.filter(...)
Recipe.objects.get(...)
Recipe.objects.create(...)
QuerySet com all()

Para buscar todos os registros:

Recipe.objects.all()

Exemplo:

recipes = Recipe.objects.all()
Percorrendo um QuerySet

Podemos utilizar um for:

recipes = Recipe.objects.all()

for recipe in recipes:
    print(recipe.title)
filter()

O método filter() permite filtrar registros.

Exemplo:

Recipe.objects.filter(
    is_published=True
)

Nesse caso, serão retornadas somente as receitas publicadas.

Filtrando por título
Recipe.objects.filter(
    title="Lasanha"
)
Múltiplos filtros

Podemos utilizar vários filtros:

Recipe.objects.filter(
    is_published=True,
    preparation_time__lte=60,
)

Nesse exemplo, buscamos receitas:

publicadas
E
com tempo de preparo menor ou igual a 60 minutos
get()

O método get() busca um único objeto.

Exemplo:

recipe = Recipe.objects.get(id=1)

Se o objeto existir, teremos uma instância de Recipe.

Atenção ao get()

O get() deve ser utilizado quando esperamos encontrar exatamente um objeto.

Se nenhum objeto existir, o Django poderá gerar:

Recipe.DoesNotExist

Se mais de um objeto corresponder à consulta, poderá ocorrer:

Recipe.MultipleObjectsReturned
Criando uma receita com save()

Também podemos criar objetos manualmente:

recipe = Recipe(
    title="Pizza",
    description="Pizza caseira",
)

recipe.save()
Atualizando um objeto

Podemos buscar um objeto:

recipe = Recipe.objects.get(id=1)

Alterar um atributo:

recipe.title = "Pizza de queijo"

E salvar:

recipe.save()
Excluindo um objeto

Podemos excluir um registro:

recipe = Recipe.objects.get(id=1)

recipe.delete()
QuerySet e Lazy Evaluation

QuerySets utilizam um comportamento conhecido como lazy evaluation.

Isso significa que a consulta ao banco normalmente não é executada imediatamente quando o QuerySet é criado.

Exemplo:

recipes = Recipe.objects.filter(
    is_published=True
)

A consulta poderá ser executada quando os dados realmente forem necessários.

QuerySet API Reference

A documentação oficial do Django possui uma referência completa sobre QuerySets.

É importante conhecer métodos como:

all()
filter()
exclude()
get()
first()
last()
exists()
count()
order_by()
Utilizando o Model real na View Home

Antes de trabalhar com o banco de dados, uma View pode utilizar dados fixos:

def home(request):

    recipes = [
        "Lasanha",
        "Pizza",
        "Hambúrguer",
    ]

    return render(
        request,
        "recipes/home.html",
        {
            "recipes": recipes,
        },
    )

Com Models, podemos buscar os dados diretamente do banco.

Buscando receitas na View
from django.shortcuts import render

from .models import Recipe


def home(request):

    recipes = Recipe.objects.all()

    return render(
        request,
        "recipes/home.html",
        {
            "recipes": recipes,
        },
    )

Agora a página utiliza dados reais do banco.

Exibindo receitas no Template

No template:

{% for recipe in recipes %}

<h2>{{ recipe.title }}</h2>

<p>
    {{ recipe.description }}
</p>

{% endfor %}

O Django percorre o QuerySet e exibe cada receita.

Fluxo do Model até o HTML
Banco de Dados
      │
      ▼
Recipe.objects.all()
      │
      ▼
QuerySet
      │
      ▼
View
      │
      ▼
Context
      │
      ▼
Template
      │
      ▼
HTML
Ocultando receitas não publicadas

Imagine que o Model tenha:

is_published = models.BooleanField(default=False)

Nem todas as receitas devem aparecer na página pública.

Podemos filtrar:

recipes = Recipe.objects.filter(
    is_published=True
)

View completa:

def home(request):

    recipes = Recipe.objects.filter(
        is_published=True
    )

    return render(
        request,
        "recipes/home.html",
        {
            "recipes": recipes,
        },
    )
Por que usar is_published?

O campo:

is_published

permite controlar a publicação das receitas.

Exemplo:

Lasanha       → True
Pizza         → True
Hambúrguer    → False

Na página pública:

Recipe.objects.filter(
    is_published=True
)

Somente:

Lasanha
Pizza

serão exibidas.

blank=True

O parâmetro:

blank=True

indica que o campo pode ficar vazio em formulários e validações do Django.

Exemplo:

category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    blank=True,
)
null=True

O parâmetro:

null=True

permite que o banco armazene NULL.

Exemplo:

category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
)
blank=True e null=True

É comum encontrar os dois juntos quando um campo pode não possuir valor:

category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
)

Diferença simplificada:

blank=True
    │
    └── relacionado à validação/formulários

null=True
    │
    └── relacionado ao banco de dados
default=None

Também podemos utilizar:

default=None

Exemplo:

category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    default=None,
)

Isso define None como valor padrão para o campo.

Corrigindo Category

Um campo de categoria opcional pode ser definido assim:

category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    default=None,
)

Depois de alterar o Model, devemos verificar as migrações:

python manage.py makemigrations

E aplicar:

python manage.py migrate
Autor da Receita

Uma receita também pode possuir um autor.

Podemos utilizar um relacionamento com o usuário do Django.

Exemplo:

from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
on_delete

Quando utilizamos ForeignKey, precisamos definir o comportamento quando o objeto relacionado for excluído.

Exemplo:

on_delete=models.SET_NULL

Nesse caso, se o usuário for excluído, o autor da receita poderá ficar como NULL.

Por isso o campo precisa permitir:

null=True
User Model

O Django possui um sistema de autenticação integrado.

Um dos Models principais é:

User

Ele pode representar usuários da aplicação.

Exemplo:

from django.contrib.auth.models import User
Relacionamento Recipe e User

Podemos visualizar:

User
 │
 │ 1
 │
 │
 │ N
 ▼
Recipe

Um usuário pode ser autor de várias receitas.

Exibindo o autor

No template:

{% for recipe in recipes %}

<h2>{{ recipe.title }}</h2>

<p>
    Autor: {{ recipe.author }}
</p>

{% endfor %}
Erro 404 Not Found

Quando uma página ou objeto não existe, devemos retornar uma resposta HTTP:

404 Not Found

Exemplo de URL:

/recipes/999999/

Se a receita não existir, não devemos mostrar uma página de receita vazia ou gerar um erro interno.

O comportamento esperado é:

404 Not Found
Verificando manualmente se um objeto existe

Podemos fazer uma consulta:

def recipe(request, recipe_id):

    recipe = Recipe.objects.filter(
        id=recipe_id
    ).first()

    if recipe is None:
        raise Http404()

    return render(
        request,
        "recipes/detail.html",
        {
            "recipe": recipe,
        },
    )

Porém, o Django oferece atalhos para simplificar esse código.

get_list_or_404()

O get_list_or_404() é um atalho para buscar uma lista de objetos.

Exemplo:

from django.shortcuts import get_list_or_404


recipes = get_list_or_404(
    Recipe,
    is_published=True,
)

Se existirem registros:

QuerySet / lista de objetos

Se nenhum registro for encontrado:

404 Not Found
Exemplo com get_list_or_404()
from django.shortcuts import get_list_or_404
from django.shortcuts import render

from .models import Recipe


def home(request):

    recipes = get_list_or_404(
        Recipe,
        is_published=True,
    )

    return render(
        request,
        "recipes/home.html",
        {
            "recipes": recipes,
        },
    )
Página de detalhes da receita

Uma página de detalhes normalmente recebe o ID da receita pela URL.

URL:

path(
    "recipes/<int:recipe_id>/",
    views.recipe,
    name="recipe",
)

Exemplos:

recipes/1/
recipes/2/
recipes/3/
View de detalhes

Podemos criar:

def recipe(request, recipe_id):

    recipe = Recipe.objects.get(
        id=recipe_id
    )

    return render(
        request,
        "recipes/detail.html",
        {
            "recipe": recipe,
        },
    )

Porém, existe uma forma mais segura e prática.

get_object_or_404()

O Django fornece:

get_object_or_404()

Ele tenta buscar um único objeto.

Se encontrar:

Objeto

Se não encontrar:

404 Not Found
Utilizando get_object_or_404()
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Recipe


def recipe(request, recipe_id):

    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
    )

    return render(
        request,
        "recipes/detail.html",
        {
            "recipe": recipe,
        },
    )
Comparação: get() x get_object_or_404()

Com get():

recipe = Recipe.objects.get(
    id=recipe_id
)

É necessário tratar o caso em que o objeto não existe.

Com get_object_or_404():

recipe = get_object_or_404(
    Recipe,
    id=recipe_id,
)

O Django automaticamente retorna:

404 Not Found

quando o objeto não é encontrado.

Detail Page

O template de detalhes pode ser:

templates/
└── recipes/
    └── detail.html

Exemplo:

{% extends 'recipes/base.html' %}

{% block title %}
{{ recipe.title }}
{% endblock %}

{% block content %}

<h1>{{ recipe.title }}</h1>

<p>
    {{ recipe.description }}
</p>

{% endblock %}
Exibindo informações da receita

Podemos adicionar:

<h1>{{ recipe.title }}</h1>

<p>
    Autor: {{ recipe.author }}
</p>

<p>
    Tempo de preparo:
    {{ recipe.preparation_time }} minutos
</p>

<p>
    {{ recipe.description }}
</p>
Exibindo o modo de preparo

Caso exista um campo:

preparation = models.TextField()

Podemos exibir:

<h2>Modo de preparo</h2>

<p>
    {{ recipe.preparation }}
</p>
Quebra de linha no modo de preparo

Como o conteúdo pode possuir várias linhas, podemos utilizar:

{{ recipe.preparation|linebreaks }}

Exemplo:

<div class="recipe-preparation">

    {{ recipe.preparation|linebreaks }}

</div>

O filtro linebreaks transforma quebras de linha do texto em elementos HTML apropriados.

Ajustando CSS do modo de preparo

Podemos criar uma classe:

<div class="recipe-preparation">

    {{ recipe.preparation|linebreaks }}

</div>

CSS:

.recipe-preparation {
    line-height: 1.7;
    white-space: normal;
}

Isso ajuda a melhorar a leitura do conteúdo.

get_object_or_404 na prática

Uma View de detalhes recomendada:

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Recipe


def recipe(request, recipe_id):

    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        is_published=True,
    )

    return render(
        request,
        "recipes/detail.html",
        {
            "recipe": recipe,
        },
    )

Assim, receitas não publicadas também não serão acessíveis pela página pública.

get_list_or_404 na Home: usar ou não?

Podemos utilizar:

recipes = get_list_or_404(
    Recipe,
    is_published=True,
)

Porém, é importante entender o comportamento.

Se não houver nenhuma receita publicada, o Django retornará:

404 Not Found

Isso pode não ser o comportamento desejado para uma página inicial.

QuerySet vazio

Com:

recipes = Recipe.objects.filter(
    is_published=True
)

se não existirem receitas publicadas, teremos um QuerySet vazio:

<QuerySet []>

A Home ainda poderá ser exibida normalmente.

Quando usar filter()

Para uma página de listagem, normalmente podemos preferir:

recipes = Recipe.objects.filter(
    is_published=True
)

Isso permite mostrar uma página vazia com uma mensagem:

{% if recipes %}

    {% for recipe in recipes %}

        <h2>{{ recipe.title }}</h2>

    {% endfor %}

{% else %}

    <p>Nenhuma receita encontrada.</p>

{% endif %}
Quando usar get_list_or_404()

get_list_or_404() pode ser útil quando a ausência de resultados deve representar uma página inexistente.

Exemplo:

recipes = get_list_or_404(
    Recipe,
    category=category,
)

Se a categoria solicitada não possuir receitas, podemos decidir que a resposta apropriada é:

404 Not Found
Resumo: filter x get_list_or_404
filter()
Recipe.objects.filter(...)

Pode retornar:

Objetos

ou:

QuerySet vazio
get_list_or_404()
get_list_or_404(Recipe, ...)

Pode retornar:

Objetos

ou:

404 Not Found
Publicando novamente as receitas

Caso as receitas estejam com:

is_published=False

podemos alterar pelo Django Admin.

Também podemos utilizar o Django Shell.

Abrir:

python manage.py shell

Importar:

from recipes.models import Recipe

Buscar as receitas:

recipes = Recipe.objects.all()
Atualizando is_published

Podemos percorrer os objetos:

for recipe in recipes:
    recipe.is_published = True
    recipe.save()

Agora as receitas estarão publicadas.

Atualização utilizando update()

Também podemos utilizar:

Recipe.objects.all().update(
    is_published=True
)

Esse comando atualiza diretamente os registros correspondentes.

Cuidado com update()

O comando:

Recipe.objects.all().update(
    is_published=True
)

altera todos os registros.

Portanto, deve ser utilizado somente quando essa for realmente a intenção.

Renomeando um projeto Django inteiro

Renomear um projeto Django exige atenção porque o nome do projeto pode aparecer em vários lugares.

Exemplo de projeto:

old_project/

Pode ser necessário renomear para:

new_project/
Locais que podem precisar de alteração

Ao renomear um projeto Django, procure referências ao nome antigo em arquivos como:

manage.py
settings.py
urls.py
wsgi.py
asgi.py

Também é importante verificar imports:

from old_project.settings import ...

ou:

old_project.urls
Exemplo de estrutura

Antes:

project/
│
├── manage.py
│
└── project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

Depois:

new_project/
│
├── manage.py
│
└── new_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
Atenção ao renomear

Antes de executar o projeto novamente, procure referências ao nome antigo.

No VS Code:

Ctrl + Shift + F

Pesquise pelo nome antigo do projeto.

Depois atualize todas as referências necessárias.

Internacionalização no Django

O Django possui recursos para:

Tradução.
Internacionalização.
Localização.
Formatação de datas.
Formatação de números.
Time Zones.

Esses recursos permitem adaptar a aplicação para diferentes idiomas e regiões.

LANGUAGE_CODE

No arquivo:

settings.py

podemos configurar:

LANGUAGE_CODE = "pt-br"

Isso indica o idioma padrão da aplicação.

Time Zone

Também podemos configurar:

TIME_ZONE = "America/Sao_Paulo"

Isso define o fuso horário utilizado pela aplicação.

USE_I18N

A configuração:

USE_I18N = True

habilita os recursos de internacionalização do Django.

USE_TZ

A configuração:

USE_TZ = True

habilita o suporte a time zones.

Exemplo:

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True
Tradução

O Django possui ferramentas para tradução de textos.

Uma aplicação pode ter:

Português
Inglês
Espanhol
Francês

Por exemplo:

from django.utils.translation import gettext_lazy as _

Podemos marcar um texto para tradução:

title = _("Receitas")
Tradução em Templates

No template, podemos utilizar:

{% load i18n %}

E marcar textos:

{% translate "Receitas" %}

Exemplo:

{% load i18n %}

<h1>
    {% translate "Receitas" %}
</h1>
Internacionalização x Localização
Internacionalização

Preparar a aplicação para trabalhar com diferentes idiomas e regiões.

i18n
Localização

Adaptar a aplicação para uma região específica.

l10n

Exemplo:

Idioma:
Português

Região:
Brasil

Fuso horário:
America/Sao_Paulo
Estrutura final do projeto

Uma estrutura possível:

meu_projeto/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── recipes/
    │
    ├── migrations/
    │
    ├── templates/
    │   └── recipes/
    │       ├── base.html
    │       ├── home.html
    │       └── detail.html
    │
    ├── admin.py
    ├── models.py
    ├── urls.py
    └── views.py
Fluxo completo da aplicação
Usuário
    │
    ▼
URL
    │
    ▼
View
    │
    ▼
QuerySet
    │
    ▼
Model
    │
    ▼
Banco de Dados
    │
    ▼
Objeto / QuerySet
    │
    ▼
Context
    │
    ▼
Template
    │
    ▼
HTML
    │
    ▼
Navegador
Fluxo de uma página de lista
GET /recipes/
       │
       ▼
urls.py
       │
       ▼
home()
       │
       ▼
Recipe.objects.filter(
    is_published=True
)
       │
       ▼
QuerySet
       │
       ▼
context
       │
       ▼
home.html
       │
       ▼
Lista de receitas
Fluxo de uma página de detalhes
GET /recipes/1/
       │
       ▼
urls.py
       │
       ▼
recipe(request, recipe_id)
       │
       ▼
get_object_or_404()
       │
       ▼
Recipe
       │
       ▼
context
       │
       ▼
detail.html
       │
       ▼
Receita
Exemplo completo de Model
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    preparation = models.TextField()

    preparation_time = models.IntegerField()

    is_published = models.BooleanField(
        default=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
Exemplo completo de View Home
from django.shortcuts import render

from .models import Recipe


def home(request):

    recipes = Recipe.objects.filter(
        is_published=True,
    )

    context = {
        "recipes": recipes,
    }

    return render(
        request,
        "recipes/home.html",
        context,
    )
Exemplo completo de View Detail
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Recipe


def recipe(request, recipe_id):

    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        is_published=True,
    )

    context = {
        "recipe": recipe,
    }

    return render(
        request,
        "recipes/detail.html",
        context,
    )
Exemplo completo de URLs
from django.urls import path

from . import views


app_name = "recipes"


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "recipes/<int:recipe_id>/",
        views.recipe,
        name="recipe",
    ),
]
Exemplo de Home Template
{% extends "recipes/base.html" %}

{% block title %}
Receitas
{% endblock %}

{% block content %}

<h1>Receitas</h1>

{% if recipes %}

    {% for recipe in recipes %}

        <article>

            <h2>
                <a href="{% url 'recipes:recipe' recipe.id %}">
                    {{ recipe.title }}
                </a>
            </h2>

            <p>
                {{ recipe.description }}
            </p>

            <p>
                Autor: {{ recipe.author }}
            </p>

        </article>

    {% endfor %}

{% else %}

    <p>Nenhuma receita publicada.</p>

{% endif %}

{% endblock %}
Exemplo de Detail Template
{% extends "recipes/base.html" %}

{% block title %}
{{ recipe.title }}
{% endblock %}

{% block content %}

<article>

    <h1>
        {{ recipe.title }}
    </h1>

    <p>
        Autor: {{ recipe.author }}
    </p>

    <p>
        Tempo de preparo:
        {{ recipe.preparation_time }} minutos
    </p>

    <h2>Descrição</h2>

    <p>
        {{ recipe.description }}
    </p>

    <h2>Modo de preparo</h2>

    <div class="recipe-preparation">
        {{ recipe.preparation|linebreaks }}
    </div>

</article>

{% endblock %}
Boas práticas
Utilize Models para representar os dados da aplicação.
Crie Models com nomes claros e objetivos.
Escolha corretamente os tipos dos campos.
Utilize makemigrations depois de alterar Models.
Utilize migrate para aplicar as migrações.
Utilize o Django Admin para facilitar a manipulação dos dados.
Utilize o Django Shell para testar consultas.
Conheça a API de QuerySets.
Utilize filter() para consultas que podem retornar vários objetos.
Utilize get() quando espera exatamente um objeto e sabe como tratar exceções.
Utilize get_object_or_404() em páginas que precisam retornar 404 quando um objeto não existe.
Utilize get_list_or_404() somente quando a ausência de resultados realmente representar um 404.
Utilize blank=True quando um campo puder ficar vazio em formulários/validações.
Utilize null=True quando o banco puder armazenar NULL.
Utilize default=None quando None for o valor padrão desejado.
Utilize relacionamentos como ForeignKey para conectar Models.
Filtre receitas públicas utilizando is_published=True.
Não exponha dados que deveriam permanecer privados.
Organize Templates, Views, Models e URLs por responsabilidade.
Mantenha configurações de idioma e fuso horário coerentes com o projeto.
Consulte a documentação oficial do Django quando houver dúvidas sobre Models e QuerySets.
Conceitos importantes
Model

Representa os dados da aplicação.

class Recipe(models.Model):
    ...
Field

Representa um campo do Model.

title = models.CharField(max_length=200)
Migration

Representa alterações na estrutura do banco.

python manage.py makemigrations
python manage.py migrate
QuerySet

Representa o resultado de uma consulta.

Recipe.objects.all()
Manager

É utilizado para realizar consultas.

Recipe.objects
filter()

Filtra registros.

Recipe.objects.filter(
    is_published=True
)
get_object_or_404()

Busca um objeto e retorna 404 se não existir.

get_object_or_404(
    Recipe,
    id=recipe_id,
)
get_list_or_404()

Busca uma lista e retorna 404 se nenhum registro for encontrado.

get_list_or_404(
    Recipe,
    is_published=True,
)
Resumo

A Programação Orientada a Objetos (POO) é fundamental para compreender como o Django estrutura grande parte de seu funcionamento. Os Models são classes Python que representam dados da aplicação e seus campos representam informações que serão armazenadas no banco de dados.

Depois de criar ou modificar um Model, utilizamos:

python manage.py makemigrations

para criar as migrações e:

python manage.py migrate

para aplicar essas alterações ao banco.

O Django Admin permite manipular os registros de forma visual, enquanto o Django Shell permite testar e manipular Models diretamente através do Python.

As consultas são realizadas principalmente através do Manager:

Recipe.objects

e de métodos da API de QuerySets:

all()
filter()
get()
exclude()
first()
last()
exists()
count()
order_by()

Para uma página pública de receitas, podemos buscar somente os registros publicados:

Recipe.objects.filter(
    is_published=True
)

Quando trabalhamos com objetos que podem não existir, o Django oferece atalhos importantes:

get_object_or_404()
get_list_or_404()

O get_object_or_404() é especialmente útil em páginas de detalhes, pois permite buscar uma receita e retornar automaticamente 404 Not Found caso ela não exista.

Relacionamentos também são importantes. Um Recipe pode possuir uma categoria e um autor através de ForeignKey, permitindo representar relações entre tabelas:

User
  │
  └── várias Recipes

Category
  │
  └── várias Recipes

Também é importante compreender a diferença entre:

blank=True

e:

null=True

blank=True está relacionado principalmente à validação e aos formulários, enquanto null=True permite que o banco armazene NULL.

Por fim, o Django oferece recursos de internacionalização, tradução e gerenciamento de fusos horários. Uma aplicação direcionada ao Brasil pode utilizar, por exemplo:

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

Esses conceitos formam uma base importante para evoluir de uma aplicação Django que utiliza dados estáticos para uma aplicação realmente conectada ao banco de dados, capaz de criar, consultar, filtrar, atualizar e exibir informações dinamicamente.