# Program to calculate SI using function
# ....................................................................
def interest(p, r, t):
    return (p*r*t)/100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

print(f"Simple Interest: {interest(p,r,t)}")
# ....................................................................
"""
Output:
Enter P: 1000
Enter R: 4
Enter T: 2
Simple Interest: 80.0
"""