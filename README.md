# eventos
CRUD com Python + Flask

## Executar no próprio computador
Criar um ambiente virtual
  > python3 -m venv venv

Ativar o ambiente virtual
  
  No Linux:
  > . venv/bin/activate
  
  No Windows:
  > venv\Scripts\activate

Instalar o Flask
  > pip install flask

Instalar o conector MySQL
  > pip install mysql-connector-python

Executar o Flask
  > flask run

## Executar pelo Docker
1. Criar arquivo ```.env```:
```
MYSQL_ROOT_PASSWORD=admin
MYSQL_USER=teste
MYSQL_PASSWORD=123
MYSQL_DATABASE=leajs

MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=admin

FLASK_DEBUG=1
```

2. Ligar o Docker
  > docker-compose up

## Acessar
 > http://localhost:5000