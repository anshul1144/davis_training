"""

A school stores student data in a file:
id,name,marks1,marks2,marks3

Build a system that:
- Reads file
- Calculates total, percentage
- Assigns grade using selection statements
- Handles missing/invalid data using exception handling
- Outputs toppers per class
"""

from pathlib import Path


def assign_grade(percentage):
    # Assign grade using selection statements
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def analyze_results(input_file="students_results.csv", output_file="student_report.csv"):
    # Resolve files relative to this script directory
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / input_file
    output_path = base_dir / output_file

    toppers = {}

    with open(input_path, "r", encoding="utf-8") as infile, open(
        output_path, "w", encoding="utf-8"
    ) as outfile:
        # Write output header
        outfile.write("id,name,class,total,percentage,grade\n")

        # Skip header if present
        first_line = infile.readline().strip()
        if "marks1" not in first_line.lower():
            infile.seek(0)

        for line_no, line in enumerate(infile, start=2):
            try:
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) != 6:
                    raise ValueError("Invalid column count")

                stu_id, name, m1, m2, m3, class_name = parts
                marks = [float(m1), float(m2), float(m3)]
                if any(m < 0 or m > 100 for m in marks):
                    raise ValueError("Marks out of range")

                total = sum(marks)
                percentage = total / 3
                grade = assign_grade(percentage)

                outfile.write(
                    f"{stu_id},{name},{class_name},{total:.2f},{percentage:.2f},{grade}\n"
                )

                # Track topper per class
                if class_name not in toppers or percentage > toppers[class_name][0]:
                    toppers[class_name] = (percentage, name, stu_id)

            except Exception as exc:
                # Handle missing/invalid data safely
                print(f"Skipped line {line_no}: {exc}")

    print("Topper(s) per class:")
    for class_name, (pct, name, stu_id) in toppers.items():
        print(f"Class {class_name}: {name} ({stu_id}) - {pct:.2f}%")


if __name__ == "__main__":
    analyze_results()
