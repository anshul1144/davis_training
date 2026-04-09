# Write a program to find longest word.

# Function to find the longest word in a given string
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

# Get user input
input_string = input("Enter a string: ")
result = find_longest_word(input_string)
print(f"The longest word is: {result}")

""" Output:
Enter a string: I love programming
The longest word is: programming
"""