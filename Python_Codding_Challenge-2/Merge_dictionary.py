# Write a program to merge dictionaries.


# Function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Get user input
input_string1 = input("Enter the first dictionary (e.g., {'a':1}): ")
input_string2 = input("Enter the second dictionary (e.g., {'b':2}): ")
# Convert input strings to dictionaries 

dict1 = eval(input_string1)
dict2 = eval(input_string2)
result = merge_dictionaries(dict1, dict2)
print(f"Merged dictionary: {result}")

""" Output:
Enter the first dictionary (e.g., {'a':1}): {'a':1}
Enter the second dictionary (e.g., {'b':2}): {'b':2}
Merged dictionary: {'a': 1, 'b': 2}
"""