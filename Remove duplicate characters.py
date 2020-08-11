def remove_duplicate(user_input):
    result=''

    for char in user_input:
        if char not in result:
            result=result+char
    return result

user_input=input("enter your string:")

no_duplicate=remove_duplicate(user_input)

print(no_duplicate)