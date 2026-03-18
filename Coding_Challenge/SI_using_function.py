# Program to create a function to calculate simple interest.
# ....................................................................
# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest based on the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest
# Input the principal amount, rate of interest, and time period from the user
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))



#display the input values
print(f"Principal Amount: ${principal_amount:.2f}")
print(f"Rate of Interest: {rate_of_interest:.2f}%")
print(f"Time Period: {time_period:.2f} years")

# Calculate the simple interest using the function
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)
# Print the calculated simple interest
print(f"The simple interest is: ${simple_interest:.2f}")
# ....................................................................

"""Output:
Enter the principal amount: 1000
Enter the rate of interest (in %): 5
Enter the time period (in years): 2
The simple interest is: $100.00
"""