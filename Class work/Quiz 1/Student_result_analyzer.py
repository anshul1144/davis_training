"""
A school stores student data in a file: id,name,marks1,marks2,marks3 Build a system that: 
• Reads file  
• Calculates total, percentage  
• Assigns grade using selection statements  
• Handles missing/invalid data using exception handling  
• Outputs toppers per class  
"""

import csv


# Get class from student id
# Example: 10A-01 -> 10A, 9B_03 -> 9B
def get_class_from_id(student_id):
    if "-" in student_id:
        return student_id.split("-")[0].strip()
    if "_" in student_id:
        return student_id.split("_")[0].strip()
    return "Unknown"


# Assign grade using percentage
def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# File path
file_name = "Class work/Quiz 1/student_data.csv"

# List to store valid student records
students = []

#  Read file and process row by row
try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Skip header
        header = next(reader, None)
        if header is None:
            print("File is empty.")

        # Read each row
        for line_number, row in enumerate(reader, start=2):
            try:
                # Ignore empty rows
                if not row or all(cell.strip() == "" for cell in row):
                    continue

                # Check correct number of values
                if len(row) != 5:
                    raise ValueError("Expected 5 values: id,name,marks1,marks2,marks3")

                student_id = row[0].strip()
                name = row[1].strip()
                mark1 = float(row[2].strip())
                mark2 = float(row[3].strip())
                mark3 = float(row[4].strip())

                # Marks must be between 0 and 100
                for mark in (mark1, mark2, mark3):
                    if mark < 0 or mark > 100:
                        raise ValueError("Marks should be between 0 and 100")

                total = mark1 + mark2 + mark3
                percentage = total / 3
                grade = assign_grade(percentage)
                class_name = get_class_from_id(student_id)

                # Save valid student data
                students.append(
                    {
                        "id": student_id,
                        "name": name,
                        "class": class_name,
                        "total": total,
                        "percentage": percentage,
                        "grade": grade,
                    }
                )

            except ValueError as error:
                print(f"Line {line_number}: Invalid data -> {error}")
            except Exception as error:
                print(f"Line {line_number}: Unexpected error -> {error}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as error:
    print(f"Error while reading file: {error}")


#  Print all student results
if len(students) == 0:
    print("No valid student records found.")
else:
    print("\n--- Student Result Report ---")
    for student in students:
        print(
            f"ID: {student['id']}, Name: {student['name']}, "
            f"Class: {student['class']}, Total: {student['total']:.2f}, "
            f"Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}"
        )

    # Find and print topper(s) class wise
    class_groups = {}

    # Group students by class
    for student in students:
        class_name = student["class"]
        if class_name not in class_groups:
            class_groups[class_name] = []
        class_groups[class_name].append(student)

    print("\n--- Class Topper(s) ---")
    for class_name, class_students in class_groups.items():
        highest_total = max(s["total"] for s in class_students)

        # If tie, print all toppers
        toppers = [s for s in class_students if s["total"] == highest_total]

        print(f"\nClass: {class_name}")
        for topper in toppers:
            print(
                f"Topper: {topper['name']} (ID: {topper['id']}), "
                f"Total: {topper['total']:.2f}, Percentage: {topper['percentage']:.2f}%"
            )
