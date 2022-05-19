import pymongo

class DAO:
	def __init__(self, collectionName='collection1'):
		self.collectionName = collectionName
			
	def connect(self):
		connection = pymongo.MongoClient("mongodb://root:admin@mongodb:27017/")
		return connection

	def getCollection(self):
		connection = self.connect()
		db = connection[self.getDBName()]
		collection = db[self.getCollectionName()]
		return collection
		
	def createDB(self):
		pass
		
	def dropDB(self):
		del self.pessoas
		
	def list(self, columns='*'):
		collection = self.getCollection()
		beans = collection.find()
		return beans

	def insert(self, bean):
		collection = self.getCollection()
		id = collection.insert_one(bean)
		return id.inserted_id
	
	def update(self, row, id):
		return self.execute(sql, row + (id, ))

	def delete(self, id):
		return self.execute(sql, (id, ))
		
	def findOne(self, id):
		return row

	def getDBName(self):
		return 'db'
	def getCollectionName(self):
		return self.collectionName