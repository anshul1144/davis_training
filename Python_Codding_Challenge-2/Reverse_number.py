# Write a program to reverse a number.

# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num

# Get user input
number = int(input("Enter a number: "))
result = reverse_number(number)
print(f"Reversed number: {result}")

""" Output:
Enter a number: 1234
Reversed number: 4321
"""