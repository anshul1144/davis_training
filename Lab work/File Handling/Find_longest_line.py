""" Find the longest line in a file and print its length and content."""


def find_longest_line(file_name="input.txt"):
    longest_line = ""

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            # Compare line lengths after removing trailing newline
            current = line.rstrip("\n")
            if len(current) > len(longest_line):
                longest_line = current

    print("Length:", len(longest_line))
    print("Content:", longest_line)


if __name__ == "__main__":
    find_longest_line()
