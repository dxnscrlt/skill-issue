#This program is designed to add two rational numbers.
print("Hello! Let's get started on adding two rational numbers.")
a = float(input("Enter the first addend:"))
print("You entered:", a)
b = float(input("Enter the second addend:"))
print("You entered:", b, "\nThe sum is:", a+b)
c = input("Is this correct? (Y/N)")
if c == "Y":
    print("Well done!")
elif c == "N":
    print("Let's try that again!")
else:
    print("I didn't catch that. Could you give me a valid answer? (Y/N)")
