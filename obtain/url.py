#encoding=utf-8
import urllib, urllib2, cookielib
import os
import re
		
rootURL = "https://en.wikipedia.org/wiki/"


user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',    
headers = { 'User-Agent' : user_agent 
			}  
'''
browser disguise
'''

cookiejar = cookielib.CookieJar()		
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar)) 
urllib2.install_opener(opener)	
'''
install handler
'''
			
def downloadHTML(url, food, dirPath, totLog):
	global rootURL, headers
	url = rootURL + url
	print url
	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req) 
	content = response.read()
	dirPath = "{dirPath}/{name}.html".format(dirPath = dirPath, name = totLog)
	html = open(dirPath, 'w')
	html.write(content)
	html.close()
	print "have writen {0} urls, current is the {1}th {2}".format(totLog, totLog, food)
'''
	download html code
'''

def abstract(dirPath, htmlContent):
	myItems = re.findall('<a.*?section=1.*?>edit</a>(.*)<a.*?section=2.*?>edit</a>', htmlContent, re.S)	
	allURL = open(dirPath + "/rootall", "w")
	totLog = 0
	for item in myItems:
		tdurl = re.findall('<tr>.<td><a href="/wiki/(.*?)" title=".*?".*?>(.*?)</a>.*?</td>', item, re.S)
		for row in tdurl:
			totLog += 1
			print >> allURL, totLog,
			allURL.write(' ')
			allURL.write(row[1])
			allURL.write('\n')
			downloadHTML(row[0], row[1], dirPath, totLog)
'''
	abstract useful code
'''

def seek(dirPath, foodClass):
	foodURL = rootURL + foodClass
	print "open url ", foodURL
	global headers
	req = urllib2.Request(foodURL, headers = headers)
	response = urllib2.urlopen(req) 
	content = response.read()
	html = open(dirPath + '/root.html', 'w')
	html.write(content)
	html.close()
	abstract(dirPath, content)
'''
	seek url
'''

def main():
	file = open("table.txt")
	foodList = file.readlines()
	for foodClass in foodList:
		foodClass = foodClass.replace(' ', '_')
		path = os.path.dirname(os.path.abspath(__file__)) + '/' + foodClass
		isExists = os.path.exists(path)
		if (not isExists):
			os.mkdir(path)
		seek(dirPath = path, foodClass = foodClass)
		
if (__name__ == "__main__"):
	main()