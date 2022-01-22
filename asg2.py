#ques no.1
var1="python is a case sensitive language"
print(len(var1))
print(var1[::-1])
print(var1[10:26])
print(var1.replace("a case sensitive","object oriented"))
print(var1.find("a"))
print(var1.replace(" ",""),end="\n")


#ques no.2
var1="hey, Himanshu Bansal here!\n"
var2="My sid is 21105050\n"
var3="I am from electronics and communication department\n"
var4="my cgpa is 9.9\n"
print(var1,var2,var3,var4)


#ques no.3
a=56
b=10
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)
#left shift both a and b with 2 bits.
print("a<<2:",a<<2,"\tb<<2:",b<<2)
# right shift a with 2 bits and b with 4 bits.
print("a>>2:",a>>2,"\tb>>2:",b>>4,end="\n")



#ques no.4
a=int(input("enter the 1st no:"))
b=int(input("enter the second no:"))
c=int(input("enter the 3rd no:"))
if a>b:
    if a>c:
        highest_number=a
    else:
        highest_number=c
if b>a:
    if b>c:
        highest_number=b
    else:
        highest_number=c
print("the highest number is:",(highest_number))



#ques no.5
input_string=input("Enter input string:")
if "name" in input_string:
    print("yes")
else:
    print("no")


#ques no.6
a=int(input("enter the 1st lenght:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if a+b>c and a+c>b and b+c>a:
    print("yes")
else:
    print("no")



