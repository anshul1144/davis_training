# Program to dispaly even factors of a given number.
#..................................................
num = int(input("Enter a number: "))

# Display the input number
print("The input number is:", num)


found = False

for x in range(1, num + 1):
    if num % x == 0 and x % 2 == 0:
        print(x)
        found = True
        
print("The even factors of", num, "are:")

if not found:
        print("No even factors are present")


#..................................................
""" Output:
Enter a number: 36
The input number is: 36
The even factors of 36 are:
2
4
6
12
18
36
"""