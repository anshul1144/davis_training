# Program to print even numbers using list
# ....................................................................
N = int(input("Enter N: "))

print(f"Even numbers between 1 and {N}:")
evens = [i for i in range(1, N+1) if i % 2 == 0]

for num in evens:
    print(num, end=" ")
# ....................................................................
"""
Output:
Enter N: 10
2 4 6 8 10
"""