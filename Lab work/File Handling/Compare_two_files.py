""" Find lines present in file1.txt but not in file2.txt."""


def compare_files(file1="file1.txt", file2="file2.txt"):
    # Read all lines of file2 into a set for fast lookup
    with open(file2, "r", encoding="utf-8") as f2:
        file2_lines = set(f2.readlines())

    # Print lines from file1 that are not in file2
    with open(file1, "r", encoding="utf-8") as f1:
        print("Lines in file1 but not in file2:")
        for line in f1:
            if line not in file2_lines:
                print(line.rstrip())


if __name__ == "__main__":
    compare_files()
