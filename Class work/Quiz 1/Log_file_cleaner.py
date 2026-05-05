"""
Log File Cleaner

Task:
1. Remove duplicate entries
2. Filter only ERROR logs
3. Count occurrences

Concepts used:
- set for uniqueness
- file handling
"""

# Input and output file paths
input_file = "Class work/Quiz 1/system_logs.txt"
output_file = "Class work/Quiz 1/clean_error_logs.txt"

# Set to keep unique ERROR lines
unique_error_logs = set()

# Dictionary to count each ERROR line occurrence
error_count = {}

# Read log file
try:
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            # Remove extra spaces/newline from left and right
            clean_line = line.strip()

            # Skip blank line
            if clean_line == "":
                continue

            # Keep only ERROR logs
            if "ERROR" in clean_line:
                # Add into set (duplicate entries auto removed)
                unique_error_logs.add(clean_line)

                # Count occurrence
                if clean_line in error_count:
                    error_count[clean_line] += 1
                else:
                    error_count[clean_line] = 1

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as error:
    print(f"Something went wrong while reading file: {error}")


# Write unique ERROR logs into new file
try:
    with open(output_file, "w", encoding="utf-8") as file:
        for log_line in sorted(unique_error_logs):
            file.write(log_line + "\n")
except Exception as error:
    print(f"Something went wrong while writing file: {error}")


# Display results
print("\n--- Log Cleaner Report ---")
print(f"Total unique ERROR logs: {len(unique_error_logs)}")
print(f"Output file: {output_file}")

print("\nERROR log occurrences:")
if len(error_count) == 0:
    print("No ERROR logs found.")
else:
    for log_line, count in error_count.items():
        print(f"{count} time(s) -> {log_line}")
