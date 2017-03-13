# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:27:24 2017

@author: xk
"""

#!/usr/bin/python3
#Author: Haiyang Zheng
#Create: 2017-03-09
#Commit: requests, BeautifulSoup, format, chr(12288)...
 
import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
 
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):
            rank=tr.td.prettify().split('\n')[1] #Get rank for each University
            tds=tr.td('td')
            ulist.append([rank, tds[0].string, tds[2].string])
 
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{0:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    #print({'排名':^8}\t{'学校':{chr(12288)}^10}\t{'总分':<10})
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
 
def main():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
 
if __name__ == '__main__':
    main()
