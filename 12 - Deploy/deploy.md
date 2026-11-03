# Deploy no Django

Este módulo reúne os principais passos para publicar uma aplicação Django em produção, configurando servidor, banco de dados, domínio, HTTPS e deploy automatizado.

A ideia central é levar a aplicação do ambiente local para um ambiente acessível pela internet, com segurança e organização.

---

## 1. Avisos e dicas: Deploy, Hospedagem e domínio e opções inclusivas para todos

Antes de publicar a aplicação, é importante entender os cuidados envolvidos em deploy, hospedagem e domínio.

### Pontos importantes

- escolher uma hospedagem adequada ao projeto
- entender o custo e os limites do ambiente
- garantir segurança da aplicação em produção
- pensar em acessibilidade e boas práticas de infraestrutura
- considerar opções inclusivas e sustentáveis para diferentes perfis de usuários

Em produção, o objetivo não é só colocar o projeto online, mas deixar a aplicação estável, segura e funcional.

---

## 2. Ajustando as configurações de `DATABASES` e `.env` da nossa aplicação

Quando a aplicação sai do ambiente local, as configurações de banco e ambiente precisam ser ajustadas.

### O que geralmente muda

- nome do banco de dados
- usuário e senha
- host do banco
- porta
- variáveis sensíveis em arquivo `.env`

### Exemplo de configuração

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
```

O `.env` ajuda a manter informações sensíveis fora do código-fonte.

---

## 3. Configurando o `ALLOWED_HOSTS` e o `DEBUG` para publicação do app

Em produção, é necessário ajustar algumas configurações essenciais do Django.

### `DEBUG`

O `DEBUG` deve ser `False` em produção, pois ele expõe informações internas do projeto em caso de erro.

### `ALLOWED_HOSTS`

Essa configuração define quais domínios e IPs podem acessar a aplicação.

```python
ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com', 'ip-do-servidor']
```

Sem isso, o Django pode bloquear requisições em ambiente de produção.

---

## 4. Criando um servidor Linux na Google Cloud Platform e configurando SSH

A hospedagem pode ser feita em servidores na nuvem.

### Passos básicos

- criar uma instância Linux na GCP
- selecionar sistema operacional compatível
- configurar regras de firewall
- gerar ou importar chaves SSH
- conectar ao servidor remotamente

A conexão por SSH permite administrar o servidor com segurança e controle.

---

## 5. Instalando os pacotes necessários no servidor

No servidor, é preciso instalar as dependências do ambiente de execução da aplicação.

### Exemplos de pacotes comuns

- Python
- pip
- virtualenv
- git
- PostgreSQL client
- bibliotecas do sistema
- `gunicorn`
- `psycopg2`

Esses itens são fundamentais para que o projeto rode corretamente em produção.

---

## 6. Configurando o PostgreSQL e o Git no servidor

O banco de dados em produção geralmente é um serviço separado e mais robusto que o SQLite usado em desenvolvimento.

### PostgreSQL

- criar banco
- criar usuário
- configurar senha
- permitir conexão local ou pela aplicação

### Git

O Git será usado para sincronizar o código do repositório com o servidor.

Em deploy, isso ajuda a manter o projeto versionado e facilitar a atualização.

---

## 7. Criando os repositórios da aplicação e bare

Uma estrutura comum em deploy é ter:

- repositório principal da aplicação
- repositório `bare` para receber o código
- diretório de publicação para execução da aplicação

### Repositório `bare`

Ele serve como ponto central para receber atualizações via git.

### Fluxo comum

1. criar o repositório remoto no servidor
2. fazer `git push` para esse repositório
3. atualizar o código da aplicação pela máquina de produção

Essa estratégia facilita a publicação e manutenção do projeto.

---

## 8. Criando `unix.socket` e configurando o Gunicorn

O Gunicorn é um servidor WSGI usado para servir aplicações Django em produção.

### `unix.socket`

Um socket Unix permite que o Nginx fale com o Gunicorn de forma eficiente e segura.

### Objetivo

- receber requisições da web
- executar a aplicação Django
- tratar múltiplas conexões

O uso do Gunicorn é uma das formas mais comuns de deploy Django em produção.

---

## 9. Criando os arquivos de configuração do Nginx

O Nginx atua como servidor web frontal, encaminhando requisições para o Gunicorn.

### Funções do Nginx

- receber tráfego HTTP/HTTPS
- servir arquivos estáticos
- redirecionar requisições para a aplicação
- melhorar performance e estabilidade

As configurações incluem geralmente:

- `server_name`
- `location /`
- proxy para o socket do Gunicorn
- diretórios de arquivos estáticos

---

## 10. Adição de arquivos estáticos e sincronização do Git + `.gitignore`

Em produção, arquivos estáticos como CSS, JS, imagens e uploads precisam ser organizados corretamente.

### O que fazer

- coletar os arquivos estáticos com `collectstatic`
- configurar diretórios corretos
- ignorar arquivos locais desnecessários via `.gitignore`
- manter sensíveis fora do controle do repositório

Isso deixa o deploy mais limpo e evita problemas de sincronização.

---

## 11. Primeiro acesso para a nossa aplicação (`createsuperuser`)

Depois de publicar a aplicação, é hora de criar o primeiro usuário administrador.

```bash
python manage.py createsuperuser
```

Esse passo permite:

- acessar o painel administrativo do Django
- testar o sistema em produção
- verificar se o deploy está funcionando corretamente

---

## 12. Conversa sobre domínios e HTTPS (SSL)

Depois que a aplicação está funcionando, é comum configurar um domínio e ativar HTTPS.

### Domínio

O domínio é o endereço do projeto na internet, por exemplo:

```text
meudominio.com
```

### HTTPS

HTTPS protege as conexões com criptografia SSL/TLS, aumentando segurança e confiabilidade.

Essa etapa é essencial para aplicações reais.

---

## 13. Redirecionando um registro DNS tipo A para o IP do servidor (subdomínio)

Para acessar a aplicação através de um domínio, o DNS precisa apontar para o IP do servidor.

### Registro tipo A

Esse tipo de registro conecta um domínio ou subdomínio ao endereço IP do servidor.

Exemplo:

```text
app.meudominio.com -> IP do servidor
```

Isso faz com que o navegador encontre a aplicação corretamente.

---

## 14. Configurando um certificado SSL para HTTPS com a Let's Encrypt

O Let's Encrypt é uma forma gratuita e automatizada de gerar certificados SSL.

### Benefícios

- HTTPS habilitado
- navegação segura
- melhor reputação do projeto
- compatibilidade com browsers modernos

Com a configuração correta, o Nginx passa a servir a aplicação via HTTPS e redireciona o tráfego em segurança.

---

## 15. Fazendo alterações do local para o servidor de maneira simples e rápida

Depois do deploy inicial, pequenos ajustes precisam ser feitos frequentemente.

### Estratégia prática

- editar em ambiente local
- commitar no Git
- fazer push para o repositório do servidor
- atualizar a aplicação em produção

Isso deixa o processo de manutenção mais simples e organizado, sem depender de ações manuais complexas.

---

## Conclusão

O deploy é o momento em que a aplicação passa a ser acessada em ambiente real.

Ao longo deste módulo, você aprende que:

- a configuração do ambiente é crucial
- o Django precisa de ajustes específicos para produção
- banco de dados, domínio, SSL e servidor são partes fundamentais
- o Nginx e o Gunicorn ajudam a servir a aplicação de forma estável
- o Git organiza a entrega e atualização da aplicação

Esse conjunto de passos é essencial para transformar um projeto local em uma aplicação disponível para uso real.
