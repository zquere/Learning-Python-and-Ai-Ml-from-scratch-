"""
04 - POLYMORPHISM
=================

Poly = many
Morph = forms

Polymorphism means one interface/name can work with different
objects and produce different behavior.
"""

# ------------------------------------------------------------
# 1. METHOD OVERRIDING
# ------------------------------------------------------------

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


# ------------------------------------------------------------
# 2. DUCK TYPING
# ------------------------------------------------------------
# Python often cares about what an object CAN DO, not what class it is.

class Duck:
    def speak(self):
        print("Quack!")


class Person:
    def speak(self):
        print("Hello!")


def make_speak(obj):
    obj.speak()


make_speak(Duck())
make_speak(Person())


# ------------------------------------------------------------
# 3. OPERATOR OVERLOADING
# ------------------------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __eq__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return self.value == other.value

    def __repr__(self):
        return f"Number({self.value})"


a = Number(10)
b = Number(20)

print(a + b)
print(a == b)


# ------------------------------------------------------------
# 4. METHOD OVERLOADING — IMPORTANT PYTHON DETAIL
# ------------------------------------------------------------

class Hello:
    def speak(self, name=None, age=None):
        if name is None and age is None:
            print("Hello!")

        elif age is None:
            print(f"Hello {name}!")

        else:
            print(f"Hello {name}, age {age}!")


obj = Hello()
obj.speak()
obj.speak("Aman")
obj.speak("Aman", 21)

# IMPORTANT:
# Python does NOT support traditional method overloading like:
#
# def speak(self, a): ...
# def speak(self, a, b): ...
#
# The second definition would replace the first.
#
# Use default arguments, *args, **kwargs, or functools.singledispatch
# when you need multiple calling patterns.


# ------------------------------------------------------------
# 5. POLYMORPHISM WITH A COMMON FUNCTION
# ------------------------------------------------------------

class Circle:
    def area(self):
        return 3.14159 * 5 * 5


class Square:
    def area(self):
        return 10 * 10


def print_area(shape):
    print("Area:", shape.area())


print_area(Circle())
print_area(Square())
