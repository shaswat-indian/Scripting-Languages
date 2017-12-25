from operator import itemgetter

def ctof(ip):
	op=(1.8*ip)+32
	print "Temperature in Fahrenheit: ",op
	return op

def ftoc(ip):
	op=float((ip-32))/(1.8)
	print "Temperature in Celcius: ",op
	return op

def ctok(ip):
	op=ip+273
	print "Temperature in Kelvin: ",op
	return op


def ktoc(ip):
	op=ip-273
	print "Temperature in Celcius: ",op
	return op


def ftok(ip):
	op=((ip-32)/(1.8))+273
	print "Temperature in Kelvin: ",op
	return op

def ktof(ip):
	op=((ip-273)*1.8)+32
	print "Temperature in Fahrenheit: ",op
	return op


conversions=[]

ch='y'
while ch=='y':
	print "\n\n\t\t**MENU**"
	print "1.Celcius to Fahrenheit"
	print "2.Fahrenheit to Celcius"
	print "3.Celcius to Kelvin"
	print "4.Kelvin to Celcius"
	print "5.Fahrenheit to Kelvin"
	print "6.Kelvin to Fahrenheit"
	print "7.View Previous Conversions"
	print "8.Exit"
	ch=int(raw_input("Enter Your Choice: "))

	if(ch==1):
		ip=float(raw_input("Enter Temperature in Celcius: "))
		op=ctof(ip)
		conversions.append(('C',ip,'F',op))
	
	elif(ch==2):
		ip=float(raw_input("Enter Temperature in Fahrenheit: "))
		op=ftoc(ip)
		conversions.append(('F',ip,'C',op))

	elif(ch==3):
		ip=float(raw_input("Enter Temperature in Celcius: "))
		op=ctok(ip)
		conversions.append(('C',ip,'K',op))

	elif(ch==4):
		ip=float(raw_input("Enter Temperature in Kelvin: "))
		op=ktoc(ip)
		conversions.append(('K',ip,'C',op))

	elif(ch==5):
		ip=float(raw_input("Enter Temperature in Fahrenheit: "))
		op=ftok(ip)
		conversions.append(('F',ip,'K',op))

	elif(ch==6):
		ip=float(raw_input("Enter Temperature in Kelvin: "))
		op=ktof(ip)
		conversions.append(('K',ip,'F',op))

	elif(ch==7):
		print "\n\n\t\t**Display MENU**"
		print "1.Ascending Order of FROM Value"
		print "2.Descending Order of FROM Value"
		print "3.Ascending Order of TO Value"
		print "4.Descending Order of TO Value"
		ch=int(raw_input("Enter Your Choice: "))

		if(len(conversions)==0):
			print "No Conversions Found!"

		elif(ch==1):
			c=sorted(conversions,key=itemgetter(1))
			for i in c:
				print i

		elif(ch==2):
			c=sorted(conversions,key=itemgetter(1),reverse=True)
			for i in c:
				print i

		elif(ch==3):
			c=sorted(conversions,key=itemgetter(3))
			for i in c:
				print i

		elif(ch==4):
			c=sorted(conversions,key=itemgetter(3),reverse=True)
			for i in c:
				print i
		
		else:
			print "Invalid Choice!"
	
	elif(ch==8):
		quit("Exiting Program..")

	else:
		print "Invalid Choice!"

	ch=str(raw_input("Do you wish to Continue?(y/n): "))




