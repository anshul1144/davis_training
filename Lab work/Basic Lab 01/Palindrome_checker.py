
""" Write a function:

Check if a number/string is palindrome
Use loop (while or for)
Use if-else to print result """


def is_palindrome(value):
    # Convert input to string so function works for both numbers and text
    text = str(value)
    reversed_text = ""

    # Build reversed string using a for loop
    for char in text:
        reversed_text = char + reversed_text

    # Return True if original and reversed values are same
    return text == reversed_text


# Take input from user
user_input = input("Enter a number or string: ")

# Use if-else to print result
if is_palindrome(user_input):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
