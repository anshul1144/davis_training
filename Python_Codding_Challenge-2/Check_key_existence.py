# Write a program to check if key exists in dictionary.

# Function to check if key exists in dictionary
def check_key_existence(dictionary, key):
    if key in dictionary:
        return "Yes"
    else:
        return "No"
    
# Get user input
input_dict = input("Enter a dictionary (e.g., {'a':1,'b':2}): ")
key_to_check = input("Enter the key to check: ")
# Convert input string to dictionary
dictionary = eval(input_dict)
result = check_key_existence(dictionary, key_to_check)
print(result)

""" Output:
Enter a dictionary (e.g., {'a':1,'b':2}): {'a':1,'b':2}
Enter the key to check: a
Yes
"""