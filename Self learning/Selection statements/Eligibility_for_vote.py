# program to check whether a person is eligible to vote (age ≥ 18).
#...........................................................
# taking input from the user
age = int(input("Enter your age: "))

# displaying the age entered by the user
print("Your age is: ", age ,"years.")

#  validation for negative age
if age < 0:
    exit("Invalid age. Age cannot be negative.")

# checking whether the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#...........................................................

""" Output:
Enter your age: 20
Your age is:  20 years.
You are eligible to vote.
"""