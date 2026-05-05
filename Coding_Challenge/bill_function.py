# Program to calculate electricity bill using function
# ....................................................................
def calc(u):
    return u*5 if u<=100 else u*7 if u<=200 else u*10

units = int(input("Enter units: "))
print(f"Total bill amount: {calc(units)}")
# ....................................................................
"""
Output:
Enter units: 110
Total bill amount: 770
"""