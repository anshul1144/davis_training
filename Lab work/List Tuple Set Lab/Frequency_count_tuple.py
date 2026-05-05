# Count the frequency of each element in a tuple.
#...............................................................................

# taking input from user for the tuple
elements = []
n = int(input("Enter number of elements in the tuple: "))
for i in range(n):
    elem = input("Enter element for the tuple: ")
    elements.append(elem)
# converting list to tuple
my_tuple = tuple(elements)
# counting frequency of each element in the tuple
frequency = {}
for elem in my_tuple:
    if elem in frequency:
        frequency[elem] += 1
    else:
        frequency[elem] = 1
# printing the frequency of each element
print("Frequency of each element in the tuple:")
for elem, count in frequency.items():
    print(f"{elem}: {count}")

#...............................................................................

""" Output: 
Enter number of elements in the tuple: 6
Enter element for the tuple: apple
Enter element for the tuple: banana
Enter element for the tuple: apple
Enter element for the tuple: orange
Enter element for the tuple: banana
Enter element for the tuple: apple
Frequency of each element in the tuple:
apple: 3
banana: 2
orange: 1
"""