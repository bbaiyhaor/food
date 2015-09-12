#encoding=utf-8
from HTMLParser import HTMLParser
from random import randint

dataFlag = False
dataDiv = 0
index = {}
indexID = 0

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global dataFlag, dataDiv
		if (dataFlag == True):
			dataDiv += 1
		elif (tag=='div'):
			for item in attrs:
				if ((item[0] == 'id') and (item[1] == 'bodyContent')):
					dataFlag = True
					dataDiv = 1
	
	def handle_endtag(self, tag):
		global dataFlag, dataDiv
		if (dataFlag == False):	
			dataDiv -= 1
			if (dataDiv == 0):
				dataFlag = False
				
	def handle_startendtag(self, tag, attrs):
		pass
		
	def handle_data(self, data):
		global dataFlag, dataDiv
		if (dataFlag == True):
			dataList = data.split()
			for item in dataList:
				if (item.isalpha() == True):
					item = item.lower()
					if not (item in index):
						index[item] = [indexID]
					if (index[item][-1] != indexID):
						index[item].append(indexID)
					
	def handle_comment(self, data):
		pass
		
	def handle_entityref(self, name):
		pass
		
	def handle_charref(self, name):
		pass