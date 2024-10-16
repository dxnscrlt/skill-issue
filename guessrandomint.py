#This program generates a guessing game, with optional conditions.
#Guessing game by importing 'random' library
import random
lower = 0
upper = int(input("Enter a positive integer:\n"))
while upper <= 0:
    if upper <= 0:
        upper = int(input("Invalid input. Try again!\n"))
        continue
    else:
        break
rnum = random.randint(lower, upper)
gnum = int(input(f"Guess what number I'm thinking from {lower} to {upper}...\n"))
attempt = 0
while attempt <= 3:
    if gnum < lower or gnum > upper:
        gnum = int(input(("Invalid number. Try again!\n")))
        continue
    else:
        if rnum != gnum:
            gnum = int(input(f'You guessed wrong! You have {3 - attempt} attempts left.\n'))
            attempt += 1
            if attempt == 3:
                print(f'Game over.\nThe number is {rnum}')
                break
        else:
            print('Congratulations! You guessed right.')
            break
