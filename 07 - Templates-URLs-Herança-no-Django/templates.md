# Templates, URLs e Herança no Django

## Introdução

À medida que uma aplicação Django cresce, torna-se necessário criar novas páginas, organizar os templates e evitar repetição de código.

O Django fornece mecanismos para:

- Criar múltiplas URLs.
- Criar várias Views.
- Separar templates por responsabilidade.
- Reutilizar layouts através da herança de templates.
- Enviar dados das Views para os templates.
- Organizar URLs utilizando namespaces.

---

# Relação entre URL, View e Template

Cada página normalmente é composta por:

- Uma URL
- Uma View
- Um Template

Fluxo de funcionamento:

```text
Usuário
    │
    ▼
URL
    │
    ▼
View
    │
    ▼
Template
    │
    ▼
Resposta HTML
```

---

# Criando uma nova View

No arquivo `views.py`:

```python
from django.shortcuts import render


def home(request):
    return render(request, "recipes/home.html")


def about(request):
    return render(request, "recipes/about.html")
```

Agora existem duas páginas diferentes na aplicação.

---

# Criando novas URLs

No arquivo `urls.py`:

```python
from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

As URLs ficam assim:

```text
/
about/
```

Cada endereço executa uma View diferente.

---

# Organização dos Templates

É recomendado organizar os templates dentro da própria aplicação.

Estrutura:

```text
recipes/

templates/
└── recipes/
    ├── base.html
    ├── home.html
    ├── about.html
    └── detail.html
```

Essa organização evita conflitos entre aplicações diferentes.

---

# O problema da repetição

Imagine duas páginas:

**home.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Receitas</title>
</head>
<body>

<header>
    Menu
</header>

<h1>Página Inicial</h1>

<footer>
    Rodapé
</footer>

</body>
</html>
```

**about.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Receitas</title>
</head>
<body>

<header>
    Menu
</header>

<h1>Sobre</h1>

<footer>
    Rodapé
</footer>

</body>
</html>
```

Grande parte do código HTML está repetida.

Sempre que fosse necessário alterar o menu ou o rodapé, seria preciso modificar todos os arquivos.

---

# Herança de Templates

Para evitar repetição, cria-se um template base.

Arquivo:

```text
base.html
```

Exemplo:

```html
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">

    <title>
        {% block title %}
        Receitas
        {% endblock %}
    </title>
</head>

<body>

<header>
    Menu
</header>

<main>

{% block content %}

{% endblock %}

</main>

<footer>
    Rodapé
</footer>

</body>
</html>
```

O layout fica centralizado em um único arquivo.

---

# A tag `extends`

Os templates filhos reutilizam o template base utilizando:

```django
{% extends 'recipes/base.html' %}
```

Exemplo:

```html
{% extends 'recipes/base.html' %}

{% block content %}

<h1>Página Inicial</h1>

{% endblock %}
```

Outro exemplo:

```html
{% extends 'recipes/base.html' %}

{% block content %}

<h1>Sobre</h1>

{% endblock %}
```

Estrutura:

```text
base.html
        ▲
        │
 ┌──────┴──────┐
 │             │
home.html   about.html
```

---

# Template Blocks

Os blocos representam partes substituíveis do template.

Exemplo:

```django
{% block content %}

{% endblock %}
```

Podemos criar vários blocos.

```django
{% block title %}

{% endblock %}

{% block content %}

{% endblock %}

{% block scripts %}

{% endblock %}
```

Cada template filho sobrescreve apenas os blocos necessários.

---

# Alterando o título da página

No `base.html`:

```html
<title>

{% block title %}
Receitas
{% endblock %}

</title>
```

Na página Home:

```django
{% extends 'recipes/base.html' %}

{% block title %}
Home
{% endblock %}
```

Na página About:

```django
{% extends 'recipes/base.html' %}

{% block title %}
Sobre
{% endblock %}
```

Cada página terá seu próprio título.

---

# Enviando dados para o Template

Uma View pode enviar informações para o HTML utilizando um contexto.

Exemplo:

```python
def home(request):

    context = {
        "title": "Receitas"
    }

    return render(
        request,
        "recipes/home.html",
        context,
    )
```

---

# Context

O contexto é um dicionário contendo dados enviados ao template.

```python
context = {
    "title": "Receitas"
}
```

Cada chave poderá ser utilizada dentro do HTML.

---

# Utilizando variáveis

No template:

```html
<h1>{{ title }}</h1>
```

O Django substituirá:

```text
{{ title }}
```

por:

```text
Receitas
```

---

# Enviando uma lista

Na View:

```python
recipes = [
    "Lasanha",
    "Pizza",
    "Hambúrguer",
]

