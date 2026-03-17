# Program to check whether a given number is even or odd.
#..................................................
#function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#input from user
number = int(input("Enter a number: "))
print("The number is", check_even_odd(number))
#..................................................

""" Output:
Enter a number: 15
The number is Odd
"""