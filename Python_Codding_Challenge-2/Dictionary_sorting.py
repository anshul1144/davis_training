#Write a program to sort dictionary by keys.


# Function to sort dictionary by keys
def sort_dictionary_by_keys(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict
# Get user input
input_string = input("Enter a dictionary (e.g., {'b':2,'a':1}): ")
# Convert input string to dictionary
input_dict = eval(input_string)
result = sort_dictionary_by_keys(input_dict)
print(f"Sorted dictionary: {result}")

""" Output:
Enter a dictionary (e.g., {'b':2,'a':1}): {'b':2,'a':1}
Sorted dictionary: {'a': 1, 'b': 2}
"""
