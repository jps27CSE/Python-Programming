number=int(input("enter a number:"))

count=0
for i in range(2,number):
    if number%i==0:
       count=count+1


if(count==0):
    print("Prime Number")
else:
    print("not a Prime Number")
        