import random

randomNUmbers = random.randint(1,9)

chance=0

print("Gues the number (between 1 to 9)")


while chance < 5:

    guess=int(input("enter the number:"))

    if guess == randomNUmbers:
        print("You won!!!")
        break

    elif guess < randomNUmbers:
        print("your guess number is low")
    else:
        print("your guess number is high")

    chance+=1

    if not chance < 5:
        print(f"you loss!! the number is {randomNUmbers}")