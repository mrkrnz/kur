from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


class getExternalRate():
	def __init__(self,*args):
		# { kur : [alis, satis] , kur2 : [alis,satis] , ....}
		self.kurPath = {
			'usd' : [ "//*[@id='htmlDefaultTableCover']/div[1]/div[3]", "//*[@id='htmlDefaultTableCover']/div[1]/div[2]" ],
			'eur' : [ "//*[@id='htmlDefaultTableCover']/div[2]/div[3]", "//*[@id='htmlDefaultTableCover']/div[2]/div[2]" ]
		}
		#self.usdXpath = "\"//*[@id='htmlDefaultTableCover']/div[1]/div[2]\""
		#self.eurXpath = "\"//*[@id='htmlDefaultTableCover']/div[2]/div[2]\""
		self.wd = webdriver.Firefox()
		time.sleep(3)
		self.kurNames = [ str(k) for k in args[0] ]
		self.weblink = "https://www.isbank.com.tr/TR/fiyatlar-ve-oranlar/doviz-kurlari/Sayfalar/doviz-kurlari.aspx"
		self.wd.get(self.weblink)

	def getKurRates(self):
		self.rates = {}
		for i in self.kurNames:
			tempKur = []
			for j in self.kurPath[i]:
				kurx = self.wd.find_element_by_xpath(j)
				tempKur.append(float(kurx.text))
			self.rates[i] = tempKur
		return self.rates

	def wdClose(self):
		 self.wd.close()
