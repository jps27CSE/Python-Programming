Real_string=input("enter a word:")

Real_string=Real_string.casefold()

print(Real_string)

Reverse_string=reversed(Real_string)

if list(Real_string)==list(Reverse_string):
    print("Palindrome")
else:
    print("not Palindrome")