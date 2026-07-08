# Função render no Django

A função `render` é uma das ferramentas mais usadas no Django para devolver uma página HTML para o navegador.

Em vez de montar manualmente uma resposta com `HttpResponse`, o `render` faz esse trabalho de forma mais prática, porque ele já conecta a view com um template HTML.

## O que é o render?

`render` é uma função que recebe:

- a requisição (`request`)
- o template que será exibido
- um dicionário com dados opcionais para o template

Ela retorna um objeto `HttpResponse` com o conteúdo HTML já processado.

## Estrutura básica

```python
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
```

### Explicação:

- `request`: representa a requisição feita pelo navegador
- `'home.html'`: é o arquivo HTML que será mostrado
- `render`: monta a resposta final para o usuário

## Como funciona na prática?

Quando o usuário acessa uma URL, o Django chama a view correspondente. A view pode usar `render` para mostrar um template.

Exemplo:

```python
from django.shortcuts import render


def sobre(request):
    return render(request, 'sobre.html')
```

Nesse caso:

1. O navegador faz uma requisição
2. A URL chama a view `sobre`
3. A view usa `render`
4. O Django procura o arquivo `sobre.html`
5. A página é enviada ao navegador

## Enviando dados para o template

O `render` também pode passar informações para o template.

```python
from django.shortcuts import render


def index(request):
    nome = 'Maria'
    idade = 25
    contexto = {
        'nome': nome,
        'idade': idade
    }
    return render(request, 'index.html', contexto)
```

No template `index.html`, você pode usar esses dados assim:

```html
<h1>Olá, {{ nome }}</h1>
<p>Idade: {{ idade }}</p>
```

## Diferença entre `render` e `HttpResponse`

### Usando `HttpResponse`

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Olá mundo</h1>')
```

Esse exemplo funciona, mas fica menos organizado, porque o HTML está escrito diretamente no Python.

### Usando `render`

```python
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
```

Com `render`, o HTML fica em um arquivo separado, o que deixa o projeto mais limpo e organizado.

## Vantagens do render

O `render` é muito útil porque:

- separa lógica e apresentação
- facilita a manutenção do código
- permite usar templates HTML
- deixa o projeto mais organizado
- torna mais simples passar dados para a página

## Importante

Para usar `render`, é necessário importar:

```python
from django.shortcuts import render
```

## Exemplo completo

```python
from django.shortcuts import render


def home(request):
    titulo = 'Minha página inicial'
    contexto = {
        'titulo': titulo
    }
    return render(request, 'home.html', contexto)
```

Template:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
</head>
<body>
    <h1>{{ titulo }}</h1>
</body>
</html>
```

## Resumo

A função `render` é usada para retornar páginas HTML de forma prática e organizada. Ela conecta a view com um template, permite passar dados para a página e deixa o projeto mais limpo do que escrever HTML direto no Python.

Em resumo:

- `HttpResponse` escreve a resposta diretamente
- `render` monta a resposta a partir de um template

Essa é uma das formas mais comuns de trabalhar com Django em páginas web.
