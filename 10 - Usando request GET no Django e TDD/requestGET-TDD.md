# Seção 10: Usando request.GET no Django e Introdução ao TDD (Test Driven Development)

---

## Duplicando receitas com o shell do Django

O Django oferece um shell interativo para executar comandos Python dentro do ambiente do projeto.

### Abrindo o shell

```bash
python manage.py shell
```

Dentro do shell, voc? pode importar os modelos e consultar os registros existentes no banco de dados:

```python
from recipes.models import Recipe

recipes = Recipe.objects.all()
```

`Recipe.objects.all()` retorna todos os registros do modelo `Recipe`.

Para duplicar uma receita, ? poss?vel criar novas inst?ncias com base nos dados existentes. ? importante observar os campos obrigat?rios e as regras de unicidade, como o `slug`, para evitar conflitos no banco de dados.

O shell ? ?til para executar opera??es pontuais e testar consultas sem precisar criar uma view.

---

## Corrigindo o campo slug

O `SlugField` ? usado para armazenar identificadores leg?veis para URLs.

```python
slug = models.SlugField(unique=True)
```

O argumento `unique=True` indica que o valor do campo deve ser ?nico no banco de dados. Isso significa que duas receitas n?o podem compartilhar o mesmo slug.

Exemplos v?lidos:

- pudim-de-leite-condensado
- bolo-de-chocolate
- pizza-caseira

Cada receita deve ter um identificador diferente quando esse campo possui essa restri??o.

Antes de adicionar `unique=True` a um campo j? existente, ? preciso verificar se h? valores duplicados e corrigi-los antes de aplicar a migra??o.

---

## Criando uma nova URL para busca com TDD

TDD significa Test Driven Development, ou Desenvolvimento Orientado a Testes.

Nesse m?todo, os testes s?o escritos antes da implementa??o da funcionalidade. O fluxo usual ?:

- Red: escrever um teste que falha
- Green: implementar o c?digo para fazer o teste passar
- Refactor: melhorar o c?digo sem alterar o comportamento esperado

Para testar se uma URL est? associada ? view correta, podemos usar `resolve()` e `reverse()`.

```python
def test_recipe_search_uses_correct_view_function(self):
    resolved = resolve(reverse('recipes:search'))
    self.assertIs(resolved.func, views.search)
```

Nesse teste:

- `reverse('recipes:search')` gera a URL a partir do nome da rota
- `resolve()` identifica qual view atende ? URL
- `resolved.func` retorna a fun??o associada ? rota
- `assertIs()` verifica se a fun??o encontrada ? a view esperada

A rota deve ser registrada no arquivo de URLs do aplicativo:

```python
path('search/', views.search, name='search')
```

Esse exemplo considera que o namespace da aplica??o ? `recipes` e que a fun??o `search` ser? implementada no m?dulo `views`.

---

## Criando a view de busca com TDD

Uma view ? respons?vel por receber uma requisi??o HTTP, executar a l?gica necess?ria e retornar uma resposta.

Para implementar a busca, come?amos criando testes que definem o comportamento esperado.

O cliente de testes do Django permite simular uma requisi??o:

```python
response = self.client.get(reverse('recipes:search'))
```

Uma implementa??o inicial da view pode usar `render()` para devolver um template:

```python
from django.shortcuts import render


def search(request):
    return render(request, 'recipes/pages/search.html')
```

Nesse exemplo, a view recebe a requisi??o e renderiza o template de busca.

A l?gica respons?vel por receber e processar o termo pesquisado pode ser implementada depois, conforme os requisitos definidos nos testes.

---

## Validando o template correto com TDD

Podemos usar testes automatizados para verificar se a view est? renderizando o template correto.

```python
def test_recipe_search_loads_correct_template(self):
    response = self.client.get(reverse('recipes:search'))
    self.assertTemplateUsed(response, 'recipes/pages/search.html')
```

Nesse teste:

- `self.client.get()` simula uma requisi??o HTTP GET
- `reverse()` gera a URL pelo nome da rota
- `assertTemplateUsed()` verifica se o template esperado foi utilizado

O template deve existir no caminho correspondente ? organiza??o do projeto.

Esse teste ajuda a identificar altera??es acidentais no template usado pela view.

---

## Padr?o MTV no Django

O Django utiliza a arquitetura MTV, que significa Model, Template e View.

### Model

