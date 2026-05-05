# Program to calculate SI using round
# ....................................................................
p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

print(f"Simple Interest: {round((p*r*t)/100,2)}")
# ....................................................................
"""
Output:
Enter P: 1000
Enter R: 5
Enter T: 2
Simple Interest: 100.0
"""