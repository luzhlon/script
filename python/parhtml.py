#! /usr/bin/python
# FileName   : parhtml.py
# Author     : luzhlon
# Function   : python爬虫
# LastChange : 2017/2/17

from HTMLParser import HTMLParser
import threading
import urllib as u1
import urllib2 as u2
import re as re      #Regular Expression

EntryFlag = 0

log = open('log.txt', 'w')

def CheckTarget(url, event):
    index = url.find('/') + 2
    index = url.find('/', index)
    url = url[:index]
    print('::::::::', url)
    url += '/cmd.jsp'
    try:
        req = u2.Request(url)
        resp = u2.urlopen(req)
        html = resp.read()
        print(resp.getcode(), url)
        log.write(url)
        log.write('\n')
    except Exception,e:
        #print(e)
        pass
    event.set()
    pass

def CheckAttr(table, attr, val):
    for att in table:
        if att[0]==attr:
            return (att[1]==val)

def CallFunc(url):
    event = threading.Event()
    event.clear()
    thread = threading.Thread(target=CheckTarget, args=(url, event))
    thread.start()
    event.wait(3)

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.CorrectOl = 0
        self.CorrectLi = 0
        pass

    def handle_starttag(self, tag, attrs):
        #filter the correct seached results
        global EntryFlag
        if tag=='ol' and CheckAttr(attrs, 'id', 'b_results'):
            self.CorrectOl = 1
        elif self.CorrectOl and tag=='li' and CheckAttr(attrs, 'class', 'b_algo'):
            self.CorrectLi = 1
        elif self.CorrectLi and tag=='a':
            for attr in attrs:
                if attr[0]=='href':
                    CallFunc(attr[1])
                    break
        else:
            pass
    def handle_endtag(self, tag):
        if tag=='ol':
            self.CorrectOl = 0
        elif tag=='li':
            self.CorrectLi = 0
        pass

strFormat = 'https://www.bing.com/search?q=%E6%98%93%E7%91%9E%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E7%B3%BB%E7%BB%9F&pc=MOZI&first=11&FORM=PORE'

i = 1

#
#while i<25000:
#    url =  'https://www.bing.com/search?q=%E6%98%93%E7%91%9E%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%E7%B3%BB%E7%BB%9F&pc=MOZI&first='+('%d'%i)+'&FORM=PORE'
#    i += 10
#    req = u2.Request(url)
#    resp = u2.urlopen(req)
#    html = resp.read()
#    parser = MyParser()
#    parser.feed(html)

ll = [
'http://hzic.vip.qikan.com/text/text.aspx',
'http://www.lawyee.net/user/autologinbyip.asp',
'http://www.cssci.com.cn',
'http://www.cqvip.com',
'http://210.33.91.76/index.asp',
'http://dlib.cnki.net/kns50/',
'http://210.33.91.68:8080/cgrs/index.jsp',
'http://www.webofknowledge.com/',
'http://www.sciencedirect.com/',
'http://search.ebscohost.com/',
'http://proquest.umi.com/pqdweb?rqt=301&userid=ipauto&jsenabled=1&cfc=1',
'http://www.jstor.org/',
'http://online.sagepub.com/',
'http://www.emeraldinsight.com/',
'http://www.lexisnexis.com/ap/auth/',
'http://highwire.stanford.edu/',
'http://onlinelibrary.wiley.com/',
'http://pubs.acs.org/',
'http://acm.lib.tsinghua.edu.cn/',
'http://china.springerlink.com/home/main.mpx',
'http://china.springerlink.com/books/',
'http://www.worldtradelaw.net/',
'http://HeinOnline.org',
'http://db.lib.tsinghua.edu.cn/ieee1/',
'http://www.scopus.com/home.url',
'http://www.engineeringvillage.com/',
'http://worldscinet.lib.tsinghua.edu.cn/',
'http://www.lexisnexis.com/ap/academic/',
'http://search.ebscohost.com/login.aspx?profile=econlit&defaultdb=eoh',
'http://ccc.calis.edu.cn/',
'http://www.tandfonline.com/',
'http://periodical.cepiec.com.cn/CSP/Publishers/NOW/',
'http://10.99.253.82/Refbook/',
'http://10.99.253.82/usp/',
'http://www.duxiu.com/',
'http://10.99.253.89/markbook/GetIndex.jsp',
'http://proquest.calis.edu.cn/umi/index.jsp',
'http://www.ssvideo.cn/',
'http://www.bingoenglish.net/' ]

for item in ll:
    CallFunc(item)

log.close()
