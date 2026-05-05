""" Filter students scoring above 75 from students.txt."""


def filter_students(input_file="students.txt", output_file="top_students.txt"):
    # Open source file for reading and target file for writing
    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            # Remove extra spaces/newline
            clean_line = line.strip()
            if not clean_line:
                continue

            # Expected format: Name,Marks,City
            parts = clean_line.split(",")
            if len(parts) != 3:
                continue

            name, marks_text, city = [part.strip() for part in parts]
            if not marks_text.isdigit():
                continue

            marks = int(marks_text)

            # Save only records with marks above 75
            if marks > 75:
                outfile.write(f"{name},{marks},{city}\n")


if __name__ == "__main__":
    filter_students()
    print("Filtered records saved to top_students.txt")
