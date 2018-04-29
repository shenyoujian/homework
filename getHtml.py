from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import os

pages = set()
baseUrl = "http://www.sise.com.cn"
downloadDirectory = "downloaded"
# 爬取网页
def getHtml(pageUrl):
	global pages
	html = urlopen(baseUrl+pageUrl)
	bsObj = BeautifulSoup(html,"lxml")
	tags = bsObj.findAll("a", href=re.compile("^(/sise/)(.+)(.html)$"))
	for tag in tags:
		if 'href' in tag.attrs:
			if tag.attrs['href'] not in pages:
				# 我们遇到了新页面
				newPage = tag.attrs['href']
				print(newPage)
				pages.add(newPage)
				getHtml(newPage)



# 获取下载绝对地址
def getDownloadPath(baseUrl, absoulteUrl, downloadDirectory):
	# path = absoulteUrl.replace("www.", "")
	path = absoulteUrl.replace(baseUrl,"")
	path = downloadDirectory+path
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path




getHtml("")    # 空url也就是首页
for page in pages:
	urlretrieve(baseUrl+page, getDownloadPath(baseUrl, baseUrl+page, downloadDirectory))
