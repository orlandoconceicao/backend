# Arquivos iniciais de um projeto Django

Quando você cria um projeto Django, a estrutura inicial já vem com alguns arquivos importantes. Abaixo está a explicação de cada um, organizando-os pela pasta onde aparecem.

## 1. Na raiz do projeto

### manage.py
- É o arquivo principal para executar comandos do Django.
- Com ele você roda o servidor local, cria apps, faz migrações e muito mais.
- Exemplo:
  ```bash
  python manage.py runserver
  ```

## 2. Dentro da pasta principal do projeto

Normalmente, o nome da pasta principal é o mesmo do projeto, por exemplo, `meu_projeto/`.

### __init__.py
- Indica que a pasta é um pacote Python.
- Permite que o Django trate essa pasta como parte do projeto.

### settings.py
- Contém as configurações do projeto.
- Aqui ficam informações como:
  - aplicativos instalados;
  - banco de dados;
  - idioma e fuso horário;
  - arquivos estáticos.

### urls.py
- Define as rotas principais do projeto.
- É nele que você diz quais URLs vão chamar quais páginas ou views.

### wsgi.py
- Serve para a integração do projeto com servidores Web compatíveis com WSGI.
- É usado quando o projeto é colocado em produção.

### asgi.py
- Serve para a integração com servidores assíncronos usando ASGI.
- É importante para aplicações mais modernas e assíncronas.

## Estrutura inicial típica

```bash
meu_projeto/
├── manage.py
└── meu_projeto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Resumo rápido
- `manage.py` = controla o projeto.
- `settings.py` = configura o projeto.
- `urls.py` = define as rotas.
- `wsgi.py` e `asgi.py` = conectam o projeto ao servidor.
- `__init__.py` = transforma a pasta em pacote Python.

## Requisições HTTP comuns

No Django, as views recebem requisições HTTP e retornam respostas. Os métodos HTTP mais usados são:

- `GET`: pede dados do servidor. É usado para mostrar páginas e ler informações.
- `POST`: envia dados ao servidor. É usado em formulários e para criar ou atualizar informações.
- `PUT`: atualiza um registro inteiro no servidor.
- `PATCH`: atualiza apenas parte de um registro.
- `DELETE`: apaga um recurso no servidor.
- `HEAD`: igual ao GET, mas só pede os cabeçalhos da resposta, sem o corpo.

No código Django, você pode checar o método em `request.method`:

```python
if request.method == 'GET':
    # mostra a página
elif request.method == 'POST':
    # processa dados enviados pelo formulário
```

No exemplo do arquivo `URLs.py`, usamos `GET` para permitir só a leitura da página e retornamos `405` quando outro método foi enviado.
