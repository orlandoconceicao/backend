# Página de Receitas

Aplicação web desenvolvida com Django para cadastrar e consultar receitas organizadas por categoria.

## Sobre o projeto

O projeto apresenta somente as receitas marcadas como publicadas. A página inicial lista os registros mais recentes, enquanto as rotas de categoria e detalhe permitem navegar pelo conteúdo cadastrado. Receitas, categorias e autores são administrados pelo Django Admin.

## Funcionalidades

- listagem de receitas publicadas;
- filtro de receitas por categoria;
- página de detalhes de cada receita;
- cadastro administrativo de receitas e categorias;
- suporte a imagem de capa, tempo de preparo, porções e etapas de preparação.

## Tecnologias

- Python
- Django 6
- SQLite
- Django Templates
- HTML e CSS
- Pillow para processamento de imagens

## Estrutura

```text
pagina-de-receitas/
|-- config/             # Configurações e URLs do projeto Django
|-- recipes_page/       # Models, views, rotas, templates e administração
|-- base_static/        # Arquivos CSS globais
|-- utils/              # Utilitários para dados de receitas
|-- manage.py
`-- requirements.txt
```

## Como executar

Crie um ambiente virtual, instale as dependências e prepare o banco de dados:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

A aplicação ficará disponível em `http://127.0.0.1:8000/`. O painel administrativo pode ser acessado em `/admin/` após a criação de um superusuário com `python manage.py createsuperuser`.

## Testes

O projeto possui a estrutura inicial de testes do Django, mas ainda não contém casos automatizados implementados.

## Autor

**Orlando Conceição Vilhalba de Almeida**

Desenvolvedor Backend em formação, com foco em Python, Django, Django REST Framework, PostgreSQL, APIs REST e Docker, utilizando React como tecnologia complementar para integração das aplicações.

GitHub: https://github.com/orlandoconceicao

LinkedIn: https://www.linkedin.com/in/orlando-concei%C3%A7%C3%A3o-582234315

Portfólio: https://orlandoconceicao.github.io/
