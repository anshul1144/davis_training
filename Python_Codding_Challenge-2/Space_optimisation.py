# Write a program to remove spaces from string.

# Function to remove spaces from a string
def remove_spaces(text):
    return text.replace(" ", "")
# Get user input
input_string = input("Enter a string: ")
result = remove_spaces(input_string)
print(f"String without spaces: {result}")

""" Output:
Enter a string: hello world
String without spaces: helloworld
"""