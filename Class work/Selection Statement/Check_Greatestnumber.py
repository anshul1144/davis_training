# program to check greatest number among five numbers

#taking numbers from the user
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3= int(input("Enter the third number: "))
num4= int(input("Enter the fourth number: "))
num5= int(input("Enter the fifth number: "))

#checking the greatest number among the five numbers
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    print(num1, "is the greatest number.")
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    print(num2, "is the greatest number.")
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    print(num3, "is the greatest number.")
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    print(num4, "is the greatest number.")
else:
    print(num5, "is the greatest number.")
    
#................................................................

""" Output:
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
Enter the fourth number: 40
Enter the fifth number: 50
50.0 is the greatest number.
"""