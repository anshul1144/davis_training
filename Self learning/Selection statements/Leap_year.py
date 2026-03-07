# program to check whether a year is a leap year.

#............................................................
# taking input from the user
year = int(input("Enter a year: "))
# displaying the year entered by the user
print("The year entered is: ", year)

# validation for negative year
if year < 0:
    exit("Invalid year. Year cannot be negative.")
    
# checking whether the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
#............................................................
""" Output:
Enter a year: 2020
The year entered is:  2020
2020 is a leap year.
"""