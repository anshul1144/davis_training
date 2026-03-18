# Program to print even numbers (step loop)
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
for i in range(0, N+1):
    if i % 2 == 0 and i != 0:
        print(i, end=" ")
# ....................................................................
"""
Output:
Enter N: 10
2 4 6 8 10
"""