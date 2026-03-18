# Program to print even numbers (range step)
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
print(*range(2, N+1, 2))
# ....................................................................
"""
Output:
Enter N: 12
2 4 6 8 10 12
"""