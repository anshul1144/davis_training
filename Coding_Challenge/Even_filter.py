# Program to print even numbers using filter
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
evens = list(filter(lambda x: x%2==0, range(1, N+1)))

for num in evens:
    print(num, end=" ")
# ....................................................................
"""
Output:
Enter N: 10
2 4 6 8 10
"""