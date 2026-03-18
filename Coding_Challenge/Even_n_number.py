# Program to print even numbers using while loop
# ....................................................................
N = int(input("Enter N: "))
i = 2

print(f"Even numbers between 1 and {N}:")
while i <= N:
    print(i, end=" ")
    i += 2
# ....................................................................
"""
Output:
Enter N: 8
2 4 6 8
"""