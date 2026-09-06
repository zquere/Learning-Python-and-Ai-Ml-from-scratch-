"""
01 - OOP BASICS
===============

OOP (Object-Oriented Programming) organizes code around objects.

Core vocabulary:
    Class       -> blueprint
    Object      -> instance created from a class
    Attribute   -> data/state
    Method      -> behavior/function belonging to a class
    __init__    -> constructor/initializer called when an object is created
"""

# ------------------------------------------------------------
# 1. CLASS AND OBJECT
# ------------------------------------------------------------

class Bag:
    company = "Super_D"       # class attribute: shared by instances

    def details(self):
        print("This company creates bags.")


bag1 = Bag()
bag2 = Bag()

print(bag1.company)
print(bag2.company)
bag1.details()


# ------------------------------------------------------------
# 2. INSTANCE ATTRIBUTES + __init__
# ------------------------------------------------------------

class Bags:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets


rebook = Bags("leather", 3, 2)
campus = Bags("polyester", 2, 4)

print(rebook.material)
print(campus.material)


# ------------------------------------------------------------
# 3. self
# ------------------------------------------------------------

class Animal:
    species = "Animal"

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}.")


lion = Animal("Lion")
lion.hello()

# `self` refers to the current object.
# Python effectively calls:
# Animal.hello(lion)


# ------------------------------------------------------------
# 4. CLASS METHOD
# ------------------------------------------------------------

class Company:
    country = "India"

    @classmethod
    def show_country(cls):
        print(f"Company country: {cls.country}")


Company.show_country()
company = Company()
company.show_country()


# ------------------------------------------------------------
# 5. STATIC METHOD
# ------------------------------------------------------------

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))


# ------------------------------------------------------------
# 6. __str__ AND __repr__
# ------------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r})"


student = Student("Aman", 20)
print(student)
print(repr(student))


# ------------------------------------------------------------
# 7. isinstance() / issubclass()
# ------------------------------------------------------------

class Human:
    pass

class Developer(Human):
    pass


dev = Developer()

print(isinstance(dev, Developer))  # True
print(isinstance(dev, Human))      # True
print(issubclass(Developer, Human)) # True


# ------------------------------------------------------------
# 8. COMPOSITION
# ------------------------------------------------------------
# A "has-a" relationship.
# Inheritance = "is-a"
# Composition = "has-a"

class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started.")


car = Car()
car.start()
