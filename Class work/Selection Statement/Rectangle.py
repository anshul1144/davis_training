# program to calculate the area and perimeter of a rectangle and validate the data whnenever required

# taking input from the user
length = float(input("Enter the length of the rectangle: "))
if length <= 0:
    exit("Invalid Input: Length must be greater than 0")
breadth = float(input("Enter the breadth of the rectangle: "))
if breadth <= 0:
    exit("Invalid Input: Breadth must be greater than 0")
    
# calculating area and perimeter
print("Area of the rectangle =", length * breadth)
print("Perimeter of the rectangle =", 2 * (length + breadth))
#................................................................

""" Output: 
Enter the length of the rectangle: 5
Enter the breadth of the rectangle: 3
Area of the rectangle = 15.0
Perimeter of the rectangle = 16.0
"""