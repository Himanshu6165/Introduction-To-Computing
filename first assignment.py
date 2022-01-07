#ques no.1
print("enter the value of number1")
var1=input()
print("enter the value of number2")
var2=input()
print("enter the value of number3")
var3=input()
print("the average of these 3 numbers is" , (int(var1)+int(var2)+int(var3))/3 )

#ques no.2
standard_deduction=10000
tax_rate=0.20
dependent_deduction=3000
print("enter gross income")
gross_income=input()
print("no of dependents are")
no_of_dependents=input()
taxable_income=(int(gross_income)-standard_deduction-(dependent_deduction*int(no_of_dependents)))
tax=taxable_income*tax_rate
print("your tax is $",tax )

#ques no.3
#storing different datatypes in a list
print(['21505081','any','M','ece', '9.87'])

#ques no.4
#list containing marks of 5 students out of 100
marks=[92 ,88,40,76,23]
marks.sort()
print(marks )

#ques no.5(a)
color=['red','green','white','black','pink','yellow']
color.pop(3)
print(color )

#ques no 5(b)
color=['red','green','white','black','pink','yellow']
color[3:5]=[]; color.insert(3,'purple')
print(color)
