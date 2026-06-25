# Guia de Instalação e Configuração do Visual Studio Code

## Objetivo

Instalar e configurar o Visual Studio Code (VS Code) para desenvolvimento Python/Django, com recomendações de extensões, configurações e boas práticas.

## Pré-requisitos

- Conexão com a internet
- Permissão de administrador para instalar software (quando necessário)


# 1. Download e Instalação

## Windows

**Baixar instalador:**
```
https://code.visualstudio.com/
```

Durante a instalação, marque: `Add to PATH` e `Add "Open with Code" action` para contextual menus.

## macOS

Baixar o .zip ou usar Homebrew:
```bash
brew install --cask visual-studio-code
```

## Linux (Ubuntu / Debian)

Baixar o pacote .deb ou usar repositório:
```bash
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code
```


# 2. Extensões Recomendadas

- **Python** — Suporte principal para Python
- **Pylance** — Análise estática e inteligência
- **Django** — Snippets e suporte a templates
- **GitLens** — Integração avançada de Git
- **Docker** — Se usar containers

Instalar via interface do VS Code (`Extensions` -> pesquisar) ou CLI:
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension batisteo.vscode-django
code --install-extension eamodio.gitlens
```


# 3. Configurações Úteis (settings.json)

Abra `Preferences: Open Settings (JSON)` e adicione recomendações:

```json
{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  },
  "python.pythonPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true
}
```

Notas:
- Em Windows, ajuste `python.pythonPath` para `"${workspaceFolder}\\venv\\Scripts\\python.exe"` quando usar venv local.
- Prefira formatadores como `black` ou `autopep8` instalados no venv.


# 4. Integração com Terminal e Ambiente Virtual

- Abra terminal integrado: `Terminal > New Terminal`.
- Se estiver usando `venv`, selecione o interpretador Python (Ctrl+Shift+P → `Python: Select Interpreter`) apontando para `./venv`.

Exemplo de seleção manual (Windows PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

Linux/macOS:
```bash
source venv/bin/activate
```


# 5. Depuração (Debug)

Exemplo básico de `launch.json` para Django:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "0.0.0.0:8000"],
      "django": true
    }
  ]
}
```


# 6. Atalhos e Produtividade

- Abrir paleta: `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS)
- Alternar terminal: `` Ctrl+` ``
- Formatar documento: `Shift+Alt+F`


# 7. Problemas Comuns e Soluções

- VS Code não encontra o interpretador Python: selecione manualmente com `Python: Select Interpreter`.
- Extensão Python lenta: instale `Pylance` e desative outras extensões conflitantes.
- Permissão para instalar extensões: execute o VS Code como administrador (Windows) ou use `sudo` para instalação via apt/cask.


# 8. Checklist Rápido

- [ ] VS Code instalado
- [ ] Extensões instaladas (Python, Pylance, Django)
- [ ] Interpreter apontando para `venv`
- [ ] Formatação e lint configurados


# Ambiente Final

VS Code configurado com extensões e preferências básicas para desenvolvimento Python/Django. Se quiser, eu posso adicionar um `settings.json` por workspace e um `launch.json` de exemplo dentro de um projeto específico.
