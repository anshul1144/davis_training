# Student Result Management System

def get_marks(subjects):
    marks = {}
    for subject in subjects:
        while True:
            value = input(f"Enter marks for {subject} (0-100, blank if missing): ").strip()
            if not value:
                break
            try:
                mark = float(value)
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")
    return marks


def result(student, subjects):
    marks = student["marks"]
    total = sum(marks.get(subject, 0) for subject in subjects)
    percentage = total / len(subjects)
    passed = len(marks) == len(subjects) and all(mark >= 35 for mark in marks.values())
    grade = "A" if percentage >= 75 else "B" if percentage >= 60 else "C" if percentage >= 50 else "D" if percentage >= 35 else "F"
    return total, percentage, grade, "Pass" if passed else "Fail"


def show_student(student_id, student, subjects):
    total, percentage, grade, status = result(student, subjects)
    marks = ", ".join(f"{subject}: {student['marks'].get(subject, 'Missing')}" for subject in subjects)
    print(f"{student_id} - {student['name']} | {marks}")
    print(f"Total: {total:g}/{len(subjects) * 100}, Percentage: {percentage:.2f}%, Grade: {grade}, Status: {status}")


def student_result_management():
    students = {}
    subjects = [subject.strip() for subject in input("Enter subjects, separated by commas: ").split(",") if subject.strip()]
    if not subjects:
        print("At least one subject is required.")
        return

    while True:
        print("\n1. Add  2. Delete  3. Update  4. View  5. Summary  6. Exit")
        choice = input("Choose an option: ")

        if choice in ("1", "3"):
            student_id = input("Student ID: ")
            if choice == "3" and student_id not in students:
                print("Student not found.")
                continue
            name = input("Student name: ")
            students[student_id] = {"name": name, "marks": get_marks(subjects)}
            print("Student result saved.")
        elif choice == "2":
            student_id = input("Student ID to delete: ")
            print("Deleted." if students.pop(student_id, None) else "Student not found.")
        elif choice == "4":
            if not students:
                print("No student results available.")
            for student_id, student in students.items():
                show_student(student_id, student, subjects)
        elif choice == "5":
            if not students:
                print("No student results available.")
                continue
            percentages = {student_id: result(student, subjects)[1] for student_id, student in students.items()}
            print(f"Class average: {sum(percentages.values()) / len(percentages):.2f}%")
            topper = max(percentages, key=percentages.get)
            print(f"Topper: {students[topper]['name']} ({percentages[topper]:.2f}%)")
            for subject in subjects:
                entered = {student_id: student["marks"][subject] for student_id, student in students.items() if subject in student["marks"]}
                if entered:
                    highest = max(entered, key=entered.get)
                    print(f"Highest in {subject}: {students[highest]['name']} ({entered[highest]:g})")
                else:
                    print(f"Highest in {subject}: No marks entered")
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    student_result_management()


