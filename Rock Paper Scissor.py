def Game(first,second):
    if first == second:
        return "Tie"
    elif first=='rock':
        if second == 'scissors':
            return "First player wins!"
        else:
           return "Second Player wins!"
    elif first == 'scissors':
       if second == 'paper':
           return "First player win!"
       else:
           return"Second player wins!"
    elif first == 'paper':
       if second == 'rock':
           return "First player wins!"
       else:
           return "Second player win!"
    else:
       return "Invalid input!"


first_person=input("First player: rock, paper or scissors:")
second_person=input("Second player: rock, paper or scissors:")

result=Game(first_person,second_person)

print(result)