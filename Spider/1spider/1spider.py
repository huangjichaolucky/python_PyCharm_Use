#-*- coding=utf-8 -*-
# 详细教程见 http://cuiqingcai.com/1052.html

import urllib
import urllib2
import re
def spiderMethod():

    header = {
        'User - Agent': 'Mozilla / 5.0(Macintosh;IntelMacOSX10_12_0)\n'
                        ' AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36'
    }
    url = 'http://www.jianshu.com'
    req = urllib2.Request(url, None, header)
    response = urllib2.urlopen(req)
    html = response.read()
    html
    print html
def scrapyMethod():
    print urllib.__file__()
    # scrapy startproject tutorial

def main():
    # spiderMethod()
    scrapyMethod()

if __name__ == '__main__':
    main()