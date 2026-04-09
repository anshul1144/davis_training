# Write a program to remove duplicates from list.

# Function to remove duplicates from a list
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Get user input
input_string = input("Enter a list of numbers : ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = remove_duplicates(input_list)
print(f"List after removing duplicates: {result}")

""" Output:
Enter a list of numbers : 1,1,2,3
List after removing duplicates: [1, 2, 3]
"""