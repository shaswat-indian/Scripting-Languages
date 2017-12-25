import pandas as pd
import matplotlib.pyplot as plt


fname=raw_input("Enter filename: ")
df=pd.read_csv(fname)

print "Headers of the Dataset are :-"
#print df.columns.values 
print df.head(0)


print "**Dataset Description**"
print df.info()
print df.describe()



df=df.drop(["Pclass","PassengerId","Parch","Name"],axis=1)
print "\n\nAfter Dropping Unwanted Columns:-\n",df.head(0)



print "\nWith Empty Column Values:-\n",df
df['Cabin']=df["Cabin"].fillna("CC55")
print "\n\nWithout Empty Column Values:-\n",df




print "\n\nNumber of Entries: ",len(df)
print "\nNumber of Columns: ",len(df.columns)



print "\n\nAttributes and Their Datatypes:-\n"
df.info()


print "\nMinimum Age: ",df['Age'].min()
print "\nMaximum Age: ",df['Age'].max()
print "\nMean Age: ",round(df['Age'].mean(),2)


gp=df['Age'].plot.hist()
gp.set_ylabel("Number of People")
gp.set_xlabel("Age")
gp.set_title("Age vs No. of People")
plt.show()



dgp=df.Age.plot()
dgp.set_ylabel("Age")
dgp.set_xlabel("Number of People")
dgp.set_title("Age vs No. of People")
plt.show()


