# Write a program to verify two strings are anagrams.

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)
# Get user input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("True")
else:
    print("False")
    
""" Output:
Enter the first string: listen
Enter the second string: silent
True
"""