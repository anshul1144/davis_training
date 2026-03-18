# Program to calculate discount (direct formula)
# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

print(f"Final price after discount: {price*(1-discount/100)}")
# ....................................................................
"""
Output:
Enter price: 500
Enter discount: 10
Final price after discount: 450.0
"""