O model representa os dados e define como eles s?o armazenados e consultados no banco de dados.

Exemplos de responsabilidades:

- definir os campos de uma receita
- representar categorias
- consultar registros no banco de dados
- definir relacionamentos entre os dados

### Template

O template ? respons?vel pela apresenta??o das informa??es ao usu?rio.

Normalmente, usa arquivos HTML com a linguagem de templates do Django.

Exemplos de responsabilidades:

- exibir receitas
- apresentar resultados de pesquisa
- organizar os elementos visuais da p?gina

### View

A view recebe a requisi??o, executa a l?gica necess?ria e decide qual resposta ser? retornada.

Exemplos de responsabilidades:

- receber o termo de busca
- consultar receitas
- selecionar o template
- enviar os resultados para a p?gina

### Fluxo b?sico do Django

1. O usu?rio acessa uma URL.
2. O sistema de URLs identifica a view correspondente.
3. A view processa a requisi??o.
4. Se necess?rio, a view consulta o model.
5. A view pode renderizar um template com os dados.
6. O Django retorna uma resposta HTTP.

A separa??o entre Model, Template e View ajuda a organizar o c?digo e facilita a manuten??o.

---

## Levantando erro 404 quando o termo de busca n?o for enviado

O c?digo HTTP `404 Not Found` indica que o recurso solicitado n?o foi encontrado.

Em uma funcionalidade de busca, podemos definir que uma requisi??o sem o termo esperado deve retornar uma resposta `404`, conforme a regra do projeto.

O atributo `request.GET` permite acessar os par?metros enviados pela URL por meio de uma requisi??o GET.

```python
search_term = request.GET.get('q', '').strip()
```

Nesse c?digo:

- `request.GET` cont?m os par?metros da requisi??o GET
- `get('q', '')` obt?m o par?metro `q` ou retorna uma string vazia se ele n?o existir
- `strip()` remove espa?os em branco no in?cio e no final do texto

Exemplo de URL com termo:

```text
/recipes/search/?q=bolo
```

Exemplo de URL sem termo:

```text
/recipes/search/
```

A view pode verificar se o termo est? vazio e retornar um erro `404`, caso essa seja a regra da funcionalidade.

? importante criar testes para garantir que a view apresente o comportamento esperado quando o termo n?o for enviado.

---

## Testes ajudam a prevenir regress?es

Uma regress?o acontece quando uma altera??o no c?digo faz uma funcionalidade que antes funcionava come?ar a falhar.

Os testes automatizados ajudam a detectar regress?es porque verificam se os comportamentos existentes continuam funcionando depois das modifica??es.

Por exemplo, ao criar uma nova funcionalidade de busca, podemos alterar uma view, um model ou um template. Essa mudan?a pode afetar outras p?ginas que dependem desses componentes.

Para executar os testes do Django, use:

```bash
python manage.py test
```

Se o projeto usa Pytest, execute:

```bash
pytest
```

Quando um teste falha, ? importante analisar:

- qual teste apresentou erro
- qual era o comportamento esperado
- qual foi o resultado obtido
- quais altera??es recentes podem ter causado o problema
- se o erro est? na implementa??o ou no pr?prio teste

Os testes n?o impedem todas as regress?es automaticamente, mas ajudam a detect?-las durante o desenvolvimento.

---

## Seguran?a: Cross-site scripting (XSS)

Cross-site scripting, conhecido como XSS, ? uma vulnerabilidade que ocorre quando conte?do n?o confi?vel ? interpretado pelo navegador como c?digo execut?vel.

Em uma aplica??o de receitas, por exemplo, um usu?rio pode enviar um texto contendo marca??es HTML ou JavaScript.

Se esse conte?do for inserido em uma p?gina de forma insegura, o navegador pode execut?-lo em vez de exib?-lo como texto.

Exemplo de conte?do potencialmente perigoso:

```html
<script>alert('XSS')</script>
```

Se esse conte?do for renderizado de forma insegura, o navegador poder? executar o JavaScript.

### Prote??o nos templates do Django

Por padr?o, o sistema de templates do Django realiza o escape autom?tico de vari?veis em contextos HTML comuns.

```html
<p>{{ search_term }}</p>
```

Ao exibir uma vari?vel dessa forma, o Django escapa caracteres especiais para evitar que sejam interpretados como marca??es HTML.

