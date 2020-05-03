# NOTE: cd codes\python projects

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

link= input("Enter - ")
fhand=urllib.request.urlopen(link).read()
soup=BeautifulSoup(fhand,'html.parser')

count=0
sum=0

tags=soup('span')
for tag in tags:
    num=(tag.contents[0])
    num=int(num)
    count=count+1
    sum=sum+num

print('Count',count)
print('Sum',sum)
