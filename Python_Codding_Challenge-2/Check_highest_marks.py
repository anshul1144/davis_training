# Write a program to find student with highest marks from dictionary.

# Function to find student with highest marks
def find_highest_marks(marks_dict):
    highest_student = max(marks_dict, key=marks_dict.get)
    return highest_student

# Get user input
marks_input = input("Enter student marks in the format 'Name:Marks' separated by commas: ")
marks_dict = {}
for item in marks_input.split(','):
    name, marks = item.split(':')
    marks_dict[name.strip()] = int(marks.strip())
highest_student = find_highest_marks(marks_dict)
print(f"Student with the highest marks: {highest_student}")

""" Output:
Enter student marks in the format 'Name:Marks' separated by commas: A:80,B:95,C:78
Student with the highest marks: B
"""
