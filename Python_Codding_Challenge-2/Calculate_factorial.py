# Write a program to compute factorial of a number.

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
# Get user input
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print(f"Factorial of {number} is: {result}")

""" Output:
Enter a number to calculate its factorial: 5
Factorial of 5 is: 120
"""