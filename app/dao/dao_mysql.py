import mysql.connector

class DAO:
    def __init__(self):
        pass
            
    def connect(self):
        connection = mysql.connector.connect(
            host='mysql',
            user='root',
            password='admin',
            database='eventos'
        )
        return connection
        
    def createDB(self):
        pass
        
    def dropDB(self):
        del self.pessoas
        
    def list(self, columns='*'):
        sql = self.getListSql(columns)
        return self.query(sql)

    def insert(self, row):
        sql = self.getInsertSql()
        return self.execute(sql, row)
    
    def update(self, row, id):
        sql = self.getUpdateSql()
        return self.execute(sql, row + (id, ))

    def delete(self, id):
        sql = self.getDeleteSql()
        return self.execute(sql, (id, ))

    def query(self, sql, args=None):
        connection = self.connect()
        cursor = connection.cursor()
        
        cursor.execute(sql, args)
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        return rows        

    def execute(self, sql, args=None):
        connection = self.connect()
        cursor = connection.cursor()
        
        cursor.execute(sql, args)
        id = cursor.lastrowid
        
        connection.commit()
        cursor.close()
        connection.close()
        return id
        
    def getById(self, id):
        sql = self.getByIdSql()

        connection = self.connect()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute(sql, (id, ))
        row = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return row

    def getListSql(self, columns='*'):
        return 'select {} from {}'.format(columns, self.getTableName())
    def getInsertSql(self):
        return 'insert into {} values (default, %s, %s)'.format(self.getTableName())
    def getDeleteSql(self):
        return 'delete from {} where id=%s'.format(self.getTableName())
    def getByIdSql(self):
        return 'select * from {} where id=%s'.format(self.getTableName())

class DAOEventos(DAO):
    def getTableName(self):
        return 'eventos'
    def getInsertSql(self):
        return 'insert into eventos (titulo, data) values (%s, %s)'
    def getUpdateSql(self):
        return 'update eventos set titulo=%s, data=%s where id=%s'

class DAOInscricoes(DAO):
    def getTableName(self):
        return 'inscricoes'
    def getListSql(self, columns):
        return 'select e.titulo, u.nome from eventos e join inscricoes i on e.id=i.eventos_id join usuarios u on u.id=i.usuarios_id'
    def getInsertSql(self):
        return 'insert into inscricoes (usuarios_id, eventos_id) values (%s, %s)'

class DAOUsuarios(DAO):
    def getTableName(self):
        return 'usuarios'
    def getInsertSql(self):
        return 'insert into {} (nome, email) values (%s, %s)'.format(self.getTableName())