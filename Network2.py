# NOTE: cd codes\python projects

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ans=''
fstname=''
link= input("Enter URL: ")
count=input("Enter count: ")
position=input("Enter position: ")
count=int(count)
position=int(position)
position=position-1


for i in range(count+1):
    ans=fstname
    print('Retrieving:',link)
    fhand=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(fhand,'html.parser')
    tags=soup('a')
    link=tags[position].get('href',None)
    fstname=tags[position].contents[0]

print(ans)
