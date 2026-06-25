# Ambiente de Desenvolvimento Python no Windows 11

## Objetivo

Configurar um ambiente completo para desenvolvimento com Python no Windows 11, preparando o sistema para criação de projetos utilizando frameworks como Django e Django REST Framework.

Ambiente configurado com:

- Python
- Pip
- Ambiente Virtual
- Visual Studio Code
- Extensões de desenvolvimento
- Git
- Gerenciamento de dependências


# 1. Verificar o Windows 11

Verificar a versão do sistema:

**Pressionar:**
```
Windows + R
```

**Executar:**
```
winver
```

Confirmar que o sistema está utilizando Windows 11.


# 2. Instalar Windows Terminal

O Windows Terminal será utilizado para executar comandos de desenvolvimento.

**Abrir:**
```
Microsoft Store
```

**Pesquisar:**
```
Windows Terminal
```

Instalar e abrir.

**Verificar PowerShell:**
```powershell
$PSVersionTable
```


# 3. Instalar Python

**Acessar o site:**
```
https://www.python.org/downloads/
```

Baixar a versão mais recente do Python para Windows.

**Durante a instalação, marcar:**
```
Add python.exe to PATH
```

**Depois selecionar:**
```
Install Now
```


# 4. Verificar Python

**Executar no PowerShell:**
```powershell
python --version
```

**Saída esperada:**
```
Python 3.x.x
```

**Verificar versão do Pip:**
```powershell
pip --version
```


# 5. Atualizar Pip

**Executar comando de atualização:**
```powershell
python -m pip install --upgrade pip
```

**Verificar versão atualizada:**
```powershell
pip --version
```


# 6. Instalar Visual Studio Code

**Download do site oficial:**
```
https://code.visualstudio.com/
```

**Durante a instalação, habilitar:**
```
Add to PATH
```

Abrir o VS Code após a instalação.


# 7. Extensões do VS Code

Instalar as seguintes extensões:

## Python

Suporte para desenvolvimento Python.

## Pylance

Recursos:

- Autocomplete
- Sugestões de código
- Análise de erros

## Django

Suporte para projetos Django.


# 8. Configurar Terminal do VS Code

**Abrir VS Code**

**Abrir terminal interno:**
```
Terminal > New Terminal
```

**Testar Python:**
```powershell
python --version
```


# 9. Instalar Git

**Download do site oficial:**
```
https://git-scm.com/downloads
```

**Verificar instalação:**
```powershell
git --version
```

**Configurar usuário global:**
```powershell
git config --global user.name "Seu Nome"
```

**Configurar email global:**
```powershell
git config --global user.email "seu@email.com"
```


# 10. Criar Pasta de Projetos

**Criar diretório de projetos:**
```powershell
mkdir projetos-python
```

**Entrar no diretório:**
```powershell
cd projetos-python
```

**Abrir no VS Code:**
```powershell
code .
```


# 11. Criar Ambiente Virtual

O ambiente virtual mantém as dependências dos projetos isoladas.

**Criar ambiente virtual:**
```powershell
python -m venv venv
```

**Ativar ambiente:**
```powershell
.\venv\Scripts\activate
```

**Verificar ativação (prompt alterado):**
```
(venv) C:\Users\...\
```

**Desativar ambiente:**
```powershell
deactivate
```


# 12. Atualizar Ferramentas do Ambiente

**Com o ambiente virtual ativado:**

**Atualizar pip:**
```powershell
pip install --upgrade pip
```

**Atualizar ferramentas de compilação:**
```powershell
pip install --upgrade setuptools wheel
```


# 13. Instalar Pacotes Python

**Formato geral para instalar pacotes:**
```powershell
pip install nome-do-pacote
```

**Instalar Django:**
```powershell
pip install django
```

**Instalar Django REST Framework:**
```powershell
pip install djangorestframework
```

**Listar todos os pacotes instalados:**
```powershell
pip list
```


# 14. Gerenciar Dependências

**Salvar lista de dependências:**
```powershell
pip freeze > requirements.txt
```

**Instalar todas as dependências:**
```powershell
pip install -r requirements.txt
```


# 15. Estrutura Recomendada de Projetos

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


# 16. Comandos Essenciais

**Versão do Python:**
```powershell
python --version
```

**Versão do Pip:**
```powershell
pip --version
```

**Listar pacotes instalados:**
```powershell
pip list
```

**Instalar um pacote:**
```powershell
pip install pacote
```

**Remover um pacote:**
```powershell
pip uninstall pacote
```

**Criar ambiente virtual:**
```powershell
python -m venv venv
```

**Ativar ambiente virtual:**
```powershell
.\venv\Scripts\activate
```

**Desativar ambiente virtual:**
```powershell
deactivate
```

**Salvar dependências em arquivo:**
```powershell
pip freeze > requirements.txt
```

**Instalar dependencias de arquivo:**
```powershell
pip install -r requirements.txt
```

**Aplicar migrações do banco:**
```powershell
python manage.py migrate
```

**Criar usuário administrador:**
```powershell
python manage.py createsuperuser
```

**Executar servidor de desenvolvimento:**
```powershell
python manage.py runserver
```


# Ambiente Final Configurado

Após finalizar todos os passos, o Windows 11 estará preparado para desenvolvimento Python.

Configuração concluída:

- Python instalado
- Pip configurado
- Ambiente virtual funcionando
- Visual Studio Code instalado
- Extensões configuradas
- Git configurado
- Gerenciamento de dependências pronto

Ambiente preparado para iniciar projetos com Python, Django e Django REST Framework.
```