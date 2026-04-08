# Simple menu-driven program for 3D shape operations

from importlib import util
from pathlib import Path


module_path = Path(__file__).with_name("3D_shape_module.py")
spec = util.spec_from_file_location("shape_module", module_path)
shape_module = util.module_from_spec(spec)
spec.loader.exec_module(shape_module)


def main():
    print("Select a 3D figure:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")
    choice = int(input("Enter your choice: "))

    print("Select operation:")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")
    op_choice = int(input("Enter your choice: "))

    if choice == 1:
        side = float(input("Enter side: "))
        if op_choice == 1:
            result = shape_module.calculate_curved_surface_area_cube(side)
        elif op_choice == 2:
            result = shape_module.calculate_total_surface_area_cube(side)
        else:
            result = shape_module.calculate_volume_cube(side)

    elif choice == 2:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        height = float(input("Enter height: "))
        if op_choice == 1:
            result = shape_module.calculate_curved_surface_area_cuboid(length, breadth, height)
        elif op_choice == 2:
            result = shape_module.calculate_total_surface_area_cuboid(length, breadth, height)
        else:
            result = shape_module.calculate_volume_cuboid(length, breadth, height)

    elif choice == 3:
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        if op_choice == 1:
            result = shape_module.calculate_curved_surface_area_cylinder(radius, height)
        elif op_choice == 2:
            result = shape_module.calculate_total_surface_area_cylinder(radius, height)
        else:
            result = shape_module.calculate_volume_cylinder(radius, height)

    elif choice == 4:
        radius = float(input("Enter radius: "))
        if op_choice == 1:
            slant_height = float(input("Enter slant height: "))
            result = shape_module.calculate_curved_surface_area_cone(radius, slant_height)
        elif op_choice == 2:
            slant_height = float(input("Enter slant height: "))
            result = shape_module.calculate_total_surface_area_cone(radius, slant_height)
        else:
            height = float(input("Enter height: "))
            result = shape_module.calculate_volume_cone(radius, height)

    elif choice == 5:
        radius = float(input("Enter radius: "))
        if op_choice == 1:
            result = shape_module.calculate_curved_surface_area_sphere(radius)
        elif op_choice == 2:
            result = shape_module.calculate_total_surface_area_sphere(radius)
        else:
            result = shape_module.calculate_volume_sphere(radius)

    elif choice == 6:
        radius = float(input("Enter radius: "))
        if op_choice == 1:
            result = shape_module.calculate_curved_surface_area_hemisphere(radius)
        elif op_choice == 2:
            result = shape_module.calculate_total_surface_area_hemisphere(radius)
        else:
            result = shape_module.calculate_volume_hemisphere(radius)

    else:
        print("Invalid figure choice")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()
    
