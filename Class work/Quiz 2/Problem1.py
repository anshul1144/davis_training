""" An electricity company calculates monthly bills based on the following rates: Units Consumed First 100 units Next 100 units Rate per Unit ₹5 ₹7 Above 200 units ₹10 Additionally: ● If the total bill exceeds ₹1500, apply a 5% discount. ● Print the final bill amount. Requirements ● Create a function named calculate_bill(units). ● Take the number of units from the user. ● Display: ○ Units Consumed ○ Total Bill ○ Discount (if applicable) ○ Final Amount Sample Output None Enter units consumed: 250 Units Consumed : 250 Total Bill     : ₹1700 Discount       Final Bill     : ₹85 : ₹1615 """

def calculate_bill(units):
    # Initialize total bill
    total_bill = 0

    # Calculate bill based on units consumed
    if units <= 100:
        total_bill = units * 5
    elif units <= 200:
        total_bill = (100 * 5) + ((units - 100) * 7)
    else:
        total_bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    # Check for discount
    discount = 0
    if total_bill > 1500:
        discount = total_bill * 0.05

    final_amount = total_bill - discount

    # Print the results
    print(f"Units Consumed : {units}")
    print(f"Total Bill     : ₹{total_bill}")
    if discount > 0:
        print(f"Discount       : ₹{discount}")
    print(f"Final Bill     : ₹{final_amount}")
    
calculate_bill(int(input("Enter units consumed: ")))