def largestnum(num):

    largestnumber=num[0]

    for i in num:
        if i>largestnumber:
            largestnumber=i
    return largestnumber





list=[5,6,7,8,9]

result=largestnum(list)

print(result)