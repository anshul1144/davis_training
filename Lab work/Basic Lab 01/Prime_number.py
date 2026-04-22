"""Prime Number Checker using function and for-loop."""


def is_primeNo(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False

    # Check divisibility from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    # If no divisor is found, number is prime
    return True


# Take input from user
num = int(input("Enter a number: "))

# Use if-else to display result
if is_primeNo(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
