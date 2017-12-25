from flask import Flask,session,url_for,request,redirect,render_template

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def student():
	if(request.method=="GET"):
		return render_template("b4.html")

	if(request.method=="POST"):
		uname=request.form["uname"]
		usn=request.form["usn"]
		dob=request.form["dob"]
		marks=request.form.getlist("marks[]")
		credits=request.form.getlist("credits[]")
		marks=list(map(int,marks))
		credits=map(int,credits)
		l=[]
		gpa=0
		for i in range(len(marks)):
			grade=getgrade(marks[i])
			gp=getgp(grade)
			gpa=gpa+(credits[i]*gp)
			l.append({"no":i+1,"marks":marks[i],"credits":credits[i],"grade":grade})

		sumcredits=reduce(lambda x,y:x+y,credits)
		sgpa=float(gpa)/sumcredits
		sgpa=round(sgpa,2)
		return render_template("b4s.html",uname=uname,usn=usn,dob=dob,cart=l,sgpa=sgpa)
			

def getgrade(ip):
	if(ip>=90):
		return 'S'
	elif(ip>=75):
		return 'A'
	elif(ip>=60):
		return 'B'
	elif(ip>=50):
		return 'C'
	elif(ip>=40):
		return 'D'
	else:
		return 'F'


def getgp(g):
	if(g=='S'):
		return 10
	elif(g=='A'):
		return 9
	elif(g=='B'):
		return 8
	elif(g=='C'):
		return 7
	elif(g=='D'):
		return 6
	elif(g=='F'):
		return 0


if(__name__=='__main__'):
	app.run()

