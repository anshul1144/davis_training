# Program to find the HCF of two numbers
# input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#..................................................
if num2 == 0:
    print("HCF is", num1)
else:
    while num2 != 0:
        rem = num1 % num2
        num1 = num2
        num2 = rem
#..................................................
    print("HCF is", num1)
    
""" Output:
Enter the first number: 48
Enter the second number: 18
HCF is 6
"""