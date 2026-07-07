from django.contrib import admin
from django.urls import path
from views import home, sobre, contato


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home') significa:
    # - URL vazia '' = página inicial
    # - home = função que responde quando o navegador acessa /
    # - name='home' = nome da rota para usar em templates ou reverse()
    path('', home, name='home'),
    # path('sobre/', sobre, name='sobre') significa:
    # - /sobre/ = caminho da URL
    # - sobre = função que responde essa rota
    # - name='sobre' = nome da rota
    path('sobre/', sobre, name='sobre'),
    # path('contato/', contato, name='contato') significa:
    # - /contato/ = caminho da URL
    # - contato = função que responde essa rota
    # - name='contato' = nome da rota
    path('contato/', contato, name='contato'),
]

"""
Explicação do código:
- request: objeto que carrega informações da requisição do navegador.
- response: objeto HttpResponse que o Django envia de volta.
- status: código HTTP que indica sucesso (200) ou erro (405).
- method: tipo de requisição HTTP, como GET ou POST.

A rota path('sobre/', sobre, name='sobre') funciona assim:
- O navegador acessa /sobre/.
- O Django busca essa rota em urlpatterns.
- Ele chama a função sobre(request).
- A função decide a resposta e retorna HttpResponse.

Status codes padrão explicados:
- 200 = OK: tudo certo, a página foi exibida.
- 404 = Not Found: o endereço não existe no site.
- 405 = Method Not Allowed: o endereço existe, mas o método HTTP não é aceito.
- 500 = Internal Server Error: erro no servidor ou no código do site.
"""