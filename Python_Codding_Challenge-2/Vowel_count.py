# Write a program to count vowels in a string.

# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count
# Get user input
input_string = input("Enter a string: ")
result = count_vowels(input_string)
print(f"Number of vowels in the string: {result}")

""" Output:
Enter a string: hello
Number of vowels in the string: 2
"""
