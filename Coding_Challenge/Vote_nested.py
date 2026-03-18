# Program to check voting (nested style)
# ....................................................................
age = int(input("Enter age: "))

if age >= 0:
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
# ....................................................................
"""
Output:
Enter age: 15
Not Eligible
"""