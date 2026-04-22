""" Custom Sorting Engine

Sort list of tuples:
(name, marks, age)

Sort by:
- marks desc
- age asc

Without using built-in sorted() (implement logic manually)
"""


def compare_records(a, b):
    # Primary: marks descending
    if a[1] != b[1]:
        return a[1] > b[1]
    # Secondary: age ascending
    return a[2] < b[2]


def custom_sort(records):
    # Manual bubble sort logic
    n = len(records)
    result = records[:]

    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare_records(result[j], result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    students = [
        ("Riya", 85, 17),
        ("Aman", 92, 18),
        ("Zoya", 92, 16),
        ("Karan", 76, 19),
    ]

    print("Sorted records:")
    for row in custom_sort(students):
        print(row)
