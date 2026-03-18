# calculate the sum of two numbers using a module
#..................................................
# import the module
from Modules.Numeric_calculations.Arthematic_operation import calculate_sum

# input from user
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
# calculate the sum using the module function
print("Sum =", calculate_sum(number1, number2))
#..................................................