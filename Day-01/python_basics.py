# ============================================================
# PYTHON BASICS
# ============================================================


# ------------------------------------------------------------
# 1. PRINT
# ------------------------------------------------------------

print("Hello World")
print(10)
print(10 + 20)

name = "Alex"
age = 20

print(name)
print(age)

print("Name:", name)
print("Age:", age)


# ------------------------------------------------------------
# 2. VARIABLES
# ------------------------------------------------------------

name = "Alex"
age = 20
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# Multiple variables

x, y, z = 10, 20, 30

print(x, y, z)


# Same value

a = b = c = 100

print(a, b, c)


# ------------------------------------------------------------
# 3. TYPE
# ------------------------------------------------------------

name = "Python"
age = 20
height = 5.8
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))


# ------------------------------------------------------------
# 4. COMMENTS
# ------------------------------------------------------------

# This is a single-line comment.

"""
This is a
multi-line string.
It can also be used as a block comment.
"""


# ------------------------------------------------------------
# 5. INPUT
# ------------------------------------------------------------

name = input("Enter your name: ")

print("Hello", name)


# IMPORTANT:
# input() always returns a string.

age = input("Enter your age: ")

print(type(age))


# Convert input to integer

age = int(input("Enter your age: "))

print(age)
print(type(age))


# ------------------------------------------------------------
# 6. F-STRINGS
# ------------------------------------------------------------

name = "Alex"
age = 20

print(f"My name is {name}")
print(f"I am {age} years old.")

print(f"{name} is {age} years old.")


# ------------------------------------------------------------
# 7. BASIC ARITHMETIC
# ------------------------------------------------------------

a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Remainder
print(a ** b)   # Power


# ------------------------------------------------------------
# 8. COMPARISON
# ------------------------------------------------------------

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ------------------------------------------------------------
# 9. LOGICAL OPERATORS
# ------------------------------------------------------------

age = 20

print(age > 18 and age < 30)
print(age < 18 or age > 60)
print(not age > 18)


# ------------------------------------------------------------
# 10. ASSIGNMENT OPERATORS
# ------------------------------------------------------------

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)
