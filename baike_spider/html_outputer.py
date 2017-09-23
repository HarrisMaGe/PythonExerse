# -*- coding: utf-8 -*-
import re
import urllib


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")

        fout.write("<body>")
        # fout.write("<table>")
        for data in self.datas:
            # fout.write("<tr>")
            fout.write("<br/")
            fout.write("<h1>%s</h1>" % data['title'].encode('utf-8'))
            fout.write("<p>%s</p>" % data['summary'].encode('utf-8'))
            # fout.write("</tr>")
        # fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def getImg(html):
        reg = r'src="(.+?\.jpg)" '
        img = re.compile(reg)
        imglist = re.findall(img, html)
        x = 0

        for imgurl in imglist:
            urllib.urlretrieve(imgurl, 'F:\\2   \\%s.jpg' % x)
            x += 1
