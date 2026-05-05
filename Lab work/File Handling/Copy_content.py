""" Copy contents of one file into another."""


def copy_file_content(source_file, destination_file):
    # Read full content from source file
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

    # Write content into destination file
    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)


def main():
    # Take file names from user
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    copy_file_content(source, destination)
    print("Content copied successfully.")


if __name__ == "__main__":
    main()
