# Write a program to find union of two sets.

# Function to find union of two sets
def union_of_sets(set1, set2):
    union_set = set1 | set2
    return union_set

# Get user input for two sets
input_string1 = input("Enter the first set of numbers (comma separated): ")
input_string2 = input("Enter the second set of numbers (comma separated): ")
set1 = set(int(num.strip()) for num in input_string1.split(','))
set2 = set(int(num.strip()) for num in input_string2.split(','))
result = union_of_sets(set1, set2)
print(f"Union of the two sets: {result}")

""" Output:
Enter the first set of numbers (comma separated): 1,2
Enter the second set of numbers (comma separated): 2,3
Union of the two sets: {1, 2, 3}
"""