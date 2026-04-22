
""" Create a function:

Takes a number from user
Uses for loop to print table (1–10)
Use if to restrict negative input """


def generate_table(number):
    # Print multiplication table from 1 to 10
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Take number input from user
num = int(input("Enter a number: "))

# Restrict negative input using if
if num < 0:
    print("Negative numbers are not allowed")
else:
    generate_table(num)
