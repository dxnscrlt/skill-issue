#This program generates a guessing game, with optional conditions.
import random
print("Welcome to the Number Guessing Game! Let's get started.")

#Setting the upper limit:
lower = 0
upper = int(input("Enter a positive integer:\n"))
while upper <= 0:
    upper = int(input("Invalid input. Try again!\n"))
    
#Choosing handicap conditions:
oddeven = str(input("Would you like to know if the number is odd or even? Y/N\n"))
while oddeven.lower() != 'y' and oddeven.lower() != 'n':
    oddeven = str(input("Invalid input. Try again!\n"))
highlow = str(input("Would you like to know if your current guess is higher or lower than the number? Y/N\n"))
while highlow.lower() != 'y' and highlow.lower() != 'n':
    highlow = str(input("Invalid input. Try again!\n"))

#Game
rnum = random.randint(lower, upper)
if oddeven.lower() == 'y':
    if rnum % 2 == 0:
        print(f'The number I\'m thinking is even.')
    else:
        print(f'The number I\'m thiniking is odd.')
gnum = int(input(f"Guess what number I'm thinking from {lower} to {upper}...\n"))
attempt = 0
while attempt <= 3:
    if gnum < lower or gnum > upper:
        gnum = int(input(("Invalid number. Try again!\n")))
        continue
    else:
        if rnum != gnum:
            if highlow.lower() == 'y':
                if gnum > rnum:
                    print(f'{gnum} is too high.')
                elif gnum < rnum:
                    print(f'{gnum} is too low.')
            gnum = int(input(f'You guessed wrong! You have {3 - (attempt + 1)} attempts left.\n'))
            attempt += 1
            if attempt == 3 and rnum != gnum:
                print(f'Game over.\nThe number is {rnum}')
                break
        else:
            print('Congratulations! You guessed right.')
            break
