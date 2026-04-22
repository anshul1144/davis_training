""" Student Grouping System

Given list of students:
- Group by grade
- Store in dictionary of lists

Example:
A: [students]
B: [students]
"""


def group_students_by_grade(students):
    grouped = {}

    for student in students:
        name = student["name"]
        grade = student["grade"]

        if grade not in grouped:
            grouped[grade] = []

        grouped[grade].append(name)

    return grouped


if __name__ == "__main__":
    student_list = [
        {"name": "Riya", "grade": "A"},
        {"name": "Aman", "grade": "B"},
        {"name": "Zoya", "grade": "A"},
        {"name": "Karan", "grade": "C"},
    ]

    grouped_data = group_students_by_grade(student_list)
    for grade, names in grouped_data.items():
        print(f"{grade}: {names}")