? importante n?o desativar essa prote??o desnecessariamente, por exemplo usando `safe` ou `{% autoescape off %}` quando o conte?do n?o ? confi?vel.

A prote??o contra XSS tamb?m depende do contexto em que os dados s?o inseridos. HTML, JavaScript, CSS e URLs podem exigir tratamentos diferentes.

---

## Removendo aspas sobrando no c?digo

Durante a implementa??o e os testes, ? importante revisar o c?digo para remover aspas desnecess?rias ou duplicadas.

Aspas s?o usadas para delimitar strings em Python e devem estar corretamente posicionadas.

Exemplo correto:

```python
search_term = request.GET.get('q', '')
```

Exemplo incorreto:

```python
search_term = request.GET.get('q', 'x')
```

O segundo exemplo mostra um caso em que a string foi escrita de forma incorreta e pode causar erro de sintaxe.

Tamb?m ? importante observar strings usadas em templates, consultas, URLs e testes. A revis?o do c?digo ajuda a evitar erros de sintaxe e mant?m a implementa??o mais leg?vel.

---

## Testando se `search_term` ser? escapado por seguran?a

Ao implementar a busca, devemos garantir que o termo pesquisado seja tratado com seguran?a quando exibido na p?gina.

Uma forma de verificar o escape autom?tico em um template Django ? enviar um termo contendo caracteres especiais e confirmar o conte?do retornado.

Exemplo de termo:

```python
search_term = '<script>alert("XSS")</script>'
```

O objetivo do teste ? verificar que o conte?do n?o seja interpretado como uma tag HTML execut?vel.

```python
def test_search_term_is_escaped(self):
    response = self.client.get(
        reverse('recipes:search'),
        {'q': '<script>alert("XSS")</script>'},
    )
    self.assertContains(response, '&lt;script&gt;')
```

Esse exemplo pressup?e que a view renderize o termo pesquisado em um contexto HTML com o escape autom?tico habilitado.

O teste deve ser adaptado ao template e ao comportamento real do projeto. Ele n?o substitui a an?lise de outros contextos que possam apresentar riscos de XSS.

---

## Separando testes em grupos por responsabilidade

Uma `Test Suite` ? um conjunto de testes organizados para serem executados em grupo.

Separar os testes por responsabilidade melhora a organiza??o e facilita a manuten??o do projeto.

Estrutura sugerida:

```text
recipes/
    tests/
        __init__.py
        test_recipe_views.py
        test_recipe_models.py
        test_recipe_urls.py
```

Nesse exemplo:

- `test_recipe_views.py` re?ne testes de view
- `test_recipe_models.py` re?ne testes de model
- `test_recipe_urls.py` re?ne testes de URLs

Tamb?m ? poss?vel separar os testes de cada view em classes distintas:

```python
class RecipeHomeViewTest(TestCase):
    pass


class RecipeSearchViewTest(TestCase):
    pass
```

Essa organiza??o ajuda a identificar rapidamente qual parte da aplica??o apresentou um problema.

Os arquivos devem seguir os padr?es de descoberta de testes configurados no projeto.

---

## Filtros `contains` e `icontains`

O Django ORM oferece filtros para pesquisar registros com base no conte?do de campos textuais.

### `contains`

O filtro `contains` verifica se o campo cont?m determinado texto, respeitando a diferencia??o entre letras mai?sculas e min?sculas conforme o banco de dados utilizado.

```python
Recipe.objects.filter(title__contains='bolo')
```

Essa consulta procura receitas cujo t?tulo contenha o texto `bolo`.

### `icontains`

O filtro `icontains` realiza uma busca sem diferenciar mai?sculas e min?sculas, conforme o banco de dados.

```python
Recipe.objects.filter(title__icontains='bolo')
```

Essa consulta permite encontrar t?tulos com varia??es de capitaliza??o do termo pesquisado.

---

## Consultas complexas com `Q`

A classe `Q` permite criar condi??es complexas e combinar filtros usando operadores l?gicos.

```python
from django.db.models import Q

Recipe.objects.filter(
    Q(title__icontains='bolo') |
    Q(description__icontains='bolo')
)
```

Nesse exemplo, a consulta retorna receitas cujo t?tulo ou descri??o contenha o termo pesquisado.

O operador `|` representa `OR`; isso significa que basta uma das condi??es ser verdadeira.

A classe `Q` ? ?til quando a busca precisa consultar v?rios campos ou combinar condi??es diferentes.

