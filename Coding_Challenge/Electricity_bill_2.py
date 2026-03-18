# Program to calculate electricity bill (direct)
# ....................................................................
units = int(input("Enter units: "))
rate = 5 if units<=100 else 7 if units<=200 else 10

print(f"Total bill amount: {units*rate}")
# ....................................................................
"""
Output:
Enter units: 50
Total bill amount: 250
"""