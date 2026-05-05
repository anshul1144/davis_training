""" Remove duplicate lines from a file while preserving order."""


def remove_duplicates(input_file="input.txt", output_file="unique_lines.txt"):
    seen = set()

    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            # Keep exact line (including newline) to preserve original formatting
            if line not in seen:
                seen.add(line)
                outfile.write(line)


if __name__ == "__main__":
    remove_duplicates()
    print("Unique lines saved to unique_lines.txt")
