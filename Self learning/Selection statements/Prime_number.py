# Program to check if a number is prime or not
#...........................................................
# taking input from the user
num = int(input("Enter a number: "))
# displaying the number entered by the user
print("You entered: ", num)
# validation for negative numbers
if num < 0:
    exit("Invalid input. Number cannot be negative.")
# checking if the number is prime
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
#...........................................................

""" Output:
Enter a number: 17
You entered:  17
17 is a prime number.
"""
