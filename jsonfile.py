# NOTE: cd codes\python projects

import urllib.request, urllib.parse, urllib.error
import json
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

info = json.loads(data)
print("Count : ",len(info['comments']))
for item in info["comments"]:
    sum=sum+int(item['count'])


print("Sum : ",sum)
