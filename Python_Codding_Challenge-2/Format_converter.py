# Write a program to convert string to uppercase without built-in methods.

# Function to convert string to uppercase without built-in methods
def to_uppercase(s):
    uppercase_string = ""
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by calculating the ASCII value
            uppercase_char = chr(ord(char) - (ord('a') - ord('A')))
            uppercase_string += uppercase_char
        else:
            # If it's not a lowercase letter, keep it as is
            uppercase_string += char
    return uppercase_string

# Get user input
input_string = input("Enter a string: ")
result = to_uppercase(input_string)
print(f"Uppercase string: {result}")

""" Output:
Enter a string: hello
Uppercase string: HELLO
"""
