def CUB(num):
    sum=0
    for i in range(num+1):
        sum=sum+num**3
    return sum

userInput=int(input("enter a number:"))
result=CUB(userInput)

print(result)