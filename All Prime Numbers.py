def check_prime(num):

    for i in range(2,num):
        if (num%i)==0:
            return False
    return True

def all_prime(num):
    primes=[]

    for n in range(2,num+1):
        if check_prime(n) is True:
            primes.append(n)
    return primes

num=int(input("enter number: "))

prime=all_prime(num)

print(prime)