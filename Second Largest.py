def SecondLargest(number):
    largest=number[0]
    secondlargest=number[0]

    for i in range(1,len(number)):
        if number[i] > largest:
            secondlargest=largest
            largest=number[i]
        elif number[i] > secondlargest:
            secondlargest=number[i]
    return secondlargest


num=[1,2,3,4,5,6,7]

result=SecondLargest(num)

print(result)