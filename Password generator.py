import string 
import random 

def genarate_pass(size):

    all_char=string.ascii_letters+string.digits+string.punctuation

    password=""

    for char in range(size):
        rand_char=random.choice(all_char)
        password=password+rand_char
    return password


pass_len=int(input("How many characters in your password?"))
new_password=genarate_pass(pass_len)

print("Your new password:",new_password)