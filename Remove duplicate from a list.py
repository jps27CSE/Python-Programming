test_list=[1,2,3,4,3,5,4,2]

print(f"original list is: {test_list}")

rest=[]

for i in test_list:
    if i not in rest:
        rest.append(i)


print(f"the list after removing duplicates {rest} ")