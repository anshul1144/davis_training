# program to check whether a number lies between 10 and 50.
#...........................................................

# taking input from the user
num = int(input("Enter a number: "))

# displaying the number entered by the user
print("The number entered is: ", num)

# checking whether the number lies between 10 and 50
if num > 10 and num < 50:
    print(num, "lies between 10 and 50.")
else:
    print(num, "does not lie between 10 and 50.")
    
#...........................................................

""" Output:
Enter a number: 25
The number entered is:  25
25 lies between 10 and 50.
"""