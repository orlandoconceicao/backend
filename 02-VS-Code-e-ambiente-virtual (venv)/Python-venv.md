# Guia: Criar e Usar `venv` (Ambiente Virtual Python)

## Objetivo

Explicar como criar, ativar, configurar e usar ambientes virtuais Python com `venv` em Windows, macOS e Linux, seguindo boas práticas.

## Pré-requisitos

- Python 3.6+ instalado (`python` ou `python3`)
- Acesso ao terminal / PowerShell


# 1. Por que usar `venv`?

- Isola dependências por projeto
- Evita conflitos entre versões de pacotes
- Facilita reprodução do ambiente (requirements.txt)


# 2. Criar um ambiente virtual

## Linux / macOS

**Criar:**
```bash
python3 -m venv venv
```

**Ativar:**
```bash
source venv/bin/activate
```

**Prompt esperado:**
```
(venv) usuario@maquina:~/projeto$
```

## Windows (PowerShell)

**Criar:**
```powershell
python -m venv venv
```

**Ativar (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Ativar (cmd.exe):**
```cmd
.\venv\Scripts\activate.bat
```

**Prompt esperado:**
```
(venv) C:\Users\SeuUser\projeto>
```


# 3. Atualizar pip e ferramentas básicas

Com venv ativado:

```bash
pip install --upgrade pip
pip install --upgrade setuptools wheel
```

Instalar formater/linter (exemplo):

```bash
pip install black flake8
```


# 4. Trabalhar com dependências

**Instalar pacotes:**
```bash
pip install django djangorestframework
```

**Salvar dependências:**
```bash
pip freeze > requirements.txt
```

**Instalar a partir do arquivo:**
```bash
pip install -r requirements.txt
```


# 5. Integrar `venv` com VS Code

- Abra o workspace no VS Code
- `Ctrl+Shift+P` → `Python: Select Interpreter` → escolha `./venv`/`Scripts` correspondente
- Adicionar configuração de workspace (exemplo `.vscode/settings.json`):

```json
{
  "python.pythonPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true
}
```

(Em Windows use `"${workspaceFolder}\\venv\\Scripts\\python.exe"`)


# 6. Boas práticas

- Adicione `venv/` ao `.gitignore`:
```
venv/
__pycache__/
*.pyc
```
- Sempre ativar o `venv` antes de instalar pacotes
- Use `requirements.txt` ou `pip-tools` para reproduzir ambientes


# 7. Remover ambiente virtual

Basta excluir a pasta `venv/`:

```bash
rm -rf venv
```
(Windows: deletar pasta via Explorer ou `rmdir /s venv`)


# 8. Solução de Problemas Comuns

- Erro `venv` não encontrado: instale o pacote do sistema (Ubuntu):
```bash
sudo apt install python3-venv
```
- PowerShell bloqueia execução de scripts: execute como administrador e rode:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- VS Code não detecta o venv: certifique-se de que `python.pythonPath` aponta para o interpretador dentro de `venv`.


# 9. Checklist Rápido

- [ ] `venv` criado
- [ ] `venv` ativado
- [ ] `pip` atualizado
- [ ] Dependências salvas em `requirements.txt`


# Ambiente Final

Com `venv` configurado, seu projeto fica isolado e reproduzível. Posso adicionar exemplos de `requirements.txt` ou um `Makefile` para automatizar comandos se desejar.
