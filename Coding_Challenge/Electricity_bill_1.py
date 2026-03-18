# Program to calculate electricity bill using loop
# ....................................................................
units = int(input("Enter units: "))
bill = 0

for i in range(units):
    if i < 100:
        bill += 5
    elif i < 200:
        bill += 7
    else:
        bill += 10

print(f"Total bill amount: {bill}")
# ....................................................................
"""
Output:
Enter units: 50
Total bill amount: 250
"""