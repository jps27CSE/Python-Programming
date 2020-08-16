def reverse_String(userInput):

    stack=[]

    for char in userInput:
        stack.append(char)

    rev=''

    while len(stack) > 0:

      last=stack.pop()

      rev=rev+last 

    return rev

userInput=input("enter your string:")

result=reverse_String(userInput)

print(result)