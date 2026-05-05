# Write a program to find second largest element.

# Function to find the second largest element in a list
def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two elements."
    
    first_largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
            
    if second_largest == float('-inf'):
        return "There is no second largest element."
    
    return second_largest

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = find_second_largest(input_list)
print(f"The second largest number is: {result}")

""" Output:
Enter a list of numbers (comma separated): 10,20,5,15
The second largest number is: 15
"""