# Write a program to find duplicate characters.

# Function to find duplicate characters in a string
def find_duplicate_characters(text):
    char_count = {}
    duplicates = set()

    for char in text:
        if char in char_count:
            char_count[char] += 1
            duplicates.add(char)
        else:
            char_count[char] = 1

    return ' '.join(duplicates)

# Get user input
input_string = input("Enter a string: ")
result = find_duplicate_characters(input_string)
print(f"Duplicate characters: {result}")

""" Output:
Enter a string: programming
Duplicate characters: r g m
"""