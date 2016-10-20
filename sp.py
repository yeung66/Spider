#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



url='http://www.qiushibaike.com/'
res = requests.get(url)
web = BeautifulSoup(res.text)
duanzi = web.find_all('div', 'content')

txt=open('txt.txt','w+')

for i in duanzi:
    txt.write(i.text)
print "Done!"