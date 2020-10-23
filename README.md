# youtube-description-mass-editor
Projeto para editar descrições em massa de vídeos no Youtube

Intasle as dependencias com:

```
pip intall -r requirements.txt
```

Para utilizar, cria um arquivo `.env` na raiz do projeto.

Use o arquivo contrib/env-sample como template

Cria uma chave de API no Google console conforme instruções em:
https://developers.google.com/youtube/v3/quickstart/python

Copie esse valor para a variável API_KEY do seu arqui .env

Crie o arquivo Json de credenciais. Use o tipo desktop, pois não há mais tipo "Other" como diz a documentação do Google.

Renomeie o arquivo para `client_secret.json` e compie na raiz do projeto
