def dec_to_binary(n):
   if n > 1:
       dec_to_binary(n//2)
   print(n % 2,end = '')

num = int(input("Your decimal number: "))
dec_to_binary(num)
print(" ")