def check(number):
    result=[]
    for i in range(number):
        if i%3==0 and i%5==0:
            result.append(i)
    return result
        


num=int(input("enter a number:"))

result=check(num)

print(result)

