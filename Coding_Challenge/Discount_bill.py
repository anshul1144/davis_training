# Program to calculate discount using lambda
# ....................................................................
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

calc = lambda p, d: p - p*d/100
print(f"Final price after discount: {calc(price, discount)}")
# ....................................................................
"""
Output:
Enter price: 100
Enter discount: 10
Final price after discount: 90.0
"""