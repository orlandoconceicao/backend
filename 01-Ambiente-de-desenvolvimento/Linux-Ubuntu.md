# Ambiente de Desenvolvimento Python no Linux Ubuntu

## Objetivo

Configurar um ambiente completo para desenvolvimento com Python no Linux Ubuntu, preparando o sistema para criação de projetos utilizando frameworks como Django e Django REST Framework.

Ambiente configurado com:

- Gestor de pacotes (apt)
- Python
- Pip
- Ambiente Virtual
- Visual Studio Code
- Extensões de desenvolvimento
- Git
- Gerenciamento de dependências


# 1. Verificar o Ubuntu

**Abrir o Terminal:**
```bash
Ctrl + Alt + T
```

**Verificar versão do sistema:**
```bash
lsb_release -a
```

**Saída esperada:**
```
Distributor ID: Ubuntu
Release: 22.04
Codename: jammy
```


# 2. Atualizar o Sistema

**Atualizar lista de pacotes:**
```bash
sudo apt update
```

**Atualizar pacotes instalados:**
```bash
sudo apt upgrade
```

**Limpar cache de pacotes:**
```bash
sudo apt autoclean
```


# 3. Instalar Python

**Instalar Python 3:**
```bash
sudo apt install python3
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

**Instalar Pip:**
```bash
sudo apt install python3-pip
```

**Verificar versão:**
```bash
pip3 --version
```

**Atualizar para versão mais recente:**
```bash
python3 -m pip install --upgrade pip
```


# 5. Instalar Ferramentas Adicionais

**Instalar venv (para ambientes virtuais):**
```bash
sudo apt install python3-venv
```

**Instalar build-essential (compilador C):**
```bash
sudo apt install build-essential
```


# 6. Instalar Visual Studio Code

**Download do site oficial:**
```
https://code.visualstudio.com/download
```

**Instalar dependências:**
```bash
sudo apt install software-properties-common apt-transport-https
```

**Adicionar chave GPG:**
```bash
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
```

**Adicionar repositório VS Code:**
```bash
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
```

**Atualizar e instalar:**
```bash
sudo apt update
sudo apt install code
```


# 7. Extensões do VS Code

Instalar as seguintes extensões:

## Python

Extensão oficial para suporte ao Python.

## Pylance

Recursos:

- Autocomplete
- Sugestões de código
- Análise de erros

## Django

Suporte para projetos Django.


# 8. Configurar Terminal do VS Code

**Abrir VS Code:**

**Abrir terminal interno:**
```
Terminal > New Terminal
```

**Testar Python:**
```bash
python3 --version
```


# 9. Instalar Git

**Instalar Git:**
```bash
sudo apt install git
```

**Verificar instalação:**
```bash
git --version
```

**Configurar usuário global:**
```bash
git config --global user.name "Seu Nome"
```

**Configurar email global:**
```bash
git config --global user.email "seu@email.com"
```


# 10. Criar Pasta de Projetos

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


# 11. Criar Ambiente Virtual

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
(venv) usuario@computador:~$
```

**Desativar ambiente:**
```bash
deactivate
```


# 12. Atualizar Ferramentas do Ambiente

**Com o ambiente virtual ativado:**

**Atualizar pip:**
```bash
pip install --upgrade pip
```

**Atualizar ferramentas de compilação:**
```bash
pip install --upgrade setuptools wheel
```


# 13. Instalar Pacotes Python

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


# 14. Gerenciar Dependências

**Salvar lista de dependências:**
```bash
pip freeze > requirements.txt
```

**Instalar todas as dependências:**
```bash
pip install -r requirements.txt
```


# 15. Estrutura Recomendada de Projetos

```
projetos-python/

├── projeto1/
│
├── projeto2/
│
└── estudos/
```

Estrutura interna de um projeto:

```
projeto/

├── venv/
├── src/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```


# 16. Comandos Essenciais

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

Após finalizar todos os passos, o Linux Ubuntu estará preparado para desenvolvimento Python.

Configuração concluída:

- Python instalado
- Pip configurado
- Ambiente virtual funcionando
- Visual Studio Code instalado
- Extensões configuradas
- Git configurado
# Ambiente de Desenvolvimento Python no Linux Ubuntu

