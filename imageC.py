# -*- coding: utf-8 -*-

import urllib2
import urllib
import re

from collections import deque


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
     reg = r'src="(.+?\.jpg)"'
     img = re.compile(reg)
     imglist = re.findall(img,html)
     x = 0

     for imgurl in imglist:
         urllib.urlretrieve(imgurl, 'F:\\2\\%s.jpg' % x)
         x += 1


def setUrl(url, visited,queue):
    queue.append(url)

    while queue:
        url = queue.popleft()
        if url ==re.compile(r'http://?/p/?'):
            visited.add(url)
        try:
            urlop = urllib.urlopen(url)
            html = urlop.read()
            linkre = re.compile('href=\"(.+?)\"')
            for x in linkre.findall(html):
                if 'http' in x and x not in visited:
                    queue.append(x)
                    print("加入队列....." + x)
            getImg(queue.popleft())
        except:
            continue
    return visited

queue = deque()
visited = set()

setUrl("http://tieba.baidu.com/f?kw=李一桐&ie=utf-8&tab=good",visited,queue)


#url = "http://movie.douban.com/tag/"
#pageData = urllib.request.urlopen(url).read()
#data = pageData.decode('UTF-8')
#print(data)
