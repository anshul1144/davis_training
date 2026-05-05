# 3D Operation Module
# Write a program to create a python module which contains the functions to calculate curved surface area, total surface area, volume of threed figures(cube,cuboid, cylinder,cone,sphere, hemisphere).
#
# Units:
# - Input dimensions (side, length, breadth, height, radius, slant_height) are in `units`.
# - Surface area results are in `square units` (units^2).
# - Volume results are in `cubic units` (units^3).

# functions to perform operations on a cube
def calculate_curved_surface_area_cube(side):
    """Returns curved/lateral surface area in square units (units^2)."""
    return 4 * (side ** 2)

def calculate_total_surface_area_cube(side):
    """Returns total surface area in square units (units^2)."""
    return 6 * (side ** 2)

def calculate_volume_cube(side):
    """Returns volume in cubic units (units^3)."""
    return side ** 3

# functions to perform operations on a cuboid
def calculate_curved_surface_area_cuboid(length, breadth, height):
    """Returns curved/lateral surface area in square units (units^2)."""
    return 2 * (length * height + breadth * height)

def calculate_total_surface_area_cuboid(length, breadth, height):
    """Returns total surface area in square units (units^2)."""
    return 2 * (length * breadth + length * height + breadth * height)

def calculate_volume_cuboid(length, breadth, height):
    """Returns volume in cubic units (units^3)."""
    return length * breadth * height

# functions to perform operations on a cylinder
def calculate_curved_surface_area_cylinder(radius, height):
    """Returns curved surface area in square units (units^2)."""
    return 2 * 3.14 * radius * height
def calculate_total_surface_area_cylinder(radius, height):
    """Returns total surface area in square units (units^2)."""
    return 2 * 3.14 * radius * (radius + height)
def calculate_volume_cylinder(radius, height):
    """Returns volume in cubic units (units^3)."""
    return 3.14 * (radius ** 2) * height

# functions to perform operations on a cone
def calculate_curved_surface_area_cone(radius, slant_height):
    """Returns curved surface area in square units (units^2)."""
    return 3.14 * radius * slant_height
def calculate_total_surface_area_cone(radius, slant_height):
    """Returns total surface area in square units (units^2)."""
    return 3.14 * radius * (radius + slant_height)
def calculate_volume_cone(radius, height):
    """Returns volume in cubic units (units^3)."""
    return (1/3) * 3.14 * (radius ** 2) * height

# functions to perform operations on a sphere
def calculate_curved_surface_area_sphere(radius):
    """Returns curved/total surface area in square units (units^2)."""
    return 4 * 3.14 * (radius ** 2)
def calculate_total_surface_area_sphere(radius):
    """Returns total surface area in square units (units^2)."""
    return 4 * 3.14 * (radius ** 2)
def calculate_volume_sphere(radius):
    """Returns volume in cubic units (units^3)."""
    return (4/3) * 3.14 * (radius ** 3)

# functions to perform operations on a hemisphere
def calculate_curved_surface_area_hemisphere(radius):
    """Returns curved surface area in square units (units^2)."""
    return 2 * 3.14 * (radius ** 2)
def calculate_total_surface_area_hemisphere(radius):
    """Returns total surface area in square units (units^2)."""
    return 3 * 3.14 * (radius ** 2)
def calculate_volume_hemisphere(radius):
    """Returns volume in cubic units (units^3)."""
    return (2/3) * 3.14 * (radius ** 3)
