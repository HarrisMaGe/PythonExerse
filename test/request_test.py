# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import urlparse

import requests
from bs4 import BeautifulSoup
import os

NUMBER = 0
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

def beginSpider(page):
    try:
        begin_url = 'http://tieba.baidu.com/f?kw=%E6%9D%8E%E4%B8%80%E6%A1%90&ie=utf-8&tp=0&pn='+str(j)
        start_url = urllib2.urlopen(begin_url)
        #print start_url.text
        base_url = 'http://tieba.baidu.com'
        soup = BeautifulSoup(start_url,'html.parser',from_encoding = 'utf-8')
        add_list = soup.find_all("div",class_ = 'threadlist_title pull_left j_th_tit ')

        urlset = set();
        for link in add_list:
            new_url = link.find('a').get('href')
            new_full_url = urlparse.urljoin(base_url,new_url)
            urlset.add(new_full_url)
            new_url_2 = urllib2.urlopen(new_full_url)
            soup_1 = BeautifulSoup(new_url_2,'lxml')
            the_page = soup_1.find('li',class_='l_pager pager_theme_4 pb_list_pager')
            the_next_url = the_page.find_all('a')
            for the_url in the_next_url:
                the_next_url_2 = the_url.get('href')
                the_final_url = urlparse.urljoin(base_url,the_next_url_2)
                    #new_full_url_2 = new_full_url + '?pn=' + str(i)
                urlset.add(the_final_url)
                    #print the_final_url
        return urlset
    except :
        print 'a'




def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html,page,path):
    global NUMBER
    soup = BeautifulSoup(html,"lxml")
    source = soup.find_all("img",class_ = "BDE_Image")
    for link in source:
        reg = link.get('src')
        urllib.urlretrieve(reg, path+'\\%s.jpg' % NUMBER)
        ##f.close()
        NUMBER = NUMBER+1


if __name__ == '__main__':
    count = 1;

    j = 0

    os.mkdir('F:\\3')
    os.chdir('F:\\3')
    while j < 3651:
        #i = 0
        url_set = beginSpider(j);
        j = j + 50
        for url in url_set:
            try:
                print '爬取第' + str(count) + '个页面'
                #print url
                html = getHtml(url);
                getImg(html,count,'F:\\3')
               # i = i+1
                count = count +1
            except:
                print '页面'+ str(count) +'出错'
                count = count + 1
                continue

