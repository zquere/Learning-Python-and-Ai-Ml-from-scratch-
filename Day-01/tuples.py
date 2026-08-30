# ============================================================
# TUPLES
# ============================================================

numbers = (1, 2, 3, 4, 5)

print(numbers)
print(type(numbers))


# Indexing

print(numbers[0])
print(numbers[-1])


# Slicing

print(numbers[1:4])


# Count

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2))


# Index

print(numbers.index(3))


# Length

print(len(numbers))


# Membership

print(2 in numbers)


# Tuple unpacking

person = ("Alex", 20, "India")

name, age, country = person

print(name)
print(age)
print(country)
