
# Ambientes de desenvolvimento — Django, Git e Windows

Breve guia prático com comandos e dicas para configurar ambiente local, Git/GitHub e checar o servidor Django.

## 1. Configurando chaves SSH, git e enviando o projeto para o Github

Passos essenciais:

- Gerar par de chaves SSH (se ainda não tiver):

```bash
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"
# ou, em sistemas onde ed25519 não é suportado:
ssh-keygen -t rsa -b 4096 -C "seu-email@exemplo.com"
```

- Copiar a chave pública e adicionar ao GitHub (Settings → SSH and GPG keys).

```bash
# Exibir chave pública (Windows PowerShell):
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

- Configurar o Git localmente:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

- Inicializar repositório, adicionar remote e enviar para o GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:seu-usuario/seu-repositorio.git
git push -u origin main
```

Observações:

- Use o remoto SSH (`git@github.com:...`) para evitar solicitações de credenciais repetidas.
- Se preferir HTTPS, crie um token de acesso pessoal e configure um helper de credenciais.

## 2. O nosso repositório e possíveis problemas no Windows

Problemas comuns no Windows e soluções:

- Finalizadores de linha (CRLF) — normalize com Git:

```bash
git config --global core.autocrlf true
```

- Caminhos longos — habilite suporte a caminhos longos no Windows 10/11 quando necessário.

- Virtualenv dentro do projeto — não comitar a venv; adicione-a ao `.gitignore`.

- Permissões e bloqueio de arquivos — feche IDEs/servidores que mantenham arquivos abertos antes de commits/builds.

- Segredos e configurações sensíveis — use variáveis de ambiente e arquivos `.env` (não versionar).

## 3. Um .gitignore exclusivo para Django e Python

Exemplo mínimo de `.gitignore` para projetos Django/Python:

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/
.venv/

# Django stuff
*.log
local_settings.py
db.sqlite3
media/

# VSCode
.vscode/

# PyCharm
.idea/

# Env files
.env

# Static files built
/staticfiles/

# macOS
.DS_Store
```

Adapte conforme suas necessidades (ex.: Docker, arquivos de build, outros IDEs).

## 4. Hello Django — verificação rápida do servidor de desenvolvimento

Passos rápidos para testar localmente:

1. Criar e ativar ambiente virtual:

```bash
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (cmd):
.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Aplicar migrações e criar superuser (opcional):

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Executar servidor de desenvolvimento:

```bash
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` no navegador para confirmar que o projeto está rodando.

Observações finais:

- Mantenha `requirements.txt` atualizado com:

```bash
pip freeze > requirements.txt
```

- Para produção, separe as configurações (use `DEBUG=False`, WSGI servers como Gunicorn, Nginx e/ou Docker). Consulte a seção de deploy quando existir.

---

Posso polir mais (ex.: adicionar links para guias, imagens, ou uma seção sobre Docker/CI). Diga o que prefere.

