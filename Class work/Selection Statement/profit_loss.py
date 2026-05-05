# program to calculate profit or loss

#.................................................................
# taking cost price from the user
cost_price = float(input("Enter the cost price: "))
#validating the cost price
if cost_price <= 0:
    exit("Invalid Input: Cost price must be greater than 0")
#input selling price
selling_price = float(input("Enter the selling price: "))
#validating the selling price
if selling_price <= 0:
    exit("Invalid Input: Selling price must be greater than 0")
    
#displaying the input values
print(".................Cost and Selling Price.................")
print("Cost Price = Rs", cost_price)
print("Selling Price = Rs", selling_price)

# calculating profit or loss
if selling_price > cost_price:
    print("Profit = Rs", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss = Rs", cost_price - selling_price)
else:
    print("No profit, no loss.")
    
#................................................................

""" Output:
Enter the cost price: 1000
Enter the selling price: 1200
Profit = Rs 200.0
"""