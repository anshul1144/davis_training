# Program to perform operations on the set
# creating a set of numbers
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# asking the user to input a number
num = int(input("Enter a number which is used to perform operations on the set: "))

# Insertion Of element in set
#.............................................................................................
# adding the number to the set
numbers.add(num)
print("Set after adding the number:", numbers)
# updating the set with another set of numbers
numbers.update({16, 17, 18})
print("Set after updating with another set of numbers:", numbers)

#
# removing the number from the set
numbers.remove(num)
print("Set after removing the number:", numbers)
# using pop to remove an arbitrary element from the set
numbers.pop()
print("Set after popping an arbitrary element:", numbers)
