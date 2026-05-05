# Program to calculate simple interest using lambda
# ....................................................................
p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

si = lambda p, r, t: (p*r*t)/100

print(f"Simple Interest: {si(p,r,t)}")
# ....................................................................
"""
Output:
Enter P: 1000
Enter R: 5
Enter T: 2
Simple Interest: 100.0
"""