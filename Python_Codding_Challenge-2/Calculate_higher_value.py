# Write a program to count numbers greater than 50 in a list.

# Function to count numbers greater than 50 in a list
def count_higher_value(numbers):
    count = sum(1 for num in numbers if num > 50)
    return count
# Get user input for the list of numbers
input_numbers = input("Enter a list of numbers: ")
# Convert the input string to a list of integers
numbers_list = [int(num.strip()) for num in input_numbers.split(",")]
# Count the numbers greater than 50
result = count_higher_value(numbers_list)
print(f"Count of numbers greater than 50: {result}")

""" Output:
Enter a list of numbers: 10,60,30,80
Count of numbers greater than 50: 2
"""