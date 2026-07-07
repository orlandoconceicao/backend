from django.http import HttpResponse


def home(request):
    # As views recebem o pedido do navegador e retornam a resposta.
    # Aqui estamos aceitando apenas requisições GET para a página inicial.
    if request.method == 'GET':
        return HttpResponse('Bem-vindo à página inicial!', status=200)
    return HttpResponse('Método não permitido', status=405)


def sobre(request):
    # Esta view mostra o texto da página Sobre apenas quando o método é GET.
    if request.method == 'GET':
        return HttpResponse('Esta é a página Sobre!', status=200)
    return HttpResponse('Método não permitido', status=405)


def contato(request):
    # A view de contato também só responde a GET neste exemplo simples.
    if request.method == 'GET':
        return HttpResponse('Esta é a página de Contato!', status=200)
    return HttpResponse('Método não permitido', status=405)


"""
Notas sobre este arquivo:
- request é o objeto que contém os dados enviados pelo navegador.
- HttpResponse cria a resposta que volta para o usuário.
- status=200 significa que a página foi entregue com sucesso.
- status=405 indica que o método HTTP usado não é aceito pela view.

Como o Django lida com isso:
1. O navegador acessa uma URL.
2. O Django consulta o arquivo de rotas (urls.py).
3. Quando encontra a rota, ele executa a view correspondente.
4. A view devolve um HttpResponse com o conteúdo.

Use este padrão para outras páginas: definir a lógica da view no arquivo de views,
 e deixar as rotas no arquivo de URL somente para apontar para essas funções.
"""
