from pymongo import MongoClient, database, errors
import variable as v
import sys
import ast

class database():
	def __init__(self):
		self.cfg = v.config()
		self.dbname = self.cfg['mongo']['db']
		self.dbhost = self.cfg['mongo']['host']
		self.dbport = self.cfg['mongo']['port']
		self.timeout = self.cfg['mongo']['timeout']
		self.mC = MongoClient(self.dbhost,self.dbport,serverselectiontimeoutms=self.timeout)
		print "Connecting to Mongo Instance -> mongo://" + self.dbhost + ':' + str(self.dbport)
		try:
			self.mC.server_info()
			print "Connected.."
		except:
			print err + " Cannot connect to Mongo Instance"
			sys.exit(10)

	def insertDoc(self,collection,query):
		self.collection = collection
		self.query = query
		coll = self.mC[self.dbname][self.collection]
		coll.insert_one(query)

	def dropCollection(self,collection):
		self.collection = collection
		coll = self.mC[self.dbname][self.collection]
		coll.drop()

#class databaseSetup(database):
#	def __init__(self):
#		pass
#
#	def checkDb(self):
#		if self.dbname in self.mC.database_names():
#			print self.dbname + " database exists"
#			return True
#		else:
#			return False
#
#
#class databaseInfo(database):
#	def __init__():
#		pass
#
#	def getCollectionList(self):
#		if self.checkDb():
#			return self.mC.self.dbname.collection_names()
#		else:
#			print "No such database " + self.dbname
#
#	def getDocumentsInCollection(self,colName):
#		self.dbColName = colName
#		a = self.checkDb()
#		b = []
#		for post in a[self.dbColName].find():
#			b.append(post)
#		return b
#
#	def insertDocumentsInCollection(self,colName,query):
#		self.dbColName = colName
#		self.dbQuery = ast.literal_eval(query)
#		a = self.checkDb()
#		result = a[self.dbColName].insert_one(dict(self.dbQuery))

