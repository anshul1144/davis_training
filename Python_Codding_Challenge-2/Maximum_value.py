# Write a program to find max without using built-in functions.

# Function to find maximum value in a list
def find_maximum(numbers):
    if not numbers:
        return "The list is empty."
    
    max_value = numbers[0]  # Initialize max_value with the first element
    for num in numbers:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found
    return max_value

# Get user input
input_numbers = input("Enter a list of numbers : ")
numbers_list = [int(num.strip()) for num in input_numbers.split(",")]  
# Convert input string to a list of integers
result = find_maximum(numbers_list)
print(f"The maximum value in the list is: {result}")

""" Output:
Enter a list of numbers : 5,8,2
The maximum value in the list is: 8
"""