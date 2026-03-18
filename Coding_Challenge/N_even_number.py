# Program to print even numbers using filter
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
print(*list(filter(lambda x: x%2==0, range(1, N+1))))
# ....................................................................
"""
Output:
Enter N: 6
2 4 6
"""