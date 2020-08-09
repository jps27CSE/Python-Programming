def squares(number):
    final=0
    for i in range(number+1):
        square=(i**2)
        final=final+square
    return final


inNumber=int(input("enter a number:"))

result=squares(inNumber)

print(result)