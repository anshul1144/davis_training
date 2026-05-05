# Program to print all even numbers between 1 to N
# ....................................................................
# Input the value of N from the user
N = int(input("Enter the value of N: "))
# Print all even numbers between 1 to N
print(f"Even numbers between 1 and {N}:")
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i, end=' ')
# ....................................................................
"""Output:
Enter the value of N: 10
Even numbers between 1 and 10:
2 4 6 8 10
"""