# Convert two tuples into a dictionary where one tuple contains keys and the other contains values
# ......................................................................

# taking input from user for keys tuple
n = int(input("Enter number of elements for keys tuple: "))
keys_list = []
for i in range(n):
    key = input("Enter key element: ")
    keys_list.append(key)

# converting list to tuple
keys_tuple = tuple(keys_list)

# taking input from user for values tuple
values_list = []
for i in range(n):
    value = input("Enter value element: ")
    values_list.append(value)

# converting list to tuple
values_tuple = tuple(values_list)

# converting two tuples into dictionary
result_dict = dict(zip(keys_tuple, values_tuple))

# printing the dictionary
print("Keys Tuple:", keys_tuple)
print("Values Tuple:", values_tuple)
print("Resulting Dictionary:", result_dict)

"""
Output:
Enter number of elements for keys tuple: 3
Enter key element: a
Enter key element: b
Enter key element: c
Enter value element: 1
Enter value element: 2
Enter value element: 3

Keys Tuple: ('a', 'b', 'c')
Values Tuple: ('1', '2', '3')
Resulting Dictionary: {'a': '1', 'b': '2', 'c': '3'}
"""