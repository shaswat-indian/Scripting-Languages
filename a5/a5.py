
l=[]
n=int(raw_input("Enter Number of Elements: "))
for i in range(n):
	l.append(int(raw_input()))

le=[x for x in l if x%2==0]

print "Even Numbers: ",le

print "Reverse of list: ",l[::-1]

