class student:

	def __init__(self,name,usn,marks):
		self.name=name
		self.marks=marks
		self.usn=usn

	def printstudent(self):
		print "\n\nName:%s\nUSN:%s\nMarks: %d,%d,%d"%(self.name,self.usn,self.marks[0],self.marks[1],self.marks[2])


	def calculate(self):
		self.sum=reduce(lambda x,y:x+y,self.marks)
		self.avg=self.sum/float(3)
		self.printstudent()
		print "Sum=%d\nAverage: %0.2f\n"%(self.sum,self.avg)

m=[]
for i in range(3): m.append(int(raw_input("Marks %d:"%(i+1) )))
s1=student(raw_input("Enter Name: "),raw_input("Enter USN: "),m )


s1.calculate()

