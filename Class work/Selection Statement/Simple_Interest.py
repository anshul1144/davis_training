# Program to calculate simple interest and validate the results

#..................................................................

# Program to calculate Simple Interest with validation

# Input principal amount
principal = float(input("Enter Principal Amount: "))
if principal <= 0:
   
    exit("Invalid Input: Principal must be greater than 0")

# Input rate of interest
rate = float(input("Enter Rate of Interest: "))
if rate <= 0:
    
    exit("Invalid Input: Rate must be greater than 0")

# Input time in years
time = float(input("Enter Time (in years): "))
if time <= 0:
  
    exit("Invalid Input: Time must be greater than 0")

    # Displaying result
    print("Simple Interest =", (principal * rate * time) / 100)

#................................................................

""" Output:
Enter the Principal Amount: 1000
Enter the Rate of Interest: 5
Enter the Time (in years): 2
Simple Interest = 100.0
"""
    