# Write a program to print multiplication table.

# Function to print multiplication table
def print_multiplication_table(n):
    table = [str(n * i) for i in range(1, 11)]
    return " ".join(table)

# Get user input
number = int(input("Enter a number to generate its multiplication table: "))
result = print_multiplication_table(number)
print(f"Multiplication table of {number}: {result}")

""" Output:
Enter a number to generate its multiplication table: 3
Multiplication table of 3: 3 6 9 12 15 18 21 24 27 30
"""