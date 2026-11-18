# Django Debug Toolbar e otimização de consultas

Este módulo reúne conceitos para investigar o comportamento de uma aplicação Django e melhorar o acesso aos dados.

A Django Debug Toolbar ajuda a observar o que acontece durante uma requisição. Com essas informações, é possível identificar consultas repetidas, aplicar `select_related` ou `prefetch_related` e investigar erros que aparecem ao executar a aplicação com Gunicorn.

---

## 1. Informações e instalação da Django Debug Toolbar

A Django Debug Toolbar é uma ferramenta de desenvolvimento que exibe informações sobre cada requisição, como consultas ao banco de dados, tempo de execução, templates renderizados e configurações utilizadas.

### Instalação

Instale o pacote no ambiente virtual do projeto:

```bash
pip install django-debug-toolbar
```

### Configuração básica

Adicione a aplicação às configurações do Django:

```python
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
]
```

Inclua o middleware da Toolbar antes do middleware de mensagens, caso ele esteja configurado:

```python
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```

No arquivo principal de URLs, disponibilize a rota durante o desenvolvimento:

```python
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    # ...
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
```

A Toolbar normalmente exige que `DEBUG` esteja habilitado e que o endereço do navegador esteja em `INTERNAL_IPS`. A configuração deve ser usada apenas no ambiente de desenvolvimento, não exposta em produção.

### Como usar

Depois de iniciar o servidor de desenvolvimento, abra uma página HTML do projeto. A barra lateral mostra painéis com detalhes da requisição. O painel **SQL** é especialmente útil para observar a quantidade e a duração das consultas ao banco.

---

## 2. Evitando consultas N+1 com `select_related`

O problema N+1 acontece quando uma consulta busca uma lista de objetos e, em seguida, uma consulta adicional é executada para cada objeto relacionado.

Por exemplo, ao listar receitas e acessar o autor de cada uma, o código pode executar uma consulta para buscar as receitas e mais uma consulta por receita para buscar seu autor.

### Usando `select_related`

`select_related()` carrega objetos relacionados em uma única consulta SQL, usando `JOIN`. Ele é indicado para relacionamentos de valor único, como `ForeignKey` e `OneToOneField`.

```python
recipes = Recipe.objects.select_related("author")
```

Agora, ao percorrer as receitas e acessar `recipe.author`, o Django já tem os dados do autor carregados.

### Quando usar

- ao acessar um relacionamento `ForeignKey`
- ao acessar um relacionamento `OneToOneField`
- quando o código percorre resultados e consulta o objeto relacionado de cada item

Use o painel SQL da Debug Toolbar para comparar as consultas antes e depois. A otimização correta reduz consultas repetidas sem alterar os dados exibidos.

---

## 3. Evitando consultas desnecessárias com `prefetch_related`

`prefetch_related()` também carrega objetos relacionados antecipadamente, mas faz isso com consultas separadas e combina os resultados em Python.

Ele é adequado para relacionamentos com vários objetos, como `ManyToManyField` e relacionamentos reversos de `ForeignKey`.

### Exemplo

Se cada receita pode ter várias categorias, elas podem ser carregadas antecipadamente:

```python
recipes = Recipe.objects.prefetch_related("categories")
```

Ao percorrer as receitas e acessar `recipe.categories.all()`, o Django reutiliza os objetos que já foram buscados, em vez de executar uma consulta para cada receita.

### Diferença entre os métodos

- `select_related`: usa `JOIN` em uma consulta; indicado para relacionamentos de objeto único.
- `prefetch_related`: executa consultas separadas e combina os resultados; indicado para relacionamentos com vários objetos.

### Como decidir

Observe quais relacionamentos o código realmente acessa e confira o painel SQL. Carregar antecipadamente relações que não são utilizadas pode fazer o Django buscar dados desnecessários; por isso, aplique a otimização conforme o uso da página.

---

## 4. Enviando os dados para o servidor e debugando os erros do Gunicorn

Depois que a aplicação é iniciada por um servidor como o Gunicorn, erros que não aparecem da mesma forma no servidor de desenvolvimento podem ser investigados pelos logs do processo e pela resposta da aplicação.

### Investigando uma requisição

Ao reproduzir o problema:

- confira a URL e os dados enviados na requisição
- observe o status HTTP e a resposta recebida
- verifique os logs do Gunicorn e da aplicação Django
- confira os logs do servidor que inicia o processo, como `systemd`, quando aplicável

Em instalações com `systemd`, os logs do serviço podem ser consultados com:

```bash
journalctl -u nome-do-servico
```

O nome do serviço e o local dos logs dependem da configuração do servidor. Mensagens de erro e tracebacks ajudam a localizar a view, o middleware ou outra etapa que falhou.

### Cuidados em produção

Não habilite `DEBUG=True` em produção para tentar encontrar o erro. A página detalhada de erro do Django pode expor configurações e dados internos. Mantenha `DEBUG=False` e use logs do servidor e da aplicação para investigar os problemas.

---

## Conclusão

A Django Debug Toolbar ajuda a entender o que acontece durante uma requisição e a identificar consultas que podem ser otimizadas.

Ao longo deste módulo, você aprendeu que:

- a Debug Toolbar apresenta informações úteis durante o desenvolvimento
- `select_related` otimiza o acesso a relacionamentos de objeto único
- `prefetch_related` reduz consultas repetidas em relacionamentos com vários objetos
- os logs ajudam a investigar erros executando a aplicação com Gunicorn
- ferramentas de depuração devem ser configuradas com cuidado em produção

Essas práticas ajudam a diagnosticar problemas e a manter aplicações Django mais eficientes e seguras.
