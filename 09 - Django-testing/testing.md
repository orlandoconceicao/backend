# Testes no Django com Pytest, Pytest-Django e Unittest

Os testes são uma parte fundamental do desenvolvimento em Django. Eles permitem verificar automaticamente se o sistema continua funcionando corretamente após alterações no código, reduzindo a chance de erros e facilitando a manutenção do projeto.

O Django possui um sistema de testes integrado baseado no módulo `unittest` da biblioteca padrão do Python, mas também é muito comum utilizar o **Pytest**, que oferece uma sintaxe mais simples e recursos extras para criação e organização de testes.

## O que é um teste?

Um teste é um trecho de código responsável por verificar se determinada funcionalidade do sistema está se comportando conforme esperado.

Exemplo:

- verificar se uma página retorna status **200**
- verificar se uma URL existe
- verificar se um modelo salva corretamente no banco
- verificar se uma view retorna o template correto
- verificar se uma função retorna o resultado esperado

## O que é o Unittest?

O **Unittest** é o framework de testes nativo do Python.

O Django utiliza esse framework como base para sua estrutura de testes.

Exemplo:

```python
from django.test import TestCase


class ExampleTest(TestCase):
    def test_example(self):
        self.assertEqual(2 + 2, 4)
```

Nesse exemplo:

- `TestCase` cria um ambiente de testes
- `test_example` é um método de teste
- `assertEqual` verifica se os valores são iguais

---

# O que é o Pytest?

O **Pytest** é um framework de testes muito popular na comunidade Python.

Ele possui uma sintaxe mais simples, gera mensagens de erro mais claras e oferece diversos plugins.

Exemplo:

```python
def test_example():
    assert 2 + 2 == 4
```

Perceba que não é necessário criar uma classe obrigatoriamente.

---

# O que é o Pytest-Django?

O **Pytest-Django** é um plugin que permite utilizar o Pytest em projetos Django.

Ele integra o Pytest com:

- banco de dados
- configurações do Django
- models
- views
- templates
- URLs
- fixtures

Sem esse plugin o Pytest não consegue trabalhar corretamente com projetos Django.

---

# Instalando

```bash
pip install pytest
pip install pytest-django
```

Também é comum instalar:

```bash
pip install pytest-watch
```

ou

```bash
pip install coverage
```

---

# Configurando o Pytest

Normalmente é criado um arquivo chamado:

```text
pytest.ini
```

Exemplo:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
python_files = test_*.py *_test.py tests.py
```

Assim o Pytest sabe onde estão as configurações do Django.

---

# Test Runner

O **Test Runner** é o componente responsável por localizar, executar e mostrar os resultados dos testes.

Quando executamos:

```bash
pytest
```

ou

```bash
python manage.py test
```

o Test Runner:

1. encontra os testes
2. prepara o ambiente
3. cria um banco temporário
4. executa todos os testes
5. mostra quais passaram ou falharam
6. remove o banco temporário

---

# Estrutura dos testes

Uma estrutura bastante utilizada é:

```text
recipes/
    tests/
        __init__.py
        test_recipe_views.py
        test_recipe_models.py
        test_recipe_urls.py
```

Separar os testes em um package melhora bastante a organização do projeto.

---

# Django Reverse URL

Ao invés de escrever URLs manualmente, utiliza-se a função `reverse`.

Exemplo:

```python
from django.urls import reverse

url = reverse('recipes:home')
```

Vantagens:

- evita URLs fixas
- facilita manutenção
- evita erros ao alterar rotas

---

# Reverse com args

```python
reverse(
    'recipes:recipe',
    args=(10,)
)
```

Resultado:

```text
/recipes/10/
```

---

# Reverse com kwargs

```python
reverse(
    'recipes:recipe',
    kwargs={
        'id': 10
    }
)
```

Resultado:

```text
/recipes/10/
```

---

# Resolve

A função `resolve` faz o caminho inverso do `reverse`.

Enquanto `reverse` gera uma URL, o `resolve` identifica qual view atende determinada URL.

Exemplo:

```python
from django.urls import resolve

match = resolve('/recipes/')
```

Pode-se verificar:

```python
match.func
```

para descobrir qual view será executada.

---

# Cliente de testes do Django

O Django disponibiliza um cliente HTTP para simular requisições.

```python
self.client.get('/')
```

ou

```python
response = self.client.get('/')
```

Esse cliente permite testar:

- GET
- POST
- PUT
- DELETE
- autenticação
- sessões
- cookies

sem abrir um navegador.

---

# Testando Status Code

```python
response = self.client.get('/')