---

## Usando `Q` para combinar `AND` e `OR`

A classe `Q` permite combinar condi??es com os operadores `AND` e `OR`.

### Operador `AND`

O operador `&` exige que todas as condi??es combinadas sejam verdadeiras.

```python
from django.db.models import Q

Recipe.objects.filter(
    Q(title__icontains='bolo') &
    Q(is_published=True)
)
```

Essa consulta retorna receitas cujo t?tulo cont?m `bolo` e que est?o publicadas.

### Operador `OR`

O operador `|` permite que pelo menos uma das condi??es seja verdadeira.

```python
Recipe.objects.filter(
    Q(title__icontains='bolo') |
    Q(description__icontains='bolo')
)
```

Essa consulta retorna receitas que correspondem ao termo no t?tulo ou na descri??o.

### Combinando `AND` e `OR`

Podemos agrupar condi??es para definir a l?gica da consulta:

```python
Recipe.objects.filter(
    Q(is_published=True) &
    (
        Q(title__icontains='bolo') |
        Q(description__icontains='bolo')
    )
)
```

A consulta exige que a receita esteja publicada e que o termo apare?a no t?tulo ou na descri??o.

### Combinando `Q` com filtros existentes

Tamb?m ? poss?vel aplicar filtros convencionais e combin?-los com express?es `Q`.

```python
Recipe.objects.filter(
    is_published=True
).filter(
    Q(title__icontains='bolo') |
    Q(description__icontains='bolo')
)
```

Essa abordagem permite construir consultas mais flex?veis sem escrever SQL manualmente.

---

## Exerc?cio de programa??o

Os exerc?cios de programa??o ajudam a praticar os conceitos apresentados durante as aulas.

Ao completar um c?digo, ? importante compreender:

- qual comportamento precisa ser implementado
- quais fun??es e m?todos devem ser usados
- quais resultados s?o esperados
- como verificar a solu??o por meio de testes

A solu??o deve respeitar a estrutura e os requisitos definidos no enunciado do exerc?cio.

---

## Revis?o: temas principais

Os testes de revis?o verificam os conhecimentos adquiridos ao longo da se??o.

Os principais assuntos abordados incluem:

- requisi??es HTTP
- par?metros GET
- models e consultas ao banco de dados
- views e templates
- resolu??o de URLs
- testes automatizados
- TDD
- seguran?a contra XSS
- filtros `contains` e `icontains`
- consultas complexas com `Q`

Revisar esses conceitos ajuda a compreender como as partes de uma aplica??o Django trabalham em conjunto.

---

## Testando `request.GET` com `query string`

O atributo `request.GET` permite acessar os par?metros enviados por uma URL por meio de uma requisi??o HTTP GET.

Esses par?metros s?o conhecidos como query string.

Exemplo de URL:

```text
/recipes/search/?q=bolo
```

Nesse exemplo:

- `/recipes/search/` ? o caminho da URL
- `?` inicia a query string
- `q` ? o nome do par?metro
- `bolo` ? o valor enviado

### Obtendo o par?metro na view

```python
def search(request):
    search_term = request.GET.get('q', '')
```

O m?todo `get()` permite obter o valor do par?metro sem gerar `KeyError` quando ele n?o existe.

Se o par?metro `q` n?o for enviado, o exemplo retorna uma string vazia.

### Enviando par?metros com o cliente de testes

O cliente de testes do Django permite enviar par?metros GET sem precisar montar manualmente a query string.

```python
response = self.client.get(
    reverse('recipes:search'),
    {'q': 'bolo'},
)
```

O Django transforma o dicion?rio em par?metros da requisi??o.

O resultado equivale a acessar uma URL parecida com:

```text
/recipes/search/?q=bolo
```

### Testando o termo recebido

Podemos verificar se a view processou corretamente o par?metro enviado.

```python
response = self.client.get(
    reverse('recipes:search'),
    {'q': 'bolo'},
)
```

O teste pode verificar o conte?do da resposta, o contexto do template ou os resultados retornados pela busca, conforme a implementa??o da view.

---

## Resumo

- `request.GET` acessa os par?metros de uma requisi??o GET
- `request.GET.get('q', '')` obt?m o par?metro `q` ou uma string vazia
- query string permite enviar informa??es pela URL
- `self.client.get()` simula requisi??es GET nos testes
- `reverse()` gera a URL a partir do nome da rota

---
