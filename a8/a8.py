
def findmax(l):
	if(len(l)==1):
		return l[0]
	else:
		rem=l[1:]
		if(l[0]>findmax(rem)):
			return l[0]
		else:
			return findmax(rem)

l=[]
n=int(raw_input("Enter No. of Elements: "))
print "Enter the Elements:-"
for i in range(n):
	l.append(int(raw_input()))

print "Largest Number: ",findmax(l)
