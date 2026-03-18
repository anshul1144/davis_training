# Program to calculate SI with validation
# ....................................................................
p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

if p > 0 and r > 0 and t > 0:
    print(f"Simple Interest: {(p*r*t)/100}")
else:
    print("Invalid Input")
# ....................................................................
"""
Output:
Enter P: 1000
Enter R: 5
Enter T: 2
Simple Interest: 100.0
"""