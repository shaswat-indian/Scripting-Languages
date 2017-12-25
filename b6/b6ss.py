from flask import Flask,session,render_template,request,redirect,url_for

app=Flask(__name__)

app.secret_key="mysecret1"

@app.route("/",methods=["GET","POST"])
def atm():
	try:
		balance=session['balance']
		transaction=session['transaction']
	except KeyError:
		balance=session['balance']=0
		transaction=session['transaction']=0

	if(request.method=="GET"):
		return render_template("b6.html",balance=balance,transaction=transaction,msg="")

	if(request.method=="POST"):
		if(transaction==5):
			msg="5 Transactions Completed!"
			session.clear()
			return render_template("b6.html",balance=0,transaction=0,msg=msg)

		if(request.form["action"]=="Withdraw"):
			if(int(request.form["amount"])>balance):
				msg="Cannot Withdraw more than Balance!"
				return render_template("b6.html",balance=balance,transaction=transaction,msg=msg)
			else:
				balance=balance-int(request.form["amount"])
				transaction=transaction+1
				session['balance']=balance
				session['transaction']=transaction
				msg="Amount Withdrawn Successfully!"
				return render_template("b6.html",balance=balance,transaction=transaction,msg=msg)

		if(request.form["action"]=="Deposit"):
			balance=balance+int(request.form["amount"])
			transaction=transaction+1
			session['balance']=balance
			session['transaction']=transaction
			msg="Amount Deposited Successfully!"
			return render_template("b6.html",balance=balance,transaction=transaction,msg=msg)
		
				

if(__name__=='__main__'):
	app.run()
