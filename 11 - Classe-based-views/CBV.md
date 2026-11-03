# Classe-Based Views (CBV) no Django

Este módulo reúne os principais conceitos de `Class Based Views` e mostra como Django pode organizar a lógica de uma aplicação por meio de classes, herança e métodos reutilizáveis.

A ideia central é simples: em vez de escrever uma função para cada requisição, você pode usar classes que já possuem comportamento padrão e personalizá-las conforme a necessidade.

---

## 1. Class Based Views e Function Based Views são dois recursos Django, não inimigos

As `Function Based Views` (FBV) e as `Class Based Views` (CBV) resolvem o mesmo problema: receber uma requisição e devolver uma resposta.

### Diferença principal

- FBV: lógica escrita em funções
- CBV: lógica organizada em classes e métodos

### Vantagens das CBVs

- reutilização de código
- maior organização
- herança entre views
- padronização com classes do Django

Em resumo, elas não são concorrentes; são abordagens diferentes para a mesma solução.

---

## 2. Mais detalhes sobre as class based views e documentação oficial do Django

A documentação oficial do Django é a melhor referência para entender as CBVs.

### O que aprender nessa parte

- como as classes do Django funcionam
- quais métodos existem por padrão
- como personalizar comportamento com `get`, `post`, `dispatch` e outros
- como a herança melhora o código

### Ideia prática

Quando você usa uma CBV, a classe define o fluxo da requisição e cada método representa uma etapa dessa execução. Isso deixa o código mais claro e previsível.

---

## 3. Adicionando `get_absolute_url` no model

O método `get_absolute_url()` indica qual é a URL canônica de um objeto do banco.

### Para que serve

- gerar links para detalhes do objeto
- redirecionar após salvar
- facilitar o uso em templates e views

### Exemplo

```python
class Recipe(models.Model):
    def get_absolute_url(self):
        return reverse('recipes:detail', args=[self.id])
```

Assim, o Django consegue descobrir automaticamente onde aquele registro deve ser exibido.

---

## 4. Fazendo `slugify` no model e usando `save`

`slugify` transforma texto em um identificador amigável para URL.

### Exemplo

```python
from django.utils.text import slugify

class Recipe(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
```

### Por que isso importa

- deixa a URL mais limpa
- melhora a organização da rota
- evita problemas com espaços e acentos

Essa prática é muito útil em projetos com páginas por objeto ou categoria.

---

## 5. Movendo `views.py` para o package `views` para organização

Quando o projeto cresce, o arquivo `views.py` pode virar um ponto de confusão.

### Benefícios de separar em pacote

- melhor organização
- menos código em um único arquivo
- divisão por responsabilidade
- manutenção mais simples

### Estrutura comum

```text
views/
    __init__.py
    home.py
    recipe.py
    category.py
    search.py
```

Isso torna o projeto mais escalável e mais fácil de navegar.

---

## 6. Criando uma view usando a classe base `django.views.View`

A classe base `View` do Django é o ponto de partida para as CBVs.

### O que ela faz

Ela recebe a requisição, identifica o método HTTP (`GET`, `POST`, etc.) e chama o método correspondente.

### Exemplo básico

```python
from django.views import View
from django.http import HttpResponse

class MyView(View):
    def get(self, request):
        return HttpResponse('Olá do Django!')
```

### Observação

Esse é o primeiro passo para criar views mais organizadas, sem a necessidade de escrever toda a lógica em funções isoladas.

---

## 7. Criando o método `post` e reorganizando a class based view

Além do `get`, a classe `View` também lida com `post`.

### Estrutura típica

```python
class RecipeCreateView(View):
    def get(self, request):
        return HttpResponse('Formulário')

    def post(self, request):
        return HttpResponse('Processando envio')
```

### Benefício

A lógica fica separada por tipo de requisição. Isso deixa a classe muito mais legível e facilita a manutenção.

---

## 8. Reutilizando a class based view para gerar novas recipes

Uma CBV pode ser reaproveitada para criar vários objetos com lógica semelhante.

### Ideia

Se a criação de receitas tem regras repetidas, você pode centralizar os passos em uma classe base ou na própria view.

### Vantagens

- menos duplicação de código
- melhor consistência
- menos risco de erro em vários fluxos

Essa reutilização é uma das principais razões para usar CBVs em projetos maiores.

---

## 9. Adicionando `login_required` em class based views e seus métodos

