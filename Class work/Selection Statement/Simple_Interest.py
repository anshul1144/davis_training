# Program to calculate simple interest and validate the results

# Taking input from user
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time (in years): "))

# Validation of inputs
if principal <= 0:
    print("Invalid Input: Principal must be greater than 0")
elif rate <= 0:
    print("Invalid Input: Rate must be greater than 0")
elif time <= 0:
    print("Invalid Input: Time must be greater than 0")
else:
    
    # Displaying result
    print("Simple Interest =", (principal * rate * time) / 100)

#...................................................

""" Output:
Enter the Principal Amount: 1000
Enter the Rate of Interest: 5
Enter the Time (in years): 2
Simple Interest = 100.0
"""
    