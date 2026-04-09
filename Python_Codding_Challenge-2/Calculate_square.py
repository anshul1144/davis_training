# Write a function to return square of a number.

# Function to calculate the square of a number
def calculate_square(num):
    return num ** 2
# Get user input
number = int(input("Enter a number: "))
result = calculate_square(number)
print(f"The square of {number} is: {result}")

""" Output:
Enter a number: 5
The square of 5 is: 25
"""