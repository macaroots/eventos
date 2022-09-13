from flask import Flask

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

# Escolha o DAO, tirando ou colocando # na linha 7. Com #: Mongo. Sem #: Mysql.
'''
from app.dao import dao_mongo
daoEventos = dao_mongo.DAO('eventos')
'''
from app.dao import dao_mysql
daoEventos = dao_mysql.DAOEventos()
''' #'''

from app.dao import dao_mysql
daoInscricoes = dao_mysql.DAOInscricoes()
daoUsuarios = dao_mysql.DAOUsuarios()

from app import routes
# from app import routesEventos

from app.controller import crud
controllerEventos = crud.CrudEventos(daoEventos)
controllerEventos.registerEndpoints('/eventos/')

controllerUsuario = crud.CrudUsuario(daoUsuarios)
controllerUsuario.registerEndpoints('/usuarios/')