# Write a program to assign grade based on marks.

# Function to assign grade based on marks
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
# Get user input
marks = int(input("Enter your marks: "))
grade = assign_grade(marks)
print(f"Your grade is: {grade}")

""" Output:
Enter your marks: 82
Your grade is: B
"""