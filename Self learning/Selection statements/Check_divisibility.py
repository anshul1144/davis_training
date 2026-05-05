# program to check whether a number is divisible by 2, 3, 5 or 7
# .....................................................................

# taking input from the user

num = int(input("Enter a number: "))
# displaying the number entered by the user

print("The number you entered is:", num)
# checking the divisibility of number

if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print(num, "is not divisible by 2, 3, 5 or 7")

else:
    if num % 2 == 0:
        print(num, "is divisible by 2")
    else:
        print(num, "is not divisible by 2")

    if num % 3 == 0:
        print(num, "is divisible by 3")
    else:
        print(num, "is not divisible by 3")

    if num % 5 == 0:
        print(num, "is divisible by 5")
    else:
        print(num, "is not divisible by 5")

    if num % 7 == 0:
        print(num, "is divisible by 7")
    else:
        print(num, "is not divisible by 7")

""" Output:
Enter a number: 210
The number you entered is: 210
210 is divisible by 2
210 is divisible by 3
210 is divisible by 5
210 is divisible by 7
"""