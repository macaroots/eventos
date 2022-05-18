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

	bean = (titulo, data)
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
		evento = daoEventos.getById(id)

	return render_template('eventos/form.html', evento=evento, id=id)


@app.route('/inscricoes/listar')
def inscricoes_listar():
	inscricoes = daoInscricoes.list()
	
	return render_template('inscricoes/listar.html', inscricoes=inscricoes)

@app.route('/inscricoes/inserir', methods=['GET', 'POST'])
def inscricoes_inserir(id=0):
	nome = request.form.get('nome')
	email = request.form.get('email')
	evento = request.form.get('evento')

	usuario = (nome, email)
	idUsuario = daoUsuarios.insert(usuario)
	inscricao = (idUsuario, evento)
	id = daoInscricoes.insert(inscricao)

	return 'Cadastro realizado com sucesso!'

@app.route('/inscricoes/form/<id>', methods=['GET', 'POST'])
@app.route('/inscricoes/form', methods=['GET', 'POST'])
def inscricoes_form(id=0):
	eventos = daoEventos.list('id, titulo')

	return render_template('inscricoes/form.html', eventos=eventos)

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
