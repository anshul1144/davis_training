# Write a program to check if string is palindrome.


# Function to check if a string is palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get user input
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Yes")
else:
    print("No")
    



""" Output:
Enter a string: madam
Yes
"""
