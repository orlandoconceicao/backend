# Teoria avançada do Django e ORM

Este módulo reúne conceitos avançados para entender melhor o Django, o ORM e a organização de uma aplicação profissional.

A ideia central é analisar como os dados são selecionados, filtrados e transformados, além de compreender tags genéricas, segurança, configuração de ambientes e validação de modelos.

---

## 1. Sobre termos: backend, frontend, fullstack, júnior, pleno e sênior

O desenvolvimento de software pode ser dividido em diferentes responsabilidades.

- **Backend**: lógica da aplicação, banco de dados, APIs e regras de negócio.
- **Frontend**: interface exibida ao usuário e interação no navegador.
- **Fullstack**: pessoa que trabalha com frontend e backend.
- **Júnior**: desenvolvedor em fase inicial, com mais necessidade de orientação e aprendizado.
- **Pleno**: desenvolvedor autônomo na maior parte das tarefas e capaz de tomar decisões técnicas.
- **Sênior**: desenvolvedor experiente que também orienta pessoas, planeja soluções e avalia impactos técnicos.

Esses termos não representam apenas tempo de carreira. Eles descrevem responsabilidades, autonomia, profundidade técnica e capacidade de resolução de problemas.

---

## 2. Criando uma view `theory` para executar os comandos

Uma view temporária pode ser usada durante o desenvolvimento para testar conceitos do ORM.

```python
from django.http import HttpResponse


def theory(request):
    return HttpResponse("View de teoria")
```

Essa view não é necessariamente usada em produção. Ela permite executar consultas, testar resultados e entender o comportamento de modelos e QuerySets sem construir uma interface completa.

---

## 3. QuerySets do Django são preguiçosas

Uma `QuerySet` não executa imediatamente toda operação realizada sobre ela.

```python
recipes = Recipe.objects.filter(is_published=True)
```

Nesse ponto, a consulta ainda não foi enviada ao banco. Ela é executada quando o valor é necessário, por exemplo ao iterar, converter em lista ou acessar o primeiro objeto.

O resultado permanece preguiçoso até que seja realmente utilizado. Encadeamento de filtros cria uma nova consulta potencial, sem executar todas as etapas isoladamente.

---

## 4. Recapitulando maneiras de selecionar objetos usando a QuerySet

Alguns métodos comuns permitem selecionar objetos ou obter um resultado específico.

```python
Recipe.objects.all()
Recipe.objects.filter(is_published=True)
Recipe.objects.exclude(is_published=False)
Recipe.objects.get(id=1)
Recipe.objects.first()
Recipe.objects.last()
```

Use `filter()` ou `exclude()` quando o resultado pode conter vários objetos. Use `get()` quando existe apenas um registro esperado e você deseja receber o objeto diretamente.

Se `get()` não encontrar nenhum objeto ou encontrar mais de um, ele pode lançar uma exceção.

---

## 5. Lookups e lookups complexos com `Q`

Lookups são modificadores usados nas consultas Django.

```python
Recipe.objects.filter(title__icontains="bolo")
Recipe.objects.filter(created_at__year=2026)
Recipe.objects.filter(preparation_time__lte=30)
```

Quando é necessário combinar condições com `OR`, `AND` ou `NOT`, pode-se usar `Q`.

```python
from django.db.models import Q

recipes = Recipe.objects.filter(
    Q(title__icontains="bolo") | Q(description__icontains="bolo")
)
```

`Q` permite criar filtros complexos mantendo a composição legível.

---

## 6. Usando `F` para referenciar campos

O objeto `F()` permite referenciar o valor de um campo diretamente dentro de uma consulta.

```python
from django.db.models import F

Recipe.objects.filter(preparation_time__lte=F("preparation_time"))
```

Ele também pode ser usado em atualizações:

```python
Recipe.objects.update(views=F("views") + 1)
```

Isso evita depender de um valor calculado fora do banco e permite comparar ou atualizar campos com base no próprio registro.

### Limitando e ordenando resultados

Slice limita o número de registros:

```python
Recipe.objects.all()[:10]
```

`order_by()` define a ordem:

```python
Recipe.objects.order_by("-created_at", "title")
```

O prefixo `-` indica ordem decrescente.

---

## 7. Especificando campos para melhor desempenho usando `values()`

`values()` faz a consulta retornar dados como dicionários, em vez de instâncias de model.

```python
recipes = Recipe.objects.values("id", "title")
```