## Objetivo

Configurar um ambiente completo para desenvolvimento com Python no Linux Ubuntu, preparando o sistema para criação de projetos utilizando frameworks como Django e Django REST Framework.

Ambiente configurado com:

- Gestor de pacotes (apt)
- Python
- Pip
- Ambiente Virtual
- Visual Studio Code
- Extensões de desenvolvimento
- Git
- Gerenciamento de dependências


# 1. Verificar o Ubuntu

**Abrir o Terminal:**
```bash
Ctrl + Alt + T
```

**Verificar versão do sistema:**
```bash
lsb_release -a
```

**Saída esperada:**
```
Distributor ID: Ubuntu
Release: 22.04
Codename: jammy
```


# 2. Atualizar o Sistema

**Atualizar lista de pacotes:**
```bash
sudo apt update
```

**Atualizar pacotes instalados:**
```bash
sudo apt upgrade
```

**Limpar cache de pacotes:**
```bash
sudo apt autoclean
```


# 3. Instalar Python

**Instalar Python 3:**
```bash
sudo apt install python3
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

**Instalar Pip:**
```bash
sudo apt install python3-pip
```

**Verificar versão:**
```bash
pip3 --version
```

**Atualizar para versão mais recente:**
```bash
python3 -m pip install --upgrade pip
```


# 5. Instalar Ferramentas Adicionais

**Instalar venv (para ambientes virtuais):**
```bash
sudo apt install python3-venv
```

**Instalar build-essential (compilador C):**
```bash
sudo apt install build-essential
```


# 6. Instalar Visual Studio Code

**Download do site oficial:**
```
https://code.visualstudio.com/download
```

**Instalar dependências:**
```bash
sudo apt install software-properties-common apt-transport-https
```

**Adicionar chave GPG:**
```bash
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
```

**Adicionar repositório VS Code:**
```bash
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
```

**Atualizar e instalar:**
```bash
sudo apt update
sudo apt install code
```


# 7. Extensões do VS Code

Instalar as seguintes extensões:

## Python

Extensão oficial para suporte ao Python.

## Pylance

Recursos:

- Autocomplete
- Sugestões de código
- Análise de erros

## Django

Suporte para projetos Django.


# 8. Configurar Terminal do VS Code

**Abrir VS Code:**

**Abrir terminal interno:**
```
Terminal > New Terminal
```

**Testar Python:**
```bash
python3 --version
```


# 9. Instalar Git

**Instalar Git:**
```bash
sudo apt install git
```

**Verificar instalação:**
```bash
git --version
```

**Configurar usuário global:**
```bash
git config --global user.name "Seu Nome"
```

**Configurar email global:**
```bash
git config --global user.email "seu@email.com"
```


# 10. Criar Pasta de Projetos

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


# 11. Criar Ambiente Virtual

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
(venv) usuario@computador:~$
```

**Desativar ambiente:**
```bash
deactivate
```


# 12. Atualizar Ferramentas do Ambiente

**Com o ambiente virtual ativado:**

**Atualizar pip:**
```bash
pip install --upgrade pip
```

**Atualizar ferramentas de compilação:**
```bash
pip install --upgrade setuptools wheel
```


# 13. Instalar Pacotes Python

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


# 14. Gerenciar Dependências

**Salvar lista de dependências:**
```bash
pip freeze > requirements.txt
```

**Instalar todas as dependências:**
```bash
pip install -r requirements.txt
```


# 15. Estrutura Recomendada de Projetos

```
projetos-python/

├── projeto1/
│
├── projeto2/
│
└── estudos/
```

Estrutura interna de um projeto:

```
projeto/

├── venv/
├── src/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```


# 16. Comandos Essenciais

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

Após finalizar todos os passos, o Linux Ubuntu estará preparado para desenvolvimento Python.

Configuração concluída:

- Python instalado
- Pip configurado
- Ambiente virtual funcionando
- Visual Studio Code instalado
- Extensões configuradas
- Git configurado
- Gerenciamento de dependências pronto

Ambiente preparado para iniciar projetos com Python, Django e Django REST Framework.
