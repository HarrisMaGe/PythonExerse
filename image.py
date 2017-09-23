# -*- coding: utf-8 -*-
import urllib2
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" '
    img = re.compile(reg)
    imglist = re.findall(img,html)
    x = 0

    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'F:\\2\\%s.jpg'%x)
        x+=1


html = getHtml("http://www.mzitu.com/")
print getImg(html)

