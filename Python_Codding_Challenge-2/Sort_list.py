# Write a program to sort list without using sort().

# Function to sort a list without using sort()
def sort_list(input_list):
    sorted_list = []
    while input_list:
        min_value = min(input_list)
        sorted_list.append(min_value)
        input_list.remove(min_value)
    return sorted_list

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = sort_list(input_list)
print(f"Sorted list: {result}")

""" Output:
Enter a list of numbers (comma separated): 3,1,2
Sorted list: [1, 2, 3]
"""