`login_required` garante que apenas usuários autenticados possam acessar determinada parte do sistema.

### Em funções

```python
from django.contrib.auth.decorators import login_required
```

### Em classes

O padrão é aplicar a regra na classe ou em métodos específicos usando decorators.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
```

### Benefício

Você protege a view sem misturar lógica de autenticação diretamente com o restante da lógica de negócios.

---

## 10. Reutilizando a class based view na herança para deletar coisas

Herança é um dos grandes diferenciais das CBVs.

### Conceito

Você cria uma classe base com o comportamento geral e outras classes herdam dela.

### Exemplo de uso

- uma base para CRUD
- uma subclasse para criação
- outra subclasse para exclusão

Assim, a lógica compartilhada fica em um só lugar e a exclusão de objetos é implementada de forma mais consistente.

---

## 11. `ListView`: criando uma base para Home, Category e Search de recipes

`ListView` é a CBV usada para listar objetos em uma página.

### Quando usar

- página inicial com várias receitas
- categoria com vários registros
- resultados de busca

### Estrutura geral

```python
from django.views.generic import ListView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/pages/home.html'
```

Ela já entende que deve buscar os registros do banco e passar para o template.

---

## 12. Home `ListView` + Desafio

Nesta etapa, a `ListView` é aplicada à página inicial do projeto.

### Objetivo

Exibir uma lista de receitas na home e manter o código organizado.

### Desafio

Enquanto a listagem funciona, pode ser necessário:

- ajustar o template
- filtrar por categoria
- aplicar ordem
- controlar quantos itens aparecem

Esse exercício ajuda a entender como personalizar a `ListView` sem perder a base fornecida pela própria classe.

---

## 13. `Category` `ListView`

A mesma ideia da home pode ser reaproveitada para uma página de categoria.

### Exemplo

Ao acessar uma categoria específica, a view busca apenas os objetos relacionados àquela categoria.

### Benefício

Você usa a mesma estrutura base da `ListView`, mudando apenas:

- o `queryset`
- o template
- o filtro da categoria

Isso reduz a duplicação de código.

---

## 14. `Search` `ListView`

A busca também pode ser implementada com `ListView`.

### Como funciona

A view recebe um termo enviado por `GET`, filtra os resultados e renderiza a página com os itens encontrados.

### Exemplo de comportamento

```python
search_term = request.GET.get('q', '').strip()
```

Se houver termo, a lista é filtrada; se não houver, a página pode devolver uma resposta vazia ou um erro de regra de negócio.

---

## 15. Corrigindo os testes que quebraram com as class based views

Quando você migra de funções para classes, alguns testes podem falhar.

### Motivos comuns

- URL apontando para a view errada
- template não encontrado
- queryset diferente do esperado
- comportamento de `GET`/`POST` alterado

### O papel dos testes

Os testes garantem que a refatoração não quebrou a funcionalidade. Com eles, você valida:

- rota correta
- template correto
- dados esperados
- status HTTP correto

---

## 16. Movendo a FBV de detalhes da receita para a `DetailView`

A `DetailView` é a CBV usada para exibir um único objeto.

### Antes

A aplicação provavelmente tinha uma função que buscava uma receita e renderizava seus detalhes.

### Depois

A lógica é movida para uma classe como:

```python
from django.views.generic import DetailView

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/pages/recipe_detail.html'
```

### Benefício

O Django cuida de buscar o registro, validar a existência e enviar os dados para o template.

---

## 17. Corrigindo os testes da `DetailView`

Depois da troca para `DetailView`, é necessário ajustar testes que validavam a antiga lógica de função.

### O que normalmente é revisado

- se a view está sendo resolvida corretamente
- se o objeto certo está sendo mostrado
- se o template está correto
- se o status é `200` em caso de sucesso
- se a página responde corretamente quando não encontra o registro

Essa etapa demonstra que a mudança para CBV não é apenas estética: ela exige revisar o comportamento e garantir que tudo continue funcionando.

---

## Conclusão

As `Class Based Views` deixam o Django mais organizado e reutilizável.

Ao longo do módulo, você aprendeu que:

- FBV e CBV podem coexistir
- as classes ajudam a estruturar a lógica
- `View`, `ListView` e `DetailView` são pilares importantes
- herança e métodos reduzem repetições
- testes são essenciais para garantir que a refatoração não quebre a aplicação

Esse conjunto de conhecimentos é a base para construir projetos Django mais escaláveis, legíveis e profissionais.
