import sys
import os

fn=raw_input("Enter File Name: ")

if(not(os.path.exists(fn))):
	print "File Not Found!"
	quit()

if(not(fn.split('.')[-1]=="txt")):
	print "Only Text Files Allowed!"
	quit()

fd=open(fn)
dic={}

for i in fd:
	for j in i.split():
		j=j.lower()
		w=dic.get(j,0)
		w=w+1
		dic[j]=w

#print dic
li=dic.items()

li.sort(key=lambda x:x[1],reverse=True)
#print li

le=[]
print "Top 10 Words by Frequency:-"
for i in range(10):
	if i>=len(li):
		print "Number of Words less than 10"
		break
	else:	
		print i+1,".Word:",li[i][0]," Frequency:",li[i][1]
		le.append(len(li[i][0]))

print "Length of the Words: ",le

avglen=float(reduce(lambda x,y:x+y,le))/len(le)
print "Average Length: %.2f"%(avglen)

sq=[x**2 for x in le if x%2!=0]
print "Squares of Odd Length: ",sq
