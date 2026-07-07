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
