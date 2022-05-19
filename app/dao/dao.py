import copy
import os

class DAOPessoasAbstrato:
	def __init__(self):
		pass
		
	def criaDB(self, nome=None):
		pass
		
	def apagaDB(self):
		pass
		
	def lista(self):
		pass
		
	def insere(self, pessoa):
		pass
		
	def getById(self, id):
		return self.lista()[id]

class DAOPessoasList(DAOPessoasAbstrato):
	def __init__(self):
		pass
		
	def criaDB(self):
		self.pessoas = []
		
	def apagaDB(self):
		del self.pessoas
		
	def lista(self):
		return copy.deepcopy(self.pessoas)
		
	def insere(self, pessoa):
		self.pessoas.append(pessoa)
		return len(self.pessoas) - 1

class DAOPessoasArquivo(DAOPessoasAbstrato):
	def __init__(self, nome='temp'):
		self.nome = nome
		
	def criaDB(self):
		arquivo = open(self.nome, 'w')
		arquivo.close()
		
	def apagaDB(self):
		os.remove(self.nome)
		
	def lista(self):
		pessoas = []
		arquivo = open(self.nome, 'r')
		linhas = arquivo.readlines()
		for linha in linhas:
			pessoa = linha.strip().split(',')
			pessoas.append(pessoa)
		arquivo.close()
		return pessoas
		
	def insere(self, pessoa):
		arquivo = open(self.nome, 'a')
		arquivo.write('{},{}\n'.format(*pessoa))
		arquivo.close()
		id = self.getNumeroLinhas() - 1
		return id
		
	def getNumeroLinhas(self):
		arquivo = open(self.nome)
		num_lines = sum(1 for line in arquivo)
		arquivo.close()
		return num_lines
		
class DAOPessoasBD(DAOPessoasAbstrato):
	def __init__(self):
		pass
		
	def criaDB(self, nome=None):
		pass
		
	def apagaDB(self):
		pass
		
	def lista(self):
		pass
		
	def insere(self, pessoa):
		pass
		
	def getById(self, id):
		return self.lista()[id]
