# Write a program to count unique elements.

# Function to count unique elements in a list
def count_unique_items(input_list):
    unique_items = set(input_list)
    return len(unique_items)

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = count_unique_items(input_list)
print(f"Number of unique items: {result}")

""" Output:
Enter a list of numbers (comma separated): 1,1,2,3,3
Number of unique items: 3
"""