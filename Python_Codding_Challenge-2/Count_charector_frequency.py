# Write a program to count occurrences of a character.

# Function to count occurrences of a character
def count_character_frequency(text, character):
    count = text.count(character)
    return count

# Get user input
input_string = input("Enter a string: ")
input_character = input("Enter a character to count: ")
result = count_character_frequency(input_string, input_character)
print(f"Number of occurrences of '{input_character}': {result}")

""" Output:
Enter a string: banana
Enter a character to count: a
Number of occurrences of 'a': 3
"""