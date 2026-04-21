""" A school stores student data in a file: id,name,marks1,marks2,marks3 Build a system that: 
• Reads file  
• Calculates total, percentage  
• Assigns grade using selection statements  
• Handles missing/invalid data using exception handling  
• Outputs toppers per class  """

import csv


def get_class_from_id(student_id):
    """
    Tries to get class name from student id.

    Examples:
    10A-01 -> 10A
    9B_12  -> 9B

    If no separator is found, returns "Unknown".
    """
    if "-" in student_id:
        return student_id.split("-")[0].strip()
    if "_" in student_id:
        return student_id.split("_")[0].strip()
    return "Unknown"


def assign_grade(percentage):
    """Assign grade based on percentage."""
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


def process_student_row(row, line_number):
    """
    Validates one row and returns processed student dictionary.
    Returns None if row has invalid data.
    """
    try:
        # Check total columns first
        if len(row) != 5:
            raise ValueError("Expected 5 values: id,name,marks1,marks2,marks3")

        student_id = row[0].strip()
        name = row[1].strip()

        # Convert marks to numbers
        mark1 = float(row[2].strip())
        mark2 = float(row[3].strip())
        mark3 = float(row[4].strip())

        # Check marks range
        for mark in (mark1, mark2, mark3):
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100")

        total = mark1 + mark2 + mark3
        percentage = total / 3
        grade = assign_grade(percentage)
        class_name = get_class_from_id(student_id)

        return {
            "id": student_id,
            "name": name,
            "class": class_name,
            "marks": [mark1, mark2, mark3],
            "total": total,
            "percentage": percentage,
            "grade": grade,
        }

    except ValueError as error:
        print(f"Line {line_number}: Invalid data -> {error}")
        return None
    except Exception as error:
        print(f"Line {line_number}: Unexpected error -> {error}")
        return None


def read_and_analyze_file(file_name):
    """Reads file and returns list of valid student records."""
    students = []

    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip header row
            header = next(reader, None)
            if header is None:
                print("File is empty.")
                return students

            # Start from line 2 because line 1 is header
            for line_number, row in enumerate(reader, start=2):
                # Ignore blank lines
                if not row or all(cell.strip() == "" for cell in row):
                    continue

                student = process_student_row(row, line_number)
                if student is not None:
                    students.append(student)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: No permission to read '{file_name}'.")
    except Exception as error:
        print(f"Error while reading file: {error}")

    return students


def print_student_report(students):
    """Prints student-wise report."""
    if not students:
        print("No valid student data to display.")
        return

    print("\n--- Student Result Report ---")
    for student in students:
        print(
            f"ID: {student['id']}, Name: {student['name']}, "
            f"Class: {student['class']}, Total: {student['total']:.2f}, "
            f"Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}"
        )


def print_toppers_by_class(students):
    """Finds and prints topper(s) in each class."""
    if not students:
        return

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

        # Handle tie case (multiple toppers)
        toppers = [s for s in class_students if s["total"] == highest_total]

        print(f"\nClass: {class_name}")
        for topper in toppers:
            print(
                f"Topper: {topper['name']} (ID: {topper['id']}), "
                f"Total: {topper['total']:.2f}, Percentage: {topper['percentage']:.2f}%"
            )


# Give file path
file_name = "Class work/Quiz 1/student_data.csv"

# Read file and process student data
students = read_and_analyze_file(file_name)

# Show results only if we have valid records
if len(students) > 0:
    print_student_report(students)
    print_toppers_by_class(students)
else:
    print("No valid student records found.")
