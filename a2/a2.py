
def remdup(li):
	dl=[]
	for i in li:
		if i not in dl:
			dl.append(i)
	return dl

print("Enter Number of Elements: "),
n=int(raw_input());
l=[]
print ("Enters Element in the List:-")
for i in range(n):
	l.append(int(raw_input()))

q=remdup(l)
print "List After Removing Duplicates: ",q
