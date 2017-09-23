import urllib2
from bs4 import BeautifulSoup
import re

url = "http://www.bilibili.com/"
response = urllib2.urlopen(url,timeout=10)

soup = BeautifulSoup( response, 'html.parser',from_encoding='utf-8')
links = soup.find_all('a')
#for link in links:
  #  print link.name,link['href'],link.get_text()



print soup.get_text