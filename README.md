# Backend - Gefin

No termina:

1. Instale um gerenciador de ambientes virtuais para python (usarei o virtualenv como exemplo)
1. Crie um ambiente virtual: `virtualenv env`
1. Ative ele: `source env/bin/activate`
1. Certifique-se que a versão do python é a *3.10.5*: `python3 --version`
1. Atualize o pip: `pip install --upgrade pip` (Caso você não tenha o pip, instale ele)
1. Instale os pacotes necessários para rodar o projeto: `pip install -r requirements.txt`

Agora, você deve ter um ambiente virtual _env_ com todos os pacotes necessários para rodar o projeto instalados. Toda vez que você precisar rodar o projeto, lembre-se de ativar este ambiente virtual! 

Para rodar o servidor de desenvolvimento:
1. Navegue até a pasta em que está o arquivo _manage.py_ : `cd gefinback`
1. Rode os comandos: 

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
