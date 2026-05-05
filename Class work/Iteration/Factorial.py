# program to find the factorial of a number
#...................................................
num = int(input("Enter a number: "))
# Display the input number
print("The input number is:", num)
# Initialize factorial to 1
fact=1
# Loop from 1 to num and multiply to fact
for x in range(1, num + 1):
    fact = fact * x
# Display the factorial
print("The factorial of", num, "is:", fact)
#...................................................
""" Output:
Enter a number: 5
The input number is: 5
The factorial of 5 is: 120
"""