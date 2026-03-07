# program to check divisibility when one number is divided by another.

#....................................................................................
# take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the numbers entered by the user
print("The first number is: ", num1)
print("The second number is: ", num2)

# calculate the remainder
print(".......................Remainder.............................")
print("Remainder when ", num1, " is divided by ", num2, " is: ", num1 % num2)

# calculate the quotient
print(".......................Quotient.............................")
print("Quotient when ", num1, " is divided by ", num2, " is: ", num1 // num2)

#...................................................................................

"""output:
Enter the first number: 10
Enter the second number: 3
The first number is:  10
The second number is:  3
Remainder when  10  is divided by  3  is:  1
Quotient when  10  is divided by  3  is"""