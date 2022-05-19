import datetime
from flask import render_template
from flask import request
from app import app
from app.dao import dao_mysql

daoEventos = dao_mysql.DAOEventos()
daoInscricoes = dao_mysql.DAOInscricoes()
daoUsuarios = dao_mysql.DAOUsuarios()

@app.route('/')
def teste():
	return render_template('site.html')


@app.route('/inscricoes/listar')
def inscricoes_listar():
	inscricoes = daoInscricoes.list('e.id, e.titulo, u.id, u.nome')
	
	return render_template('inscricoes/listar.html', inscricoes=inscricoes)

@app.route('/inscricoes/inserir/<idEvento>/<idUsuario>', methods=['GET', 'POST'])
def inscricoes_inserir(idEvento='0', idUsuario='0'):
	nome = request.form.get('nome')
	email = request.form.get('email')
	evento = request.form.get('evento')

	usuario = {
		'nome': nome, 
		'email': email
	}
	if idUsuario == '0':
		idUsuario = daoUsuarios.insert(usuario)
	else:
		daoUsuarios.update(usuario, idUsuario)
	inscricao = {
		'idUsuario': idUsuario,
		'idEvento': evento
	}
	if idEvento == '0':
		idInscricao = daoInscricoes.insert(inscricao)
		acao = 'cadastrado'
	else:
		acao = 'alterado'
		daoInscricoes.update(inscricao, idEvento, idUsuario)

	return 'Registro #({}, {}) {} com sucesso!'.format(idEvento, idUsuario, acao)

@app.route('/inscricoes/form/<idEvento>/<idUsuario>', methods=['GET', 'POST'])
@app.route('/inscricoes/form/', methods=['GET', 'POST'])
@app.route('/inscricoes/form', methods=['GET', 'POST'])
def inscricoes_form(idEvento='0', idUsuario='0'):
	print('form')
	if idEvento != '0':
		inscricao = daoInscricoes.findOne(idEvento, idUsuario, 'e.id as idEvento, e.titulo, u.id as idUsuario, u.nome, u.email')
		print('INSCRICAO', inscricao)
	else:
		inscricao = dict()

	eventos = daoEventos.list('id, titulo')

	return render_template('inscricoes/form.html', eventos=eventos, inscricao=inscricao, idEvento=idEvento, idUsuario=idUsuario)

@app.route('/submissoes/listar')
def submissoes_listar():
	return render_template('submissoes/listar.html')

@app.route('/submissoes/form', methods=['GET', 'POST'])
def submissoes_form():	
	eventos = daoEventos.list('id, titulo')
	usuarios = daoUsuarios.list('id, nome')
	
	return render_template('submissoes/form.html', eventos=eventos, usuarios=usuarios)

'''
class X:
	def __init__(self, name):
		self.name = name;
		print('/' + self.name + '/index2')
		
	def index(self):
		print(self.name)
		@app.route('/' + self.name + '/index2')
		def x():
			return 'oi, ' + self.name
		
x = X('oi')
y = X('tchau')
'''
