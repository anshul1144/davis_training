"""A school stores student data in a file: id,name,marks1,marks2,marks3 Build a system that: 
• Reads file  
• Calculates total, percentage  
• Assigns grade using selection statements  
• Handles missing/invalid data using exception handling  
• Outputs toppers per class """


# Get class name from student ID
# Example: 10A-01 -> 10A, 9B_03 -> 9B
def get_class(student_id):
    if "-" in student_id:
        return student_id.split("-")[0].strip()
    if "_" in student_id:
        return student_id.split("_")[0].strip()
    return "Unknown"


# Return grade from percentage
def get_grade(percent):
    if percent >= 90:
        return "A+"
    if percent >= 80:
        return "A"
    if percent >= 70:
        return "B"
    if percent >= 60:
        return "C"
    if percent >= 50:
        return "D"
    return "F"


# Convert one CSV line into a valid student dictionary
# If data is invalid, print error and return None
def parse_student(line, line_number):
    try:
        # Split row by comma and remove extra spaces
        parts = [x.strip() for x in line.split(",")]
        if len(parts) != 5:
            raise ValueError("Expected 5 values")

        # Read id, name and marks
        sid, name = parts[0], parts[1]
        marks = [float(parts[2]), float(parts[3]), float(parts[4])]

        # Validate marks range
        if any(m < 0 or m > 100 for m in marks):
            raise ValueError("Marks should be between 0 and 100")

        # Calculate total, percentage, grade
        total = sum(marks)
        percent = total / 3
        return {
            "id": sid,
            "name": name,
            "class": get_class(sid),
            "total": total,
            "percentage": percent,
            "grade": get_grade(percent),
        }
    except Exception as error:
        print(f"Line {line_number}: Invalid data -> {error}")
        return None


# Read file and return list of valid students
def read_students(file_name):
    students = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Read and skip header line
            if file.readline() == "":
                print("File is empty.")
                return students

            # Read each student row from line 2
            for line_number, line in enumerate(file, start=2):
                if line.strip() == "":
                    continue
                student = parse_student(line.strip(), line_number)
                if student:
                    students.append(student)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as error:
        print(f"Error while reading file: {error}")
    return students


# Print all valid student results
def print_report(students):
    print("\n--- Student Result Report ---")
    for s in students:
        print(
            f"ID: {s['id']}, Name: {s['name']}, Class: {s['class']}, "
            f"Total: {s['total']:.2f}, Percentage: {s['percentage']:.2f}%, Grade: {s['grade']}"
        )


# Group by class and print class topper(s)
def print_toppers(students):
    by_class = {}
    for s in students:
        # Create class key if not present, then append student
        by_class.setdefault(s["class"], []).append(s)

    print("\n--- Class Topper(s) ---")
    for class_name, class_students in by_class.items():
        # Find highest total in this class
        top_total = max(s["total"] for s in class_students)
        print(f"\nClass: {class_name}")
        for s in class_students:
            # Print all toppers in case of tie
            if s["total"] == top_total:
                print(
                    f"Topper: {s['name']} (ID: {s['id']}), "
                    f"Total: {s['total']:.2f}, Percentage: {s['percentage']:.2f}%"
                )


# File path
file_name = "Class work/Quiz 1/student_data.csv"

# Step 1: Read and validate data
students = read_students(file_name)

if students:
    # Step 2: Print student report
    print_report(students)

    # Step 3: Print class toppers
    print_toppers(students)
else:
    print("No valid student records found.")
