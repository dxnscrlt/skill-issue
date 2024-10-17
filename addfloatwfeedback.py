#This program is designed to add two rational numbers.
print("Hello! Let's get started on adding two rational numbers.")
c = ''
while c.upper() != 'Y':
    a = float(input("Enter the first addend:"))
    print("You entered:", a)
    b = float(input("Enter the second addend:"))
    print("You entered:", b, "\nThe sum is:", a+b)
    c = input("Is this correct? (Y/N)")
    if c.upper() == "Y":
        print("Well done!")
        break
    elif c.upper() == "N":
        print("Let's try that again!")
        continue
    else:
        print("Invalid input.\nProgram ended.")
#Pending Issue: negative float addends generate incorrect sum estimations.
