from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import os


pages = set()
apages = set()
baseUrl = "http://www.sise.com.cn/"
def getLinks():
	global pages
	html = urlopen(baseUrl)
	bsObj = BeautifulSoup(html,"lxml")
	tags = bsObj.findAll(re.compile("a|link|script|img"))
	# print(tags)
	print("Media: (%s)" %len(tags))
	# 把链接保存到txt中
	with open("C:\python_work\Scraping\chapter5\links.txt","w") as f:
		for tag in tags:
			if 'href' in tag.attrs:
				if tag.attrs['href'] not in pages:
					link = tag.attrs['href']
					print("* %s: %s" %(tag.name,link))
					pages.add(link)
					f.write(link+'\n')
			if 	'src' in tag.attrs:
				if tag.attrs['src'] not in pages:
					link = tag.attrs['src']
					print("* %s: %s" %(tag.name,link))
					pages.add(link)
				

getLinks()
