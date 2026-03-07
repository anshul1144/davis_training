# program to check whether a character is a vowel or consonant
#...........................................................
# taking input from the user
char = input("Enter a character: ")
# displaying the character entered by the user
print("The character entered is: ", char)
# validation for input length
if len(char) != 1:
    exit("Invalid input. Please enter a single character.")
# checking whether the character is a vowel or consonant
if char in 'AEIOUaeiou':
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")
#...........................................................
""" Output:
Enter a character: A
The character entered is:  A
A is a vowel.
"""