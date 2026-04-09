# Write a program to convert list to tuple.

# Function to convert list to tuple
def convert_list_to_tuple(input_list):
    return tuple(input_list)

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = convert_list_to_tuple(input_list)
print(f"Converted tuple: {result}")

""" Output:
Enter a list of numbers (comma separated): 1,2,3
Converted tuple: (1, 2, 3)
"""