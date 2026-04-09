# Write a program to find common elements between lists.

# Function to find common elements between two lists
def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)

# Get user input for two lists
input_string1 = input("Enter the first list of numbers (comma separated): ")
input_string2 = input("Enter the second list of numbers (comma separated): ")
list1 = [int(num.strip()) for num in input_string1.split(',')]
list2 = [int(num.strip()) for num in input_string2.split(',')]

common_elements = find_common_elements(list1, list2)
print(f"Common elements between the two lists: {common_elements}")

""" Output:
Enter the first list of numbers (comma separated): 1,2,3
Enter the second list of numbers (comma separated): 2,3,4
Common elements between the two lists: [2, 3]
"""