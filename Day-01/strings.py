# ============================================================
# STRINGS
# ============================================================

text = "Hello Python"

print(text)
print(type(text))


# ------------------------------------------------------------
# INDEXING
# ------------------------------------------------------------

text = "Python"

print(text[0])
print(text[1])
print(text[2])

print(text[-1])
print(text[-2])


# ------------------------------------------------------------
# SLICING
# ------------------------------------------------------------

text = "Python Programming"

print(text[0:6])
print(text[7:18])

print(text[:6])
print(text[7:])

print(text[:])

print(text[::2])
print(text[::-1])       # Reverse


# structure:
#
# string[start:stop:step]


# ------------------------------------------------------------
# LENGTH
# ------------------------------------------------------------

text = "Python"

print(len(text))


# ------------------------------------------------------------
# CHANGE CASE
# ------------------------------------------------------------

text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())


# ------------------------------------------------------------
# REMOVE SPACES
# ------------------------------------------------------------

text = "   hello python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# ------------------------------------------------------------
# FIND
# ------------------------------------------------------------

text = "Hello Python"

print(text.find("Python"))
print(text.find("Java"))


# ------------------------------------------------------------
# COUNT
# ------------------------------------------------------------

text = "banana"

print(text.count("a"))
print(text.count("na"))


# ------------------------------------------------------------
# CHECK CONTENT
# ------------------------------------------------------------

text = "Python"

print(text.startswith("Py"))
print(text.endswith("on"))

print(text.isalpha())

number = "12345"

print(number.isdigit())

mixed = "Python123"

print(mixed.isalnum())


# ------------------------------------------------------------
# REPLACE
# ------------------------------------------------------------

text = "I like Java"

text = text.replace("Java", "Python")

print(text)


# ------------------------------------------------------------
# SPLIT
# ------------------------------------------------------------

text = "Python is easy"

words = text.split()

print(words)

text = "apple,banana,mango"

fruits = text.split(",")

print(fruits)


# ------------------------------------------------------------
# JOIN
# ------------------------------------------------------------

words = ["Python", "is", "awesome"]

text = " ".join(words)

print(text)

numbers = ["1", "2", "3"]

print("-".join(numbers))


# ------------------------------------------------------------
# REMOVE PREFIX / SUFFIX
# ------------------------------------------------------------

text = "HelloPython"

print(text.removeprefix("Hello"))
print(text.removesuffix("Python"))


# ------------------------------------------------------------
# STRING CONCATENATION
# ------------------------------------------------------------

first = "Hello"
second = "World"

print(first + " " + second)


# ------------------------------------------------------------
# REPEAT STRING
# ------------------------------------------------------------

print("Python " * 3)


# ------------------------------------------------------------
# MEMBERSHIP
# ------------------------------------------------------------

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ------------------------------------------------------------
# ESCAPE CHARACTERS
# ------------------------------------------------------------

print("Hello\nWorld")
print("Hello\tWorld")

print("He said \"Hello\"")


# ------------------------------------------------------------
# RAW STRING
# ------------------------------------------------------------

path = r"C:\Users\Python\Desktop"

print(path)


# ------------------------------------------------------------
# F-STRING
# ------------------------------------------------------------

name = "Alex"
age = 20

print(f"My name is {name} and I am {age}.")
