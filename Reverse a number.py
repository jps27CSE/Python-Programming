def ReverseNumber(num):
    reverse=0

    while(num>0):
        lastDigit=num%10
        reverse=reverse*10+lastDigit
        num=num//10
    return reverse

userInput=int(input("enter number:"))

result=ReverseNumber(userInput)

print("Reverse is",result)