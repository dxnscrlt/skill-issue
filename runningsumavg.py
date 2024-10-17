#Running Sum and Average
sum = 0
count = 0
breaker = ''

#Initial Number
init = int(input(f'Enter the first number:\n'))
sum += init
count += 1
print(f'The current sum is {sum}.\nThe current average is {sum/count:.1f}.')

#Running Sum and Average
while breaker.upper() != 'X':
    next = int(input(f'Enter the next number:\n'))
    sum += next
    count += 1
    print(f'The current sum is {sum}.\nThe current average is {sum/count:.1f}.')
    breaker = str(input(f'Enter "X" to exit the program. Enter any other character to continue.'))

#Final Sum and Average
if breaker.upper() == 'X':
    print(f'The final sum is {sum}.\nThe final average is {sum/count:.1f}.\nProgram ended. Thank you!')
