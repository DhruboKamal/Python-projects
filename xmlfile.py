# NOTE: cd codes\python projects

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter location: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
sum=0
tree = ET.fromstring(data)
lst= tree.findall('.//comment')
print("Count : ",len(lst))
for item in lst:
    x=(item.find('count').text)
    sum=sum+int(x)

print("Sum : ",sum)
