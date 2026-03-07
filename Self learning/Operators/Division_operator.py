#  program to find the remainder and quotient when one number is divided by another
#.......................................................................
# taking input from the user
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

#Displaying the numbers entered by the user
print("The first number is: ", num1)
print("The second number is: ", num2)

# calculating the quotient and remainder

#Displaying the quotient
print(".................Quotient.................")
print("The quotient is: ", num1 // num2)
#Displaying the remainder
print(".................Remainder.................")
print("The remainder is: ", num1 % num2)
#........................................................................

""" Output:
Enter the first number: 10
Enter the second number: 3
The first number is:  10
The second number is:  3
.................Quotient.................
The quotient is:  3
.................Remainder.................
The remainder is:  1
"""