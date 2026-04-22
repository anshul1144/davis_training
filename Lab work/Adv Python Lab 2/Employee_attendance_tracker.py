"""Employee Attendance Tracker

File contains:
emp_id,date,status

Tasks:
- Count present/absent days
- Detect employees with low attendance (<75%)
"""


def track_attendance(file_name="attendance.csv"):
    stats = {}

    with open(file_name, "r", encoding="utf-8") as file:
        # Skip header if present
        first_line = file.readline().strip()
        if "emp_id" not in first_line.lower():
            file.seek(0)

        for line in file:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) != 3:
                continue

            emp_id, _date, status = parts
            status = status.lower()
            if emp_id not in stats:
                stats[emp_id] = {"present": 0, "absent": 0}

            if status == "present":
                stats[emp_id]["present"] += 1
            elif status == "absent":
                stats[emp_id]["absent"] += 1

    print("Attendance summary:")
    for emp_id, data in stats.items():
        total = data["present"] + data["absent"]
        pct = (data["present"] / total) * 100 if total else 0
        print(f"{emp_id}: Present={data['present']} Absent={data['absent']} Attendance={pct:.2f}%")
        if pct < 75:
            print(f"  Low attendance alert for {emp_id}")


if __name__ == "__main__":
    track_attendance()