Isso reduz o volume de dados solicitado ao banco e pode melhorar o desempenho quando não há necessidade de carregar objetos completos.

`values_list()` pode retornar tuplas:

```python
titles = Recipe.objects.values_list("title", flat=True)
```

O uso de `values()` é mais útil em listagens, relatórios e outras consultas que não modificam os registros.

---

## 8. `defer` e `only`

`defer()` indica que determinados campos não devem ser carregados inicialmente:

```python
Recipe.objects.defer("description")
```

`only()` indica os campos que devem ser carregados inicialmente:

```python
Recipe.objects.only("id", "title")
```

Esses recursos podem melhorar o desempenho ao evitar dados grandes ou pouco utilizados. Entretanto, acessar um campo adiado pode causar outra consulta ao banco.

Use `defer()` e `only()` somente quando o padrão de acesso aos dados é conhecido.

---

## 9. Usando funções de agregação

Funções de agregação calculam valores a partir de várias linhas.

```python
from django.db.models import Avg, Count, Max, Min

Recipe.objects.aggregate(
    total=Count("id"),
    maior_tempo=Max("preparation_time"),
    menor_tempo=Min("preparation_time"),
    tempo_medio=Avg("preparation_time"),
)
```

`aggregate()` devolve um dicionário com o resultado geral da consulta. Os nomes das chaves podem ser definidos pelo próprio código.

---

## 10. `annotate` para criar campos e valores na QuerySet

`annotate()` adiciona valores calculados a cada objeto da QuerySet.

```python
from django.db.models import Count

authors = Author.objects.annotate(
    total_recipes=Count("recipes")
)
```

Nesse exemplo, cada autor ganha um atributo `total_recipes` calculado pelo banco.

Depois, o campo anotado pode ser usado em filtros ou ordenação:

```python
authors.order_by("-total_recipes")
```

---

## 11. Criando seu próprio Manager para o model

Um `Manager` personalizado permite organizar filtros e comportamentos comuns.

```python
from django.db import models


class PublishedManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)


class Recipe(models.Model):
    # campos do model
    objects = PublishedManager()
```

Agora é possível reutilizar uma regra:

```python
Recipe.objects.published()
```

Managers deixam o código mais legível e evitam repetir filtros em várias views.

---

## 12. Tag App: criando um novo app para entender contenttypes

O framework `django.contrib.contenttypes` permite relacionar um objeto a qualquer model.

Para usar os tipos de conteúdo, adicione o app às configurações:

```python
INSTALLED_APPS = [
    "django.contrib.contenttypes",
]
```

Em seguida, pode-se criar um app exclusivo para tags ou etiquetas, reutilizável por receitas, autores e outros models.

---

## 13. Tag app: criando o model `Tag` com relação genérica

Uma relação genérica combina o tipo do model relacionado com a chave primária desse objeto.

```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
```

`content_type` identifica o model, `object_id` identifica o registro e `GenericForeignKey` fornece o objeto relacionado.

---

## 14. Tag app: relação com `GenericRelation` e cadastro no Django Admin

O `GenericRelation` permite acessar as tags relacionadas a partir do model que recebe a tag.

```python
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Recipe(models.Model):
    tags = GenericRelation("tags.Tag")
```

No Admin, o model pode ser registrado normalmente:

```python
from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
```

---

## 15. Tag app: exibindo dados em templates e criando uma view para tags

Para mostrar as tags no template, a view pode carregar o objeto e suas relações:

```python
def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    return render(request, "tags/detail.html", {"tag": tag})
```

No template:

```django
<h1>{{ tag.name }}</h1>
<p>{{ tag.content_object }}</p>
```

Isso permite navegar pelas tags e identificar o objeto associado a elas.

---

## 16. Tag app: usando o ORM com `ContentType`

`ContentType` permite buscar objetos vinculados a um model específico.

```python
from django.contrib.contenttypes.models import ContentType

recipe_type = ContentType.objects.get_for_model(Recipe)

tags = Tag.objects.filter(content_type=recipe_type)
```

O método `get_for_model()` garante que o tipo correto seja utilizado, inclusive em classes herdadas.

---

## 17. Corrigindo erros no PyTest por não carregar variáveis do `.env`

Os testes também precisam das configurações esperadas pela aplicação.

Um arquivo `.env` pode conter variáveis como:

```text
SECRET_KEY=chave-local
DEBUG=True
```

