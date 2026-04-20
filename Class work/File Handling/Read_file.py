# program to read a file and print its content in file handling
file_name = "Class work/File Handling/hello.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"Error: '{file_name}' not found.")
except Exception as error:
    print(f"Something went wrong: {error}")
