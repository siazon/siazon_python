# -*- coding:utf-8 -*-
#___author___= 'siazon'
from bs4 import BeautifulSoup
import re
import sqlite3
import urllib
import time

#urllib找开链接
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#正则查找
def getImg(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    return imglist

#html=getHtml("http://shop.huaji.com/")
#print  getImg(html)



#插入数据库
def insertDB(name,addr,addrp,path,qq):
    conn=sqlite3.connect('./siazon_python.db')
    cursor=conn.cursor()
    cursor.execute("INSERT into category (name,addr,addrp,path,qq) VALUES (?,?,?,?,?);",(name,addr,addrp,path,qq))
    conn.commit()
    cursor.close()


def get_qq(qqstr):
    reg=r'.*:(.*):.*'
    qq=re.findall(reg,qqstr)
    return qq


def get_attractions(url):
    page=urllib.urlopen(url)
    html=page.read()
    soup=BeautifulSoup(html,'lxml')
    shopNames = soup.select('p.shop_hd_title.fl.nowrap > a')
    addres=soup.select('p.mt5.nowrap > span')
    addrPs=soup.select('p.address')
    qqs=soup.select('a.qq_ico > img')
    for name,addr,addrp,path,qq in zip(shopNames,addres,addrPs,shopNames,qqs):
        #insertDB(name.text,addr.text,addrp.text,'http://shop.huaji.com'+path['href'],get_qq(qq['src'])[0])
        data={
            'name':name.text,
            'addr':addr.text,
            'addrp':addrp.text,
            'qq':get_qq(qq['src'])[0],
            'path':path['href'],
         }
        print data


i=1
while(i<2):
    i+=1
    get_attractions('http://shop.huaji.com/index.php?&page='+str(i))
    print i
    time.sleep(100000)


# for img in zip(imgs):
#     data={
#         'img' : img.get('src')
#     }
#     print data


#soup = BeautifulSoup(html_doc,'lxml')

# print soup.title
#
# print soup.title.name
#
# print soup.title.string
#
# print soup.p
#
# print soup.a
#
# print soup.find_all('a')
#
# print soup.find(id='link3')
#
# print soup.get_text()
#print soup.find_all('a',limit=1)