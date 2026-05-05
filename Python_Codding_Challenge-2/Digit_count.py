# Write a program to count number of digits.

# Function to count number of digits
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

# Get user input
number = int(input("Enter a number: "))
result = count_digits(number)
print(f"Number of digits: {result}")

""" Output:
Enter a number: 45678
Number of digits: 5
"""
