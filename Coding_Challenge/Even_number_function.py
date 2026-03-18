# program Print all even numbers between 1 to N by using function.
# ....................................................................
# Function to print all even numbers between 1 to N
def print_even_numbers(N):
    """
    Print all even numbers between 1 and N.
    An even number is an integer that is divisible by 2 without leaving a remainder.
    """
    print(f"Even numbers between 1 and {N}:")
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i, end=' ')
# Input the value of N from the user
N = int(input("Enter the value of N: "))
# Call the function to print even numbers
print_even_numbers(N)
# ....................................................................

"""Output:
Enter the value of N: 10
Even numbers between 1 and 10:
2 4 6 8 10
"""