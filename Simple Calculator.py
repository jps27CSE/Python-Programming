def add(num1,num2):
    return num1+num2 

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1//num2

def module(num1,num2):
    return num1%num2

num1=int(input("Enter number 1:"))

operation=input("what do you want to do + , - , * , / , % :")

num2=int(input("Enter number 2:"))

result=0

if operation == "+":
    result=add(num1,num2)

elif operation =="-":
    result=substract(num1,num2)
elif operation =="*":
    result=multiply(num1,num2)
elif operation =="/":
    result=divide(num1,num2)
elif operation =="%":
    result=module(num1,num2)



print(result)