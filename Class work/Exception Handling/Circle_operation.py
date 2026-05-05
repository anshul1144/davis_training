# Write a program to calculate area and circumference of the circle, and the radius is given by the user.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")
