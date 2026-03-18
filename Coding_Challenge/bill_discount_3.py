# Program to calculate discount (compact)
# ....................................................................
p = float(input("Enter price: "))
d = float(input("Enter discount: "))

print(f"Final price after discount: {p - p*d/100}")
# ....................................................................
"""
Output:
Enter price: 150
Enter discount: 10
Final price after discount: 135.0
"""