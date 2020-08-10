number1=int(input("enter number 1:"))

number2=int(input("enter number 2:"))

for i in range(1,number1+1 and number2+1):

    if number1%i==0 and number2%i==0:
        gcd=i


print(gcd)