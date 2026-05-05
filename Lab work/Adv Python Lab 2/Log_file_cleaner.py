"""Log File Cleaner

Given a log file:

Remove duplicate entries
Filter only ERROR logs
Count occurrences

Use:
- set for uniqueness
- file handling
"""


def clean_logs(input_file="app.log", output_file="error_unique.log"):
    seen = set()  # for uniqueness
    error_count = {}

    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            if "ERROR" not in line:
                continue

            # Count all error occurrences
            error_count[line.strip()] = error_count.get(line.strip(), 0) + 1

            # Write unique ERROR lines only
            if line not in seen:
                seen.add(line)
                outfile.write(line)

    print("Error occurrences:")
    for error_line, count in error_count.items():
        print(f"{count} -> {error_line}")


if __name__ == "__main__":
    clean_logs()
