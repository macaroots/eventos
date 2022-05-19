import pymongo
from bson.objectid import ObjectId

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
	
	def update(self, bean, id):
		query = {"_id": ObjectId(id)}
		values = {"$set": bean}

		collection = self.getCollection()
		return collection.update_one(query, values)

	def delete(self, id):
		query = {"_id": ObjectId(id)}

		collection = self.getCollection()
		result = collection.delete_one(query)
		
		return result
		
	def findOne(self, id):
		query = {"_id": ObjectId(id)}

		collection = self.getCollection()
		bean = collection.find_one(query)
		
		return bean

	def getDBName(self):
		return 'db'
	def getCollectionName(self):
		return self.collectionName