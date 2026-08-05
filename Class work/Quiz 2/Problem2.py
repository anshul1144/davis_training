""" A training institute wants to calculate student results. 
The program should: ● Ask the user for the number of students.
● For each student:
○ Enter Name ○ Enter Marks in Python (100) 
○ Enter Marks in Excel (100) 
○ Enter Marks in Communication (100) 
Calculate: 
● Total Marks 
● Percentage Assign Grades: Percentag e 90+ 75–89 60–74 40–59 Below 40 Grade A B C D Fail 
"""

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


# Input the number of students to process
num_students = int(input("Enter number of students: "))

# List to store all student results
students = []

# Variables to calculate class summary data
total_percentage = 0
highest_percentage = -1
highest_student = ""

for i in range(1, num_students + 1):
    # Read data for each student
    print(f"\nStudent {i} details:")
    name = input("Name: ")
    python_marks = int(input("Python marks out of 100: "))
    excel_marks = int(input("Excel marks out of 100: "))
    communication_marks = int(input("Communication marks out of 100: "))

    # Calculate total marks and percentage for the student
    total_marks = python_marks + excel_marks + communication_marks
    percentage = total_marks / 300 * 100
    grade = calculate_grade(percentage)

    # Save the student record and update class totals
    students.append((name, total_marks, percentage, grade))
    total_percentage += percentage

    # Track the student with the highest percentage
    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_student = name

# Print student results in a table format
print("\n===== STUDENT RESULTS =====")
print(f"{'Name':<20}{'Total':<10}{'Percentage':<15}{'Grade':<10}")
print('-' * 55)
for student in students:
    print(f"{student[0]:<20}{student[1]:<10}{round(student[2], 2):<15}{student[3]:<10}")

# Calculate and print the class summary
average_percentage = total_percentage / num_students
print("\n===== CLASS SUMMARY =====")
print("Top student:", highest_student)
print("Top percentage:", round(highest_percentage, 2), "%")
print("Average class percentage:", round(average_percentage, 2), "%")