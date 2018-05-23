import getExternalRate as g
import mongo as m
import datetime

class exchange():
	def __init__(self):
		self.collection = cfg['mongo']['collection']['toGuess']
		self.now = datetime.datetime.now()

	def exchangeInfo(self,*args):
		self.name = [ str(k) for k in args ]
		self.b = g.getExternalRate(self.name)
		self.rates = self.b.getKurRates()
		b.wdClose()
		#q = prepareQuery(self.rates)
		#writeExchangeInfo(q)

	def writeExchangeInfo(self,query):
		self.query = query
		self.m = m.insertDoc(self.collection,self.query)
