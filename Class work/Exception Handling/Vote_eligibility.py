# Write a program to check the user is eligible for vote or not by using exception handling.

#...............................................................................................

# create custom exception class 
class AgeException(Exception):
    pass

try:
    age = int(input("Enter your age in year: "))
    if age < 0:
        raise AgeException("Age cannot be negative.")
    elif age < 18:
        print("Error: You are not eligible to vote.")
    else:
        print("You are eligible to vote.")
except AgeException:
    print("Error: Age cannot be negative.")
except ValueError:
    print("Error: Please enter a valid age.")
    
else:
    print("Vote eligibility check completed successfully.")