self.assertEqual(
    response.status_code,
    200
)
```

Esse teste verifica se a página foi carregada corretamente.

---

# Testando Templates

```python
self.assertTemplateUsed(
    response,
    'recipes/pages/home.html'
)
```

Verifica se a view utilizou o template correto.

---

# Testando Context

As views enviam dados para o template através do contexto.

```python
context = response.context
```

Exemplo:

```python
self.assertIn(
    'recipes',
    response.context
)
```

---

# Testando Content

Também é possível verificar se determinado texto foi renderizado.

```python
self.assertIn(
    'Bolo de Chocolate',
    response.content.decode('utf-8')
)
```

---

# Testando "No recipes found"

Quando não existem receitas cadastradas:

```python
self.assertIn(
    'No recipes found',
    response.content.decode('utf-8')
)
```

Esse teste garante que a mensagem correta seja exibida.

---

# Testando erro 404

Quando uma receita não existe:

```python
response = self.client.get('/recipes/9999/')
```

```python
self.assertEqual(
    response.status_code,
    404
)
```

---

# Fixtures

Fixtures criam objetos necessários para os testes.

Exemplo:

- usuário
- categoria
- receita

Assim evita-se repetir código em vários testes.

---

# Classe Base de Testes

É comum criar uma classe base contendo métodos reutilizáveis.

Exemplo:

```python
class RecipeBaseTest(TestCase):
    pass
```

Outras classes herdam dela.

Isso reduz duplicação de código.

---

# Métodos reutilizáveis

Em vez de repetir:

```python
Category.objects.create(...)
```

cria-se um método:

```python
def make_category():
    ...
```

e todos os testes reutilizam essa função.

---

# Falhando testes propositalmente

Pode-se forçar uma falha.

```python
self.fail()
```

Isso é útil durante o desenvolvimento.

---

# Ignorando testes

Também é possível ignorar temporariamente um teste.

```python
from unittest import skip

@skip('Em desenvolvimento')
def test_example(self):
    ...
```

---

# Testando Models

Os modelos também devem ser testados.

Exemplo:

- valores padrão
- validações
- relacionamentos
- métodos
- representação em string

---

# Testando max_length

Utiliza-se normalmente:

```python
with self.assertRaises(
    ValidationError
):
    ...
```

O Context Manager verifica se determinada exceção foi lançada.

---

# Testes Parametrizados

Com o pacote `parameterized` é possível executar o mesmo teste utilizando vários valores.

Exemplo:

```python
@parameterized.expand([
    ('A'),
    ('B'),
    ('C'),
])
```

Isso evita repetir vários testes praticamente iguais.

---

# Valores Default

Também é possível verificar se os valores padrão do model estão corretos.

Exemplo:

```python
published = False
```

Caso alguém altere esse valor futuramente, o teste detectará o problema.

---

# Cobertura de Testes (Coverage)

O **Coverage** mede quanto do código foi executado pelos testes.

Instalação:

```bash
pip install coverage
```

Executando:

```bash
coverage run -m pytest
```

Gerando relatório:

```bash
coverage report
```

Ou um relatório HTML:

```bash
coverage html
```

Quanto maior a cobertura, maior a quantidade de código testado.

---

# Testando __str__()

É importante verificar se a representação textual do model está correta.

Exemplo:

```python
self.assertEqual(
    str(recipe),
    recipe.title
)
```

---

# Testando Category

Também é comum testar:

```python
self.assertEqual(
    str(category),
    category.name
)
```

Assim garante-se que a representação da categoria permaneça correta.

---

# Pytest-Watch

O **pytest-watch** executa automaticamente os testes sempre que um arquivo é salvo.

Executando:

```bash
ptw
```

Isso acelera bastante o desenvolvimento.

---

# Boas práticas

- escreva testes pequenos
- cada teste deve validar apenas uma funcionalidade
- utilize nomes descritivos
- reutilize código com classes base e fixtures
- utilize `reverse` em vez de URLs fixas
- teste models, views, templates e URLs
- mantenha uma boa cobertura de testes
- execute os testes frequentemente durante o desenvolvimento

---

# Resumo

Os testes garantem que o sistema continue funcionando corretamente mesmo após modificações no código. O Django utiliza o `unittest` como base, mas muitos projetos preferem o **Pytest** juntamente com o **Pytest-Django** pela simplicidade e flexibilidade.

Durante os testes é comum utilizar recursos como `reverse`, `resolve`, `self.client`, fixtures, classes base, testes parametrizados, cobertura de código com `coverage` e validações de models, views, templates e URLs.

Em resumo:

- `unittest` é o framework padrão do Python
- `TestCase` cria um ambiente isolado para testes
- `Pytest` simplifica a escrita dos testes
- `Pytest-Django` integra o Pytest ao Django
- `reverse` gera URLs pelo nome da rota
- `resolve` identifica qual view atende uma URL
- `self.client` simula requisições HTTP
- fixtures evitam repetição de código
- `coverage` mede a cobertura dos testes
- testes automatizados tornam aplicações Django mais seguras, confiáveis e fáceis de manter.