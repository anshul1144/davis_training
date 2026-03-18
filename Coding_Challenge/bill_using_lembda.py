# Program to calculate discount using lambda
# ....................................................................
p = float(input("Enter price: "))
d = float(input("Enter discount: "))

print(f"Final price after discount: {(lambda p,d: p-p*d/100)(p,d)}")
# ....................................................................
"""
Output:
Enter price: 200
Enter discount: 20
Final price after discount: 160.0
"""