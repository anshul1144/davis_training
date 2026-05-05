# Program to calculate electricity bill (compact)
# ....................................................................
units = int(input("Enter units: "))
bill = units*5 if units<=100 else units*7 if units<=200 else units*10
print(f"Total bill amount: {bill}")
# ....................................................................
"""
Output:
Enter units: 80
Total bill amount: 400
"""