import datetime
from flask import render_template
from flask import request
from app import app

# Escolha o DAO, tirando ou colocando # na linha 7. Com #: Mongo. Sem #: Mysql.
#'''
from app.dao import dao_mongo
daoEventos = dao_mongo.DAO('eventos')
'''
from app.dao import dao_mysql
daoEventos = dao_mysql.DAOEventos()
''' #'''

@app.route('/eventos/listar')
def eventos_listar():
    eventos = daoEventos.list('id, titulo, data')
    
    return render_template('eventos/listar.html', eventos=eventos)

@app.route('/eventos/apagar/<id>', methods=['GET', 'POST'])
def eventos_delete(id):
    daoEventos.delete(id)

    return 'Registro #{} apagado com sucesso!'.format(id)
    
@app.route('/eventos/inserir/', methods=['GET', 'POST'])
@app.route('/eventos/inserir/<id>', methods=['GET', 'POST'])
def eventos_inserir(id='0'):
    titulo = request.form.get('titulo')
    data = request.form.get('data')

    bean = {
        'titulo': titulo, 
        'data': data
    }
    if id == '0':
        id = daoEventos.insert(bean)
        acao = 'cadastrado'
    else:
        acao = 'alterado'
        daoEventos.update(bean, id)

    return 'Registro #{} {} com sucesso!'.format(id, acao)

@app.route('/eventos/form', methods=['GET', 'POST'])
@app.route('/eventos/form/<id>', methods=['GET', 'POST'])
def eventos_form(id='0'):
    evento = {'data': datetime.datetime.now()}
    # id = request.args.get('id')
    if id != '0':
        evento = daoEventos.findOne(id)

    return render_template('eventos/form.html', evento=evento, id=id)