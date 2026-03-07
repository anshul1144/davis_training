# program to check whether a number is divisible by 5.

# taking input from the user
num = int(input("Enter a number: "))

# checking whether the number is divisible by 5
if num % 5 == 0:
    print(num, "is divisible by 5.")
else:
    print(num, "is not divisible by 5.")
    
#...........................................................

""" Output:
Enter a number: 25
25 is divisible by 5.
"""