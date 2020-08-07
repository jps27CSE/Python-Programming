#File IO

with open("birds.txt",mode="r") as b_file:
    for line in b_file.readlines():
        print(line, end="")


#Loop

for i in range(0,10,2):
    print(i)

grocery_list=["rice","toamto","potato","water"]

for item in grocery_list:
    if item=="rice":
        continue
    print(item)

def is_even(number):
    if number%2 ==0:
        return True
    else:
        return False

starting=0
even_list=[]
userinput=int(input("Enter a number"))
while starting < userinput:
    if is_even(starting):
        print(f"{starting} is Even number")
        even_list.append(starting)
    else:
        print(f"{starting} is Odd number") 

    starting=starting+1  

print(even_list)

for starting in range(starting,userinput+1): 
    if is_even(starting):
        print(f"{starting} is Even Number")

#Condition

marks=int(input("Enter your marks: "))

def print_marks(grade):
    print(f"You Got:{grade}")



if marks >= 80:
    print_marks("A+")
elif marks <80 and marks >= 70:
    print_marks("A")
elif marks <70 and marks >= 60:
    print_marks("A-")

else:
    print_marks("Passed")


if marks > 80 or marks < 10:
    print("You are good or bad")
    if marks >=80:
        print("Your are awesome")
    elif marks <=10:
        print("You are Normal")


#List

grocery_list=["rice","potato","tomato"]

print(grocery_list)

grocery_list.append("water") #adding items by using (append)

print(grocery_list)

l2=list()

print(l2)

l2.append(2)

print(l2)

l2.append("Computer")

print(l2)


print(grocery_list[-1])

print(grocery_list[1])

grocery_list.sort()

print(grocery_list)

number=[1,2,8,3,7,6]
number.sort()
print(number)
numberlist=sorted(number)
print(numberlist)

#String

name="Jack Pritom Soren"
mood=" Loves"
tech=" Computer"

value=27

jack_value=name+" "+str(value) #converting value intro string by using (str)

print(jack_value)

addition=name+mood+tech

print(addition)

print(f"Length:{len(jack_value)}")



#Arithmetic Operation

first_number=10
second_number=20

addition=first_number+second_number
subtraction=first_number-second_number
mul=first_number * 2
div=first_number // 5 

print(f"Addition:{addition}")
print(f"Subtraction:{subtraction}")
print(f"Multiplication:{mul}")
print(f"Division:{div}")



#Function

def add_two_values(first,second):
    return first+second

number_1=10
number_2=3

sum=add_two_values(number_1,number_2)

print(f"{number_1}+{number_2}={sum}")


#Basic Input/Output
username=input("Your name:")  

print("Hello {}!".format(username))

