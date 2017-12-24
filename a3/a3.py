import os
import sys


fn=raw_input("Enter Filename: ")
if(not(os.path.exists(fn))):
	print "File does not Exist!"
	sys.exit()

if(fn.split('.')[-1]!='txt'):
	print "File should be of type Text!"
	sys.exit()

f=open(fn)
dic={}
for i in f:
	for j in i.split():
		j=j.lower()
		w=dic.get(j,0)
		w=w+1
		dic[j]=w

print dic


