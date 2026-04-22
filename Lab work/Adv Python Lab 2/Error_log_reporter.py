""" Error Log Reporter

Read error logs:
- Group by error type
- Count occurrences
- Write summary file
"""


def parse_error_type(line):
    # Example format: [ERROR] Type:DatabaseError Message:...
    if "Type:" in line:
        return line.split("Type:", 1)[1].split()[0].strip()
    return "UnknownError"


def report_errors(input_file="error.log", summary_file="error_summary.txt"):
    counts = {}

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if "ERROR" in line:
                err_type = parse_error_type(line)
                counts[err_type] = counts.get(err_type, 0) + 1

    with open(summary_file, "w", encoding="utf-8") as out:
        for err_type, count in counts.items():
            out.write(f"{err_type}: {count}\n")

    print("Error summary generated in", summary_file)


if __name__ == "__main__":
    report_errors()
