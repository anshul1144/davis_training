# Write a function to calculate total bill amount.

# Function to calculate total bill amount
def calculate_total_bill(bill_amounts):
    total_bill = sum(bill_amounts)
    return total_bill

# Get user input for bill amounts
bill_amounts = []
num_items = int(input("Enter the number of items: "))
for i in range(num_items):
    amount = float(input(f"Enter the amount for item {i+1}: "))
    bill_amounts.append(amount)
    
total_bill = calculate_total_bill(bill_amounts)
print(f"Total bill amount: {total_bill:.2f}")   

""" Output:
Enter the number of items: 3
Enter the amount for item 1: 100
Enter the amount for item 2: 200
Enter the amount for item 3: 300
Total bill amount: 600.00
"""