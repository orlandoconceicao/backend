# Ambiente de Desenvolvimento Python no macOS Monterey

## Objetivo

Configurar um ambiente completo para desenvolvimento com Python no macOS Monterey, preparando o sistema para criação de projetos utilizando frameworks como Django e Django REST Framework.

Ambiente configurado com:

- Homebrew
- Python
- Pip
- Ambiente Virtual
- Visual Studio Code
- Extensões de desenvolvimento
- Git
- Gerenciamento de dependências


# 1. Verificar o macOS

**Abrir o Terminal:**
```
Command + Espaço
```

**Pesquisar:**
```
Terminal
```

**Verificar versão do sistema:**
```bash
sw_vers
```

**Saída esperada:**
```
ProductName: macOS
ProductVersion: 12.x
```


# 2. Instalar Homebrew

O Homebrew será utilizado para instalar e gerenciar ferramentas de desenvolvimento.

**Executar script de instalação:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verificar instalação:**
```bash
brew --version
```

**Atualizar Homebrew:**
```bash
brew update
```


# 3. Instalar Python

**Instalar Python via Homebrew:**
```bash
brew install python
```

**Verificar instalação:**
```bash
python3 --version
```

**Saída esperada:**
```
Python 3.x.x
```

**Verificar localização:**
```bash
which python3
```


# 4. Instalar Pip

O Pip é o gerenciador de pacotes do Python.

**Verificar versão:**
```bash
pip3 --version
```

**Atualizar para versão mais recente:**
```bash
python3 -m pip install --upgrade pip
```


# 5. Instalar Visual Studio Code

**Download do site oficial:**
```
https://code.visualstudio.com/
```

Após instalar, abrir o VS Code.


# 6. Extensões do VS Code

Instalar as seguintes extensões:

## Python

Extensão oficial para suporte ao Python.

## Pylance

Adiciona recursos como:

- Autocomplete
- Análise de código
- Sugestões de erro

## Django

Suporte para projetos Django.


# 7. Configurar Terminal do VS Code

Abrir:

```
VS Code
```

Abrir terminal:

```
Terminal > New Terminal
```

Testar Python:

```bash
python3 --version
```


# 8. Instalar Git

**Verificar se Git está instalado:**
```bash
git --version
```

**Se não estiver instalado, usar Homebrew:**
```bash
brew install git
```

**Configurar usuário global:**
```bash
git config --global user.name "Seu Nome"
```

**Configurar email global:**
```bash
git config --global user.email "seu@email.com"
```


# 9. Criar Pasta de Projetos

**Criar diretório de projetos:**
```bash
mkdir projetos-python
```

**Entrar no diretório:**
```bash
cd projetos-python
```

**Abrir no VS Code:**
```bash
code .
```


# 10. Criar Ambiente Virtual

O ambiente virtual mantém as dependências dos projetos isoladas.

**Criar ambiente virtual:**
```bash
python3 -m venv venv
```

**Ativar ambiente:**
```bash
source venv/bin/activate
```

**Verificar ativação (prompt alterado):**
```
(venv) usuario@computador:~
```

**Desativar ambiente:**
```bash
deactivate
```


# 11. Atualizar Ferramentas do Ambiente

**Com o ambiente virtual ativado:**

**Atualizar pip:**
```bash
pip install --upgrade pip
```

**Atualizar ferramentas de compilação:**
```bash
pip install --upgrade setuptools wheel
```


# 12. Instalar Pacotes Python

**Formato geral para instalar pacotes:**
```bash
pip install nome-do-pacote
```

**Instalar Django:**
```bash
pip install django
```

**Instalar Django REST Framework:**
```bash
pip install djangorestframework
```

**Listar todos os pacotes instalados:**
```bash
pip list
```


# 13. Gerenciar Dependências

**Salvar lista de dependências:**
```bash
pip freeze > requirements.txt
```

**Instalar todas as dependências:**
```bash
pip install -r requirements.txt
```


# 14. Estrutura Recomendada de Projetos

**Organização principal:**
```
projetos-python/
├── projeto1/
├── projeto2/
└── estudos/
```

**Estrutura interna de um projeto Django:**
```
projeto/
├── venv/                    → ambiente virtual
├── src/                     → código-fonte
├── manage.py               → gerenciador Django
├── requirements.txt        → dependências
├── .gitignore              → arquivos ignorados
└── README.md               → documentação
```


# 15. Comandos Essenciais

**Versão do Python:**
```bash
python3 --version
```

**Versão do Pip:**
```bash
pip --version
```

**Listar pacotes instalados:**
```bash
pip list
```

**Instalar um pacote:**
```bash
pip install pacote
```

**Remover um pacote:**
```bash
pip uninstall pacote
```

**Criar ambiente virtual:**
```bash
python3 -m venv venv
```

**Ativar ambiente virtual:**
```bash
source venv/bin/activate
```

**Desativar ambiente virtual:**
```bash
deactivate
```

**Salvar dependências em arquivo:**
```bash
pip freeze > requirements.txt
```

**Instalar dependencias de arquivo:**
```bash
pip install -r requirements.txt
```

**Aplicar migrações do banco:**
```bash
python manage.py migrate
```

**Criar usuário administrador:**
```bash
python manage.py createsuperuser
```

**Executar servidor de desenvolvimento:**
```bash
python manage.py runserver
```


# Ambiente Final Configurado

Após finalizar todos os passos, o macOS Monterey estará preparado para desenvolvimento Python.

Configuração concluída:

- Python instalado
- Pip configurado
- Ambiente virtual funcionando
- Visual Studio Code instalado
- Extensões configuradas
- Git configurado
- Gerenciamento de dependências pronto
