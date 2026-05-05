# Program to check voting using try-except
# ....................................................................
try:
    age = int(input("Enter age: "))
    print("Eligible" if age >= 18 else "Not Eligible")
except:
    print("Invalid input")
# ....................................................................
"""
Output:
Enter age: 25
Eligible
"""