# Program to print even numbers using list comprehension
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
print(*[i for i in range(2, N+1, 2)])
# ....................................................................
"""
Output:
Enter N: 10
2 4 6 8 10
"""