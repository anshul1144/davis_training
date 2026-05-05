# Write a function to check prime number.


# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return "Not a Prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a Prime"
    return "Prime"

# Get user input
number = int(input("Enter a number: "))
result = is_prime(number)
print(result)


""" Output:
Enter a number: 7
Prime
"""