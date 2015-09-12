#encoding=utf-8
import MyHTMLParser
import urllib, urllib2, cookielib
import os
import re

myHandler = MyHTMLParser.MyHTMLParser()


def insert(content):
	global myHandler
	myHandler.feed(content)
'''
	get information
'''

def create(dirPath, foodClass):
	rootall = open(dirPath + '/rootall')
	items = rootall.readlines()
	cur = 0
	MyHTMLParser.index = {}
	for item in items:
		cur += 1
		html = open(dirPath + '/' + str(cur) + '.html')
		content = ''.join(html.readlines())
		MyHTMLParser.indexID = cur
		insert(content)
		print "current have finished {} tasks".format(cur)
		
	dict = open(dirPath + '/dict', 'w')
	print >> dict, MyHTMLParser.index
	print "\n\n" + dirPath + '/dict' + "have finished!!!\n\n"		
'''
	create index
'''

def main():
	file = open("table.txt")
	foodList = file.readlines()
	for foodClass in foodList:
		foodClass = foodClass.replace(' ', '_')
		foodClass = foodClass.replace('\n', '')
		path = os.path.dirname(os.path.abspath(__file__)) + '/' + foodClass
		isExists = os.path.exists(path)
		print path, isExists
		if (isExists):
			print path
			create(dirPath = path, foodClass = foodClass)
		
if (__name__ == "__main__"):
	main()