#! /usr/bin/python
# FileName   : srcheng.py
# Author     : luzhlon
# Function   : 爬取搜索引擎的搜索结果
# LastChange : 2017/2/17

from HTMLParser import HTMLParser
import socket
import urllib2

#Check the specified tag's attibute
def check_attr(table, attr, val):
    for att in table:
        if att[0]==attr:
            return (att[1]==val)
    return False
def get_attr(table, attr):
    for att in table:
        if att[0]==attr:
            return att[1]
    return None
def get_webpage(url, timeout=10):
    req = urllib2.Request(url)
    ff = urllib2.urlopen(req, timeout = timeout)
    return ff.read()

#SearchEngine base class
class srcheng(HTMLParser):
    def __init__(self, word, hostname = None, count = 10):
        #super(srcheng, self).__init__(self)
        HTMLParser.__init__(self)
        self.word = word   #Key words
        self.count = count #Item count per page
        self.curitem = 1   #Current item number (the first item of a page)
        self.timeout = 5   #Timeout seconds
        if hostname:
            self.hostname = hostname
            self.ip = socket.gethostbyname(hostname)
    def __iter__(self):
        return self
    def next(self):
        assert False, 'The next method must be overwrite.'
    def set_curitem(self, curitem):
        self.curitem = curitem
    def set_timeout(self, timeout):
        self.timeout = timeout
    def set_word(self, word):
        self.word = word
    def set_ip(self, iptxt):
        self.ip = iptxt
    def set_hostname(self, hostname):
        self.hostname = hostname
    def get_ip(self):
        return self.ip
    def get_pagetext(self):
        #req = url.Request(self.get_url())
        #ff = url.urlopen(req, timeout=self.timeout)
        print self.get_url()
        return get_webpage(self.get_url(), 5)

#Bing Search Engine
class Bing(srcheng):
    def __init__(self, word):
        return srcheng.__init__(self, word, 'www.bing.com')
    def get_url(self):
        return 'https://' + self.get_ip() + '/search?q=' + \
            self.word + '&first=' + str(self.curitem)
    def handle_starttag(self, tag, attrs):
        if tag=='ol' and check_attr(attrs, 'id', 'b_results'):
            self.flag_begin_parse = True
        elif not self.flag_begin_parse:
            return
        elif tag=='li' and check_attr(attrs, 'class', 'b_algo'):
            self.flag_enter_li = True
        elif tag=='a' and self.flag_enter_li:
            #self.result += get_attr(attrs, 'href')
            url = get_attr(attrs, 'href')
            self.result.append(url)
    def handle_endtag(self, tag):
        if tag=='ol':
            if self.flag_begin_parse:
                self.flag_begin_parse = False
                #self.close()
        elif tag=='li':
            self.flag_enter_li = False
    def next(self):
        self.flag_begin_parse = False
        self.flag_enter_li = False
        self.result = []
        htmltext = self.get_pagetext()
        self.feed(htmltext)
        self.curitem += self.count
        return self.result

class Baidu(srcheng):
    def __init__(self, word):
        return srcheng.__init__(self, word, 'www.baidu.com')
    def get_url(self):
        return 'https://' + self.get_ip() + '/s?wd=' + \
            self.word + '&first=' + str(self.curitem)
    def handle_starttag(self, tag, attrs):
        if tag=='div':
            if self.flag_begin_parse:
                self.flag_div_count += 1
            if check_attr(attrs, 'id', 'content_left'):
                self.flag_div_count = 0
                self.flag_begin_parse = True
            elif check_attr(attrs, 'class', 'result c-container'):
                self.flag_enter_li = True
        elif not self.flag_begin_parse:
            return
        elif tag=='a' and self.flag_enter_li:
            #self.result += get_attr(attrs, 'href')
            url = get_attr(attrs, 'href')
            self.result.append(url)
    def handle_endtag(self, tag):
        if self.flag_begin_parse and tag=='div':
            self.flag_div_count -= 1
    def next(self):
        self.flag_div_count = 0
        self.flag_begin_parse = False
        self.flag_enter_li = False
        self.result = []
        htmltext = self.get_pagetext()
        self.feed(htmltext)
        self.curitem += self.count
        return self.result

def get_google_ip():
    class ParseGoogle(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.flag_get_ip = False
            self.flag_ended = False
            self.result = None
            self.count_a = 0
        def handle_starttag(self, tag, attrs):
            if tag=='a':
                if check_attr(attrs, 'target', '_blank'):
                    if self.count_a==3:
                        self.flag_get_ip = True
                    self.count_a += 1
        def handle_data(self, data):
            if self.flag_ended:
                return
            if self.flag_get_ip:
                self.result = data
                self.flag_ended = True
    p = ParseGoogle()
    p.feed(get_webpage('http://googless.sinaapp.com/'))
    assert p.result
    return p.result

#Google Search Engine
class Google(srcheng):
    def __init__(self, word):
        #return srcheng.__init__(self, word, 'www.google.com')
        self.set_hostname('www.google.com')
        self.set_ip(get_google_ip())
        return srcheng.__init__(self, word)
    def get_url(self):
        return 'http://' + self.get_ip() + '/#q=' + \
            self.word + '&start=' + str(self.curitem)
    def handle_starttag(self, tag, attrs):
        if tag=='ol' and check_attr(attrs, 'id', 'rso'):
            self.flag_begin_parse = True
        elif not self.flag_begin_parse:
            return
        elif tag=='li' and check_attr(attrs, 'class', 'g'):
            self.flag_enter_li = True
        elif tag=='a' and self.flag_enter_li:
            url = get_attr(attrs, 'href')
            print url
            self.result.append(url)
    def handle_endtag(self, tag):
        if tag=='li':
            self.flag_enter_li = False
        elif tag=='ol':
            self.flag_begin_parse = False
    def next(self):
        self.flag_begin_parse = False
        self.flag_enter_li = False
        self.result = []
        htmltext = self.get_pagetext()
        print htmltext
        raw_input()
        self.feed(htmltext)
        self.curitem += self.count
        return self.result

def main():
    for page in Bing('vpn'):
    #for page in Google('vpn'):
        for item in page:
            print item

if __name__=='__main__':
    main()
