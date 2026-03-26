# Program to calculate_grade(marks) of the students.

#............................................................

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


for i in range(1, 6):
    marks = int(input(f"Enter marks for student {i}: "))
    grade = calculate_grade(marks)
    print(f"Student {i}: Marks = {marks}, Grade = {grade}")

#............................................................
""" Output:
Enter marks for student 1: 95
Student 1: Marks = 95, Grade = A
Enter marks for student 2: 82
Student 2: Marks = 82, Grade = B
Enter marks for student 3: 67
Student 3: Marks = 67, Grade = C
Enter marks for student 4: 45
Student 4: Marks = 45, Grade = Fail
Enter marks for student 5: 90
Student 5: Marks = 90, Grade = A
"""
