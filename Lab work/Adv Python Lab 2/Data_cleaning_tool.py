""" Data Cleaning Tool

Input file contains messy data:
- Remove null values
- Fix formatting issues
- Convert types safely using exception handling
"""


def clean_data(input_file="messy_data.csv", output_file="clean_data.csv"):
    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line_no, line in enumerate(infile, start=1):
            parts = [p.strip() for p in line.strip().split(",")]

            # Remove null/empty values
            if "" in parts or "null" in [p.lower() for p in parts]:
                continue

            # Fix formatting issues (title-case names/cities)
            if len(parts) >= 2:
                parts[1] = parts[1].title()
            if len(parts) >= 4:
                parts[3] = parts[3].title()

            # Convert types safely using exception handling
            try:
                if len(parts) >= 3:
                    parts[2] = str(int(parts[2]))
            except Exception as exc:
                print(f"Skipping line {line_no}: {exc}")
                continue

            outfile.write(",".join(parts) + "\n")


if __name__ == "__main__":
    clean_data()
    print("Cleaned data written to clean_data.csv")
