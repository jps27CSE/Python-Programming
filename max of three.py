num1=int(input("enter number 1:"))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))

if num1> num2 and num1 > num3:
    print(f"{num1} is max")
elif num2 > num1 and num2 > num3:    #method 1
    print(f"{num2} is max")

else:
    print(f"{num3} is max")


largest=max(num1,num2,num3)
                                     #method 2
print("max number is ",largest)

