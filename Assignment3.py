#question 1
print("Question 1")
sentence= input("Please give an input:")
sentence=sentence.lower().strip()
i=0
dict={}
if " " not in sentence:
    while i<len(sentence):
        counter=0
        k=0
        while k<len(sentence):
            if sentence[i]==sentence[k]:
                counter=counter+1
                k=k+1
            else:
                k=k+1
        dict[f"{sentence[i]}"]=counter
        i=i+1
else:
    list=str.split(sentence)
    while i<len(list):
        counter=0
        k=0
        while k<len(list):
            if list[i]==list[k]:
                counter=counter+1
                k=k+1
            else:
                k=k+1
        dict[f"{list[i]}"]=counter
        i=i+1
print("Total occurences")
for key,value in dict.items():
    print(f"{key}-{value}")


#question2
print("question 2")
day=int(input("please enter day:"))
month=int(input("please enter month:"))
year=int(input("please enter year:"))

if day>30 and month in{2,4,6,9,11}:
    condition=False
elif day>31 and month in{1,3,5,7,8,10,12}:
    condition=True
elif(day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True

if condition:
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    print(f"Next Date is:{next_day}/{n_month}/{n_year}")
else:
    print("this is not a valid date")

#question 3
print("Question 3")
list1=[5,7,19,24]
print(list1)

list2=[]
for x in list1:
    tuple=(x,x**2)
    list2.append(tuple)
print(list2)

#question 4
print("question 4")
grade=int(input("enter grade points:"))
dict={10:{'grade_inp':'A+','remarks':'Outstanding'},
      9:{'grade_inp':' A','remarks':'Excellent'},
      8:{'grade_inp':' B+','remarks':'Very Good'},
      7:{'grade_inp':' B','remarks':'Good'},
      6:{'grade_inp':' C+','remarks':'Average'},
      5:{'grade_inp':' C','remarks':'Below Average'},
      4:{'grade_inp':' D','remarks':'Poor'}}
if 3<grade<11:
    for key in dict.keys():
        if key==grade:
            value=dict[key]
            print(f"Your Grade is{value['grade_inp']} and {value['remarks']} performance")
        else:
            continue
else:
    print('Error!')


#ques no.5
print('question 5')
alphabets=['A','B','C','D','E','F','G','H','I','J','K']
for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ",end="")
        else:
            print(alphabets[counter],end="")
            counter=counter+1
        column=column+1
    print("")



#Question 6
print("Question 6")
condition=True
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student: "))
        name=input("Please enter the name of the Student: ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N:")
        condition = True
    else:
        condition = False
print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
    print("")



#Question 7
print("Question 7")
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

a_n1=1
a_n2=0
n=0

sum=a_n1+a_n2

print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)

while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number

print(f"Average of total {number} terms of sequence is {average}")
print("END")

#Question 8
print("Question 8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Part a")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

print("Part b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

print("Part C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

print("Part d")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

print("Part e")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")


    
    
