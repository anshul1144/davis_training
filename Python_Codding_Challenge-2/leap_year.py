# Write a program to determine whether a year is a leap year.


# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
    
# Get user input
year = int(input("Enter a year: "))
result = is_leap_year(year)
print(result)

""" Output:
Enter a year: 2024
Leap Year
"""