context = {
    "recipes": recipes
}
```

---

# Percorrendo listas

Utilizamos o template tag `for`.

```django
<ul>

{% for recipe in recipes %}

<li>{{ recipe }}</li>

{% endfor %}

</ul>
```

Resultado:

```text
• Lasanha

• Pizza

• Hambúrguer
```

---

# Enviando objetos

Também é possível enviar listas de dicionários.

```python
recipes = [
    {
        "id": 1,
        "title": "Lasanha",
    },
    {
        "id": 2,
        "title": "Pizza",
    },
]
```

No template:

```django
{% for recipe in recipes %}

<h2>{{ recipe.title }}</h2>

{% endfor %}
```

O Django acessa os atributos utilizando ponto (`.`).

---

# List Page

Uma **List Page** exibe vários registros.

Exemplo:

```text
Receita 1

Receita 2

Receita 3

Receita 4
```

View:

```python
def home(request):
    return render(...)
```

---

# Detail Page

Uma **Detail Page** exibe apenas um objeto.

Exemplo:

```text
Lasanha

Ingredientes

Modo de preparo

Tempo de preparo
```

View:

```python
def recipe(request, recipe_id):
    ...
```

---

# Parâmetros na URL

Podemos capturar valores diretamente pela URL.

```python
path(
    "recipes/<int:id>/",
    views.recipe,
    name="recipe",
)
```

Exemplos de URLs:

```text
recipes/1/

recipes/2/

recipes/3/
```

Na View:

```python
def recipe(request, id):
    ...
```

O Django envia automaticamente o valor da URL para o parâmetro da função.

---

# Nomeando URLs

É recomendado utilizar o parâmetro `name`.

```python
path(
    "",
    views.home,
    name="home",
)
```

Outro exemplo:

```python
path(
    "recipes/<int:id>/",
    views.recipe,
    name="recipe",
)
```

---

# A tag `url`

Em vez de escrever caminhos manualmente:

```html
<a href="/recipes/1/">
```

Utilizamos:

```django
<a href="{% url 'recipe' 1 %}">
```

Ou:

```django
<a href="{% url 'home' %}">
```

Assim, caso a URL seja alterada, basta modificar apenas o arquivo `urls.py`.

---

# app_name

Quando existem vários aplicativos, diferentes arquivos `urls.py` podem possuir nomes iguais.

Exemplo:

```text
recipes
blog
accounts
```

Todos podem possuir uma URL chamada:

```text
home
```

Para evitar conflitos:

```python
app_name = "recipes"
```

---

# Namespace

Após definir o `app_name`, utilizamos:

```django
{% url 'recipes:home' %}
```

Outro exemplo:

```django
{% url 'recipes:recipe' recipe.id %}
```

O namespace identifica de qual aplicação aquela URL pertence.

---

# Fluxo completo

```text
Usuário
      │
      ▼
URL
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
      │
      ▼
Navegador
```

---

# Organização recomendada

```text
meu_projeto/

config/

recipes/
│
├── templates/
│   └── recipes/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       └── detail.html
│
├── views.py
├── urls.py
└── models.py
```

---

# Boas práticas

- Organize os templates dentro da pasta da aplicação.
- Utilize um `base.html` para evitar repetição de código.
- Crie blocos (`block`) para tornar o layout reutilizável.
- Utilize `extends` para herdar o template base.
- Envie apenas os dados necessários através do contexto.
- Nomeie todas as URLs utilizando `name`.
- Utilize `{% url %}` em vez de escrever caminhos manualmente.
- Defina `app_name` para criar namespaces.
- Separe Views por responsabilidade.

---

# Resumo

À medida que uma aplicação Django cresce, é comum criar novas páginas, cada uma com sua própria URL, View e Template. Para evitar duplicação de código HTML, utiliza-se um template base (`base.html`) juntamente com a herança de templates (`extends`) e blocos (`block`).

As Views enviam informações aos templates por meio do contexto (`context`), permitindo renderizar variáveis, listas e objetos dinamicamente. Para tornar a navegação mais segura e organizada, todas as URLs devem possuir um nome (`name`) e ser acessadas pela tag `{% url %}`. Em projetos com múltiplas aplicações, o uso de `app_name` cria namespaces, evitando conflitos entre URLs com o mesmo nome e facilitando a manutenção da aplicação.