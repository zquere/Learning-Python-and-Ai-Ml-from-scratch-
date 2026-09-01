"""
Python for AI/ML — File Handling
---------------------------------

Today we learn how Python works with files.

Topics:
1. Creating files
2. Writing files
3. Appending data
4. Reading files
5. The `with open()` pattern
6. Reading line-by-line
7. pathlib
8. CSV
9. JSON
10. Error handling
11. Practical AI/ML-style example
"""


# ============================================================
# 1. CREATING A FILE
# ============================================================

# "x" creates a new file.
#
# IMPORTANT:
# If the file already exists, Python raises FileExistsError.

# file = open("file.txt", "x")
# file.close()


# ============================================================
# 2. WRITING TO A FILE
# ============================================================

# "w" = write mode.
#
# WARNING:
# If the file already contains data, "w" replaces everything.

with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("I am learning file handling.\n")


# ============================================================
# 3. APPENDING TO A FILE
# ============================================================

# "a" = append mode.
#
# Existing data is preserved.
# New data is added at the end.

with open("file.txt", "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")


# ============================================================
# 4. READING A FILE
# ============================================================

with open("file.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)


# ============================================================
# 5. WHY USE `with`?
# ============================================================

# This is the professional way to work with files.

with open("file.txt", "r", encoding="utf-8") as file:
    data = file.read()

# Python automatically closes the file
# when the `with` block ends.


# ============================================================
# 6. READ DIFFERENT WAYS
# ============================================================

# read() → reads the entire file

with open("file.txt", "r", encoding="utf-8") as file:
    print(file.read())


# readline() → reads one line

with open("file.txt", "r", encoding="utf-8") as file:
    print(file.readline())


# readlines() → returns all lines as a list

with open("file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)


# ============================================================
# 7. READING LINE BY LINE
# ============================================================

# This is better for large files because we don't
# have to load the entire file into memory.

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# ============================================================
# 8. FILE MODES
# ============================================================

"""
r   → read
w   → write (overwrites)
a   → append
x   → create a new file
r+  → read + write
w+  → write + read (overwrites)
a+  → append + read
"""


# ============================================================
# 9. pathlib — MODERN PYTHON
# ============================================================

from pathlib import Path

file_path = Path("example.txt")

# Write
file_path.write_text(
    "Hello from pathlib!",
    encoding="utf-8"
)

# Read
content = file_path.read_text(encoding="utf-8")

print(content)


# Check whether a file exists

if file_path.exists():
    print("File exists!")


# ============================================================
# 10. ERROR HANDLING
# ============================================================

try:
    with open("does_not_exist.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")


# ============================================================
# 11. JSON — VERY IMPORTANT FOR AI/ML
# ============================================================

import json

config = {
    "model": "neural_network",
    "learning_rate": 0.001,
    "epochs": 10
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)


# Reading JSON

with open("config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(loaded_config)
print(loaded_config["learning_rate"])


# ============================================================
# 12. CSV — DATA SCIENCE / AI / ML
# ============================================================

import csv

students = [
    ["name", "age", "score"],
    ["Alex", 20, 85],
    ["Sam", 22, 91],
    ["John", 21, 78],
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)


# Reading CSV

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# 13. PRACTICAL AI/ML EXAMPLE
# ============================================================

# Imagine we have a dataset containing training data.

training_data = [
    "cat,1",
    "dog,0",
    "cat,1",
    "dog,0",
]

with open("training_data.txt", "w", encoding="utf-8") as file:
    for row in training_data:
        file.write(row + "\n")


# Reading the dataset

with open("training_data.txt", "r", encoding="utf-8") as file:

    for row in file:
        animal, label = row.strip().split(",")

        print("Animal:", animal)
        print("Label:", label)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
Remember:

open()
    ↓
file modes
    ↓
read / write / append
    ↓
with open()
    ↓
pathlib
    ↓
JSON / CSV
    ↓
datasets
    ↓
AI / ML data pipelines
"""
