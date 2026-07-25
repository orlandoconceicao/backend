# Arquivos Estáticos no Django

Os arquivos estáticos são recursos utilizados pela aplicação que não são gerados dinamicamente pelo Django. Eles são responsáveis pela aparência e pela interatividade das páginas, sendo enviados ao navegador separadamente do HTML.

Entre os arquivos estáticos mais comuns estão:

- CSS
- JavaScript
- Imagens
- Ícones
- Fontes

---

# Como o Django trabalha com arquivos estáticos

Quando uma página HTML é carregada, o navegador identifica referências a arquivos CSS, JavaScript e imagens.

Após receber o HTML, ele realiza novas requisições para buscar esses arquivos.

Exemplo:

```html
<link rel="stylesheet" href="/static/css/style.css">
```

Nesse exemplo, o navegador solicita o arquivo localizado em `/static/css/style.css`.

---

# Organização dos arquivos

Cada aplicação pode possuir sua própria pasta chamada `static`.

Exemplo:

```text
meu_projeto/
│
├── app/
│   ├── static/
│   │   └── app/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── script.js
│   │       └── img/
│   │           └── logo.png
│   │
│   ├── templates/
│   └── views.py
│
├── config/
└── manage.py
```

É recomendado colocar os arquivos dentro de uma pasta com o mesmo nome da aplicação para evitar conflitos entre arquivos de diferentes apps.

---

# Utilizando arquivos estáticos nos templates

Antes de utilizar arquivos estáticos em um template, é necessário carregar a biblioteca de templates do Django.

```django
{% load static %}
```

Depois disso, utiliza-se a tag `static`.

Exemplo com CSS:

```html
<link rel="stylesheet" href="{% static 'app/css/style.css' %}">
```

Imagem:

```html
<img src="{% static 'app/img/logo.png' %}" alt="Logo">
```

JavaScript:

```html
<script src="{% static 'app/js/script.js' %}"></script>
```

---

# A tag `load static`

A instrução abaixo habilita o uso da tag `static` dentro do template.

```django
{% load static %}
```

Sem ela, o Django não reconhecerá a tag `{% static %}` e ocorrerá um erro.

---

# STATIC_URL

A configuração `STATIC_URL` define o endereço base utilizado para acessar os arquivos estáticos.

No arquivo `settings.py`:

```python
STATIC_URL = "static/"
```

Quando utilizamos:

```django
{% static 'app/css/style.css' %}
```

O Django gera uma URL semelhante a:

```text
/static/app/css/style.css
```

---

# STATICFILES_DIRS

Além das pastas `static` existentes em cada aplicativo, é possível informar diretórios adicionais onde o Django também deve procurar arquivos estáticos.

Exemplo:

```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

Estrutura:

```text
meu_projeto/

static/
├── css/
├── js/
└── img/

config/
manage.py
```

Essa pasta costuma ser utilizada para arquivos compartilhados por toda a aplicação.

---

# Diferença entre `static` e `STATICFILES_DIRS`

A pasta `static` de cada aplicativo contém arquivos específicos daquele aplicativo.

Já `STATICFILES_DIRS` aponta para diretórios compartilhados, onde podem ficar arquivos utilizados por todo o projeto.

---

# STATIC_ROOT

Durante o desenvolvimento, o Django encontra os arquivos diretamente nas pastas configuradas.

Em produção, normalmente todos os arquivos são reunidos em um único diretório.

Essa pasta é definida por:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

# O comando `collectstatic`

O comando:

```bash
python manage.py collectstatic
```

copia todos os arquivos encontrados nas pastas configuradas para o diretório definido em `STATIC_ROOT`.

Antes:

```text
app1/static/app1/css/style.css

app2/static/app2/js/script.js

static/img/logo.png
```

Depois:

```text
staticfiles/

├── app1/
├── app2/
└── img/
```

---

# Quando utilizar `collectstatic`

Esse comando é utilizado principalmente antes de publicar a aplicação em produção.

Durante o desenvolvimento, o servidor do Django já consegue localizar os arquivos automaticamente.

---

# Fluxo de funcionamento

```text
Arquivo criado na pasta static
        │
        ▼
Template utiliza {% static %}
        │
        ▼
Django gera a URL correta
        │
        ▼
O navegador solicita o arquivo
        │
        ▼
O arquivo é enviado ao navegador
```

Em produção, antes do servidor web entregar os arquivos, todos eles são reunidos através do comando `collectstatic`.

---

# Exemplo de configuração

## settings.py

```python
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

## Estrutura de diretórios

```text
meu_projeto/

static/
├── css/
│   └── style.css
├── js/
│   └── script.js
└── img/
    └── logo.png
```

---

## Template HTML

```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">

    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>

    <img src="{% static 'img/logo.png' %}" alt="Logo">

    <script src="{% static 'js/script.js' %}"></script>

</body>
</html>
```

---

# Desenvolvimento e Produção

| Desenvolvimento | Produção |
|-----------------|----------|
| O Django encontra os arquivos diretamente nas pastas configuradas. | Os arquivos são reunidos em `STATIC_ROOT`. |
| Não é necessário executar `collectstatic`. | É necessário executar `collectstatic` antes da publicação. |
| O servidor de desenvolvimento serve os arquivos automaticamente. | Um servidor web, como Nginx ou Apache, normalmente entrega os arquivos estáticos. |

---

# Resumo

Os arquivos estáticos são utilizados para armazenar recursos como CSS, JavaScript, imagens, ícones e fontes.

Os principais conceitos são:

- `static/` → pasta onde os arquivos estáticos ficam armazenados.
- `{% load static %}` → habilita o uso da tag `static`.
- `{% static %}` → gera a URL correta do arquivo.
- `STATIC_URL` → define o endereço base dos arquivos estáticos.
- `STATICFILES_DIRS` → adiciona diretórios extras de arquivos estáticos.
- `STATIC_ROOT` → diretório que reúne todos os arquivos para produção.
- `collectstatic` → copia todos os arquivos para `STATIC_ROOT`, preparando a aplicação para ser publicada.