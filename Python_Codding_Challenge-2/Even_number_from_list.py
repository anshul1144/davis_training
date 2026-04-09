# Write a function to return all even numbers from list.


# Function to return all even numbers from a list
def get_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Get user input
input_string = input("Enter a list of numbers (comma separated): ")
input_list = [int(num.strip()) for num in input_string.split(',')]
result = get_even_numbers(input_list)
print(f"Even numbers from the list: {result}")

""" Output:
Enter a list of numbers (comma separated): 1,2,3,4
Even numbers from the list: [2, 4]
"""