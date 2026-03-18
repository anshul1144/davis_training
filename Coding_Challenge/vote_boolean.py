# Program to check voting using boolean variable
# ....................................................................
age = int(input("Enter age: "))
is_valid = age >= 18

print("Eligible" if is_valid else "Not Eligible")
# ....................................................................
"""
Output:
Enter age: 18
Eligible
"""