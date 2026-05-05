# Create a module with a function to add two numbers and import it.

# importing the function from the module
from calculation_module import add_two_numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = add_two_numbers(number1, number2)
print(result)
