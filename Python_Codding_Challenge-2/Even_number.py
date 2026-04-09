# Write a program to print all even numbers from 1 to N.


# Function to print even numbers from 1 to N
def print_even_numbers(n):
    even_numbers = [str(num) for num in range(1, n + 1) if num % 2 == 0]
    return " ".join(even_numbers)

# Get user input
N = int(input("Enter a number N: "))
result = print_even_numbers(N)
print(f"Even numbers from 1 to {N}: {result}")

""" Output:
Enter a number N: 10
Even numbers from 1 to 10: 2 4 6 8 10
"""