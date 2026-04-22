"""6) Merge file1.txt and file2.txt into one file with line numbers."""


def merge_files_with_line_numbers(
    file1="file1.txt", file2="file2.txt", output_file="merged_file.txt"
):
    line_no = 1

    with open(output_file, "w", encoding="utf-8") as outfile:
        # Read and write lines from first file
        with open(file1, "r", encoding="utf-8") as f1:
            for line in f1:
                outfile.write(f"{line_no}. {line.rstrip()}\n")
                line_no += 1

        # Read and write lines from second file
        with open(file2, "r", encoding="utf-8") as f2:
            for line in f2:
                outfile.write(f"{line_no}. {line.rstrip()}\n")
                line_no += 1


if __name__ == "__main__":
    merge_files_with_line_numbers()
    print("Files merged into merged_file.txt")
