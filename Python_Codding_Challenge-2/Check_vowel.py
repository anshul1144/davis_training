# Write a program to check if a character is a vowel.


# Function to check if a character is a vowel
def is_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return "Vowel"
    else:
        return "Not a Vowel"
    
# Get user input
character = input("Enter a character: ")
result = is_vowel(character)
print(result)

""" Output:
Enter a character: e
Vowel
"""