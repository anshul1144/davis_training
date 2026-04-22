""" Marks Improvement Tracker

Compare two exam files:
- Identify students who improved
- Calculate improvement %
"""


def load_marks(file_name):
    data = {}
    with open(file_name, "r", encoding="utf-8") as file:
        # Skip header if present
        first_line = file.readline().strip()
        if "marks" not in first_line.lower():
            file.seek(0)

        for line in file:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 3:
                continue
            stu_id, name, marks_text = parts
            try:
                data[stu_id] = (name, float(marks_text))
            except ValueError:
                continue
    return data


def track_improvement(file_exam1="exam1.csv", file_exam2="exam2.csv"):
    exam1 = load_marks(file_exam1)
    exam2 = load_marks(file_exam2)

    print("Students who improved:")
    for stu_id, (name2, marks2) in exam2.items():
        if stu_id in exam1:
            name1, marks1 = exam1[stu_id]
            if marks2 > marks1:
                improvement_pct = ((marks2 - marks1) / marks1) * 100 if marks1 != 0 else 100
                print(f"{stu_id} {name2}: {marks1} -> {marks2} ({improvement_pct:.2f}%)")


if __name__ == "__main__":
    track_improvement()
