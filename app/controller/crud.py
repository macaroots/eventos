import datetime
from flask import render_template
from flask import request
from app import app

class Crud:
    def __init__(self, dao, viewFolder='crud'):
        self.dao = dao
        self.viewFolder = viewFolder
    def registerEndpoints(self, context='/'):
        print('REGISTER', self.list, flush=True)
        app.add_url_rule(f'{context}listar', view_func=self.list)
        app.add_url_rule(f'{context}delete/<id>', view_func=self.delete)

        app.add_url_rule(f'{context}inserir/', methods=['POST'], view_func=self.insert)
        app.add_url_rule(f'{context}inserir/<id>', methods=['POST'], view_func=self.insert)

        app.add_url_rule(f'{context}form', view_func=self.form)
        app.add_url_rule(f'{context}form/<id>', view_func=self.form)

    def list(self, columns='*'):
        rows = self.dao.list(columns)
        print('colunas', columns, flush=True)
        return render_template(f'{self.viewFolder}/listar.html', rows=rows)

    def delete(self, id):
        self.dao.delete(id)

        return 'Registro #{} apagado com sucesso!'.format(id)
        
    def insert(self, id='0'):
        bean = self.getBeanFromRequest()
        if id == '0':
            id = self.dao.insert(bean)
            acao = 'cadastrado'
        else:
            acao = 'alterado'
            self.dao.update(bean, id)

        return 'Registro #{} {} com sucesso!'.format(id, acao)

    def form(self, id='0'):
        bean = self.getDefaultBean()
        # id = request.args.get('id')
        if id != '0':
            bean = self.dao.findOne(id)

        return render_template(f'{self.viewFolder}/form.html', bean=bean, id=id)

    def getDefaultBean(self):
        bean = {}
        return bean

class CrudEventos(Crud):
    def __init__(self, dao):
        super().__init__(dao, viewFolder='eventos')

    def list(self):
        return super().list('id, titulo, data')

    def getBeanFromRequest(self):
        titulo = request.form.get('titulo')
        data = request.form.get('data')

        bean = {
            'titulo': titulo, 
            'data': data
        }
        return bean

    def getDefaultBean(self):
        bean = {'data': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')}
        return bean


class CrudUsuario(Crud):
    def __init__(self, dao):
        super().__init__(dao, viewFolder='usuarios')

    def list(self):
        return super().list('id, titulo, data')
    def getBeanFromRequest(self):
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        bean = {
            'nome': nome, 
            'senha': senha
        }
        return bean