Se o projeto usa `django-environ`, elas podem ser carregadas no `settings.py`:

```python
import environ

env = environ.Env()
environ.Env.read_env()
```

Ao executar os testes, confirme que o arquivo `.env` existe, que os nomes das variáveis estão corretos e que o carregamento ocorre antes de o Django iniciar.

---

## 18. Tag app: usando `ManyToManyField` para tags

Uma relação muitos para muitos é outra forma de associar tags a objetos.

```python
class Recipe(models.Model):
    tags = models.ManyToManyField("tags.Tag", blank=True)
```

Diferente de uma relação genérica, o `ManyToManyField` exige que o relacionamento seja conhecido entre dois models específicos.

Exemplos de uso:

```python
recipe.tags.add(tag)
recipe.tags.remove(tag)
recipe.tags.all()
```

É uma solução apropriada quando as tags são usadas apenas por um tipo de model ou por tipos relacionados conhecidos.

---

## 19. `ALLOWED_HOSTS`

`ALLOWED_HOSTS` define quais domínios ou hostnames podem servir a aplicação.

```python
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "meu-dominio.com",
]
```

Em produção, use domínios reais e evite usar `["*"]`, exceto quando isso realmente tiver sido planejado e esteja protegido por outras medidas.

Essa configuração ajuda a evitar respostas não autorizadas para requisições com cabeçalhos `Host` inesperados.

---

## 20. `CSRF_TRUSTED_ORIGINS`

`CSRF_TRUSTED_ORIGINS` informa quais origens externas podem enviar requisições protegidas por CSRF.

```python
CSRF_TRUSTED_ORIGINS = [
    "https://meu-dominio.com",
]
```

Esse valor é necessário quando o domínio da aplicação é acessado por HTTPS e, especialmente, quando existem proxies reversos ou origens alternativas.

A configuração não substitui o middleware CSRF. Ela apenas declara quais origens podem ser confiadas além das regras padrões do mesmo host.

---

## 21. Organizando o arquivo `settings.py` em um Python package

À medida que o projeto cresce, uma única configuração pode se tornar extensa.

Uma estrutura comum é:

```text
config/
    settings/
        __init__.py
        base.py
        development.py
        production.py
        test.py
```

Em `__init__.py`, pode-se selecionar ou combinar a configuração adequada:

```python
from .base import *
from .development import *
```

Essa separação facilita manter valores comuns em um arquivo e configurações específicas em ambientes separados.

---

## 22. Atualizando o ChromeDriver e evitando erros com Pytest

Testes Selenium podem falhar quando a versão do Chrome não é compatível com o ChromeDriver.

Para evitar problemas:

- mantenha o Chrome atualizado
- use uma versão compatível do ChromeDriver
- confira se o executável está disponível no `PATH`
- garanta que o arquivo esteja configurado corretamente no projeto

Ao executar o Pytest, erros de navegador podem aparecer antes da falha real do teste. A mensagem do Selenium e a versão do Chrome ajudam a identificar incompatibilidade.

---

## 23. Validação de dados no próprio model

A validação centralizada no model evita que dados inválidos sejam repetidamente aceitos por formulários, views ou Admin.

```python
from django.core.exceptions import ValidationError


class Recipe(models.Model):
    title = models.CharField(max_length=255)

    def clean(self):
        if len(self.title) < 3:
            raise ValidationError(
                {"title": "O título deve ter pelo menos 3 caracteres."}
            )
```

O método `clean()` pode ser chamado explicitamente ou por formulários e `ModelForm`. A validação exclusiva em uma view não protege todos os fluxos.

---

## Conclusão

Este módulo reúne conceitos avançados que ajudam a construir aplicações Django mais eficientes e organizadas.

Ao longo dele, você viu que:

- QuerySets são preguiçosas e podem ser filtradas antes da execução
- `Q`, `F`, `values`, `defer` e `only` oferecem formas específicas de consultar dados
- agregações e `annotate` permitem analisar resultados no banco
- Managers personalizados reutilizam regras frequentes
- relações genéricas e `ManyToManyField` atendem necessidades diferentes
- configuração de hosts e CSRF exige atenção em ambiente de produção
- a organização das settings melhora projetos maiores
- testes dependem de configurações e versões compatíveis
- a validação no model centraliza regras de integridade

Esses conhecimentos ajudam a tomar decisões técnicas sobre ORM, segurança, testes e estrutura da aplicação.
