# Program to check voting using function
# ....................................................................
def check(age):
    return age >= 18

age = int(input("Enter age: "))
print("Eligible" if check(age) else "Not Eligible")
# ....................................................................
"""
Output:
Enter age: 16
Not Eligible
"""