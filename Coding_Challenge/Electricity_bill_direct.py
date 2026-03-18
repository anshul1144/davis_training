# Program to calculate electricity bill (compact if)
# ....................................................................
units = int(input("Enter units: "))

if units > 200:
    bill = units * 10
elif units > 100:
    bill = units * 7
else:
    bill = units * 5

print(f"Total bill amount: {bill}")
# ....................................................................
"""
Output:
Enter units: 90
Total bill amount: 450
"""