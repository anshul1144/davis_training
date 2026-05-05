# Write a program to find intersection.

# Function to find intersection of two sets
def intersection_of_sets(set1, set2):
    intersection_set = set1 & set2
    return intersection_set

# Get user input for two sets
input_string1 = input("Enter the first set of numbers (comma separated): ")
input_string2 = input("Enter the second set of numbers (comma separated): ")
set1 = set(int(num.strip()) for num in input_string1.split(','))
set2 = set(int(num.strip()) for num in input_string2.split(','))
result = intersection_of_sets(set1, set2)
print(f"Intersection of the two sets: {result}")    

""" Output:
Enter the first set of numbers (comma separated): 1,2
Enter the second set of numbers (comma separated): 2,3
Intersection of the two sets: {2}
"""