# Write a program to check if a number is palindrome.

# Function to check if a number is palindrome
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
        
    return original_num == reversed_num

# Get user input
number = int(input("Enter a number: "))
if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a palindrome")
    
""" Output:
Enter a number: 121
Palindrome
"""