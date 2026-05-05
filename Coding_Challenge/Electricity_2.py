# Program to calculate electricity bill (if ladder)
# ....................................................................
units = int(input("Enter units: "))

if units <= 100:
    print(f"Total bill amount: {units*5}")
elif units <= 200:
    print(f"Total bill amount: {units*7}")
else:
    print(f"Total bill amount: {units*10}")
# ....................................................................
"""
Output:
Enter units: 180
Total bill amount: 1260
"""