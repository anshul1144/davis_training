# Check whether a person is eligible to vote

# ....................................................................
age = int(input("Enter age: "))
eligible = age >= 18

if eligible:
    print("Eligible")
else:
    print("Not Eligible")
# ....................................................................
"""
Output:
Enter age: 18
Eligible
"""