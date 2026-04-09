#Write a program to replace vowels with *.

# Function to replace vowels with *
def hide_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join('*' if char in vowels else char for char in text)
    return result

# Get user input
input_string = input("Enter a string: ")
result = hide_vowels(input_string)
print(f"String with vowels hidden: {result}")

""" Output:
Enter a string: hello
String with vowels hidden: h*ll*
"""