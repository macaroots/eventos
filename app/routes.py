import mysql.connector
import datetime
from flask import render_template
from flask import request
from app import app

def getConexao():
	conexao = mysql.connector.connect(
		host='localhost',
		user='root',
		password='admin',
		database='eventos'
	)
	return conexao

@app.route('/')
def teste():
	return render_template('site.html')

@app.route('/eventos/listar')
def eventos_listar():
	sql = "select id, titulo, data from eventos"
	
	conexao = getConexao()
	cursor = conexao.cursor()
	
	cursor.execute(sql)
	eventos = cursor.fetchall()
	
	cursor.close()
	conexao.close()
	
	return render_template('eventos/listar.html', eventos=eventos)

@app.route('/eventos/editar/<id>', methods=['GET', 'POST'])
def eventos_update(id):
	pass

@app.route('/eventos/apagar/<id>', methods=['GET', 'POST'])
def eventos_delete(id):
	pass
	
@app.route('/eventos/inserir', methods=['GET', 'POST'])
def eventos_inserir(id=0):
	titulo = request.form.get('titulo')
	data = request.form.get('data')

	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'insert into eventos (titulo, data) values (%s, %s)'
	cursor.execute(sql, (titulo, data))
	id = cursor.lastrowid
	conexao.commit()
	cursor.close()
	conexao.close()
	return 'Cadastro realizado com sucesso!'

@app.route('/eventos/cadastrar', methods=['GET', 'POST'])
@app.route('/eventos/cadastrar/<id>', methods=['GET', 'POST'])
def eventos_form(id=None):
	evento = {'data': datetime.datetime.now()}
	# id = request.args.get('id')
	if id is not None:
		conexao = getConexao()
		cursor = conexao.cursor(dictionary=True)
		
		sql = 'select * from eventos where id=%s'
		cursor.execute(sql, (id, ))
		evento = cursor.fetchone()
		
		cursor.close()
		conexao.close()
	return render_template('eventos/cadastrar.html', evento=evento)


@app.route('/inscricoes/listar')
def inscricoes_listar():
	sql = 'select e.titulo, u.nome from eventos e join inscricoes i on e.id=i.eventos_id join usuarios u on u.id=i.usuarios_id'
	
	conexao = getConexao()
	cursor = conexao.cursor()
	
	cursor.execute(sql)
	inscricoes = cursor.fetchall()
	
	cursor.close()
	conexao.close()
	
	return render_template('inscricoes/listar.html', inscricoes=inscricoes)

@app.route('/inscricoes/inserir', methods=['GET', 'POST'])
def inscricoes_inserir(id=0):
	nome = request.form.get('nome')
	email = request.form.get('email')
	evento = request.form.get('evento')

	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'insert into usuarios (nome, email) values (%s, %s)'
	cursor.execute(sql, (nome, email))
	id = cursor.lastrowid
	sql = 'insert into inscricoes (usuarios_id, eventos_id) values (%s, %s)'
	cursor.execute(sql, (id, evento))
	
	conexao.commit()
	cursor.close()
	conexao.close()
	return 'Cadastro realizado com sucesso!'

@app.route('/inscricoes/editar/<id>', methods=['GET', 'POST'])
@app.route('/inscricoes/cadastrar', methods=['GET', 'POST'])
def inscricoes_form(id=0):
	sql = "select id, titulo from eventos"
	
	conexao = getConexao()
	cursor = conexao.cursor()
	
	cursor.execute(sql)
	eventos = cursor.fetchall()
	
	cursor.close()
	conexao.close()
	return render_template('inscricoes/cadastrar.html', eventos=eventos)

@app.route('/submissoes/listar')
def submissoes_listar():
	return render_template('submissoes/listar.html')

@app.route('/submissoes/cadastrar', methods=['GET', 'POST'])
def submissoes_form():
	conexao = getConexao()
	cursor = conexao.cursor()
	
	sql = "select id, titulo from eventos"
	cursor.execute(sql)
	eventos = cursor.fetchall()
	sql = "select id, nome from usuarios"
	cursor.execute(sql)
	usuarios = cursor.fetchall()
	
	cursor.close()
	conexao.close()
	return render_template('submissoes/cadastrar.html', eventos=eventos, usuarios=usuarios)

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
