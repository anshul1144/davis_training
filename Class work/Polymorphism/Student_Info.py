# Python program that manages student information and teachers.
class Person:
    # Constructor to initialize name and age.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display common person details.
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Student class inherits common properties and methods from Person.
class Student(Person):
    # Constructor to initialize student-specific details.
    def __init__(self, name, age, student_id, course, marks):
        # Call the parent class constructor to set name and age.
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

        # Set marks using the setter method so validation is applied.
        self.set_marks(marks)

    # Getter method to access the private marks attribute.
    def get_marks(self):
        return self.__marks

    # Setter method to update marks with validation.
    def set_marks(self, marks):
        # Marks must be between 0 and 100.
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    # Method to calculate grade based on marks.
    def calculate_grade(self):
        marks = self.get_marks()

        if marks >= 90:
            return "A"
        if marks >= 75:
            return "B"
        if marks >= 60:
            return "C"
        if marks >= 40:
            return "D"
        return "F"

    # Override display_details() to show student details and grade.
    def display_details(self):
        # Display name and age from the parent class.
        super().display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.get_marks()}")
        print(f"Grade: {self.calculate_grade()}")


# Teacher class inherits common properties and methods from Person.
class Teacher(Person):
    # Constructor to initialize teacher-specific details.
    def __init__(self, name, age, employee_id, subject):
        # Call the parent class constructor to set name and age.
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    # Override display_details() to show teacher details.
    def display_details(self):
        # Display name and age from the parent class.
        super().display_details()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")


# Function to take numeric input from the user with optional validation.
def input_number(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            # Check minimum value if it is provided.
            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            # Check maximum value if it is provided.
            if maximum is not None and value > maximum:
                print(f"Value must be at most {maximum}.")
                continue

            return value
        except ValueError:
            print("Please enter a valid number.")


# Function to take student details from the user.
def input_student():
    print("Enter Student Details")
    name = input("Name: ")
    age = input_number("Age: ", 0)
    student_id = input("Student ID: ")
    course = input("Course: ")
    marks = input_number("Marks: ", 0, 100)

    # Create and return a Student object.
    return Student(name, age, student_id, course, marks)


# Function to take teacher details from the user.
def input_teacher():
    print("Enter Teacher Details")
    name = input("Name: ")
    age = input_number("Age: ", 0)
    employee_id = input("Employee ID: ")
    subject = input("Subject: ")

    # Create and return a Teacher object.
    return Teacher(name, age, employee_id, subject)


# List to store both Student and Teacher objects.
people = []

# Ask the user how many records they want to enter.
student_count = input_number("How many students do you want to enter? ", 0)
teacher_count = input_number("How many teachers do you want to enter? ", 0)

# Take input for all students and add them to the list.
for index in range(student_count):
    print(f"\nStudent {index + 1}")
    people.append(input_student())

# Take input for all teachers and add them to the list.
for index in range(teacher_count):
    print(f"\nTeacher {index + 1}")
    people.append(input_teacher())

# Demonstrate polymorphism by calling display_details() on each object.
print("\nAll Details")
for person in people:
    person.display_details()
    print()
