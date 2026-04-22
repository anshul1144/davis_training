"""7) Reverse file content line-wise into another file."""


def reverse_lines(input_file="input.txt", output_file="reversed_output.txt"):
    # Read all lines into a list
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # Write lines in reverse order
    with open(output_file, "w", encoding="utf-8") as outfile:
        for line in reversed(lines):
            outfile.write(line)


if __name__ == "__main__":
    reverse_lines()
    print("Reversed content saved to reversed_output.txt")
