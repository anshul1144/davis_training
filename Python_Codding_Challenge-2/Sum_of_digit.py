# Write a program to find sum of digits.

# Function to calculate the sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

# Get user input
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"Sum of digits: {result}")

""" Output:
Enter a number: 123
Sum of digits: 6
"""