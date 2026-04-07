# Program to calculate simple interest by using the function.
#................................................................
def calculate_SI(principal, rate, time):
    return ((principal * rate * time) / 100)
#input from user
Principal = float(input("Enter the principal amount: "))
Rate= float(input("Enter the rate of interest: "))
Time = int(input("Enter the time in years: "))

print("The simple interest is", calculate_SI(Principal, Rate, Time))
#................................................................
""" Output:
Enter the principal amount: 1000
Enter the rate of interest: 5
Enter the time in years: 3
The simple interest is 150.0
"""