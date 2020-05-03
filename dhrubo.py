# NOTE: cd codes\python projects
# NOTE:  python dhrubo.py

import re
sum=0
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "sample.txt"

fh = open(fname)


for line in fh:
    temp=re.findall("[0-9]+",line)
    for i in temp:
        n=int(i)
        sum=sum+n

print(sum)
