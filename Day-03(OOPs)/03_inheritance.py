"""
03 - INHERITANCE
================

Inheritance allows a child class to reuse/extend a parent class.

Relationship:
    Child IS-A Parent

Types demonstrated:
    1. Single inheritance
    2. Multilevel inheritance
    3. Multiple inheritance
    4. Hierarchical inheritance
"""

# ------------------------------------------------------------
# 1. SINGLE INHERITANCE
# ------------------------------------------------------------

class Animal:
    species = "Animal"

    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Name: {self.name}")


class Human(Animal):
    def walk(self):
        print(f"{self.name} is walking.")


person = Human("Lemon")
person.details()
person.walk()
print(person.species)


# ------------------------------------------------------------
# 2. super()
# ------------------------------------------------------------

class BagFactory:
    def __init__(self, material, pockets, zips):
        self.material = material
        self.pockets = pockets
        self.zips = zips

    def details(self):
        print(f"Material: {self.material}")
        print(f"Pockets: {self.pockets}")
        print(f"Zips: {self.zips}")


class Reebok(BagFactory):
    def __init__(self, material, pockets, zips, color):
        super().__init__(material, pockets, zips)
        self.color = color

    def details(self):
        print(f"Color: {self.color}")
        super().details()


bag = Reebok("plastic", 4, 1, "pink")
bag.details()


# ------------------------------------------------------------
# 3. MULTILEVEL INHERITANCE
# ------------------------------------------------------------

class A:
    def method_a(self):
        print("A")


class B(A):
    def method_b(self):
        print("B")


class C(B):
    def method_c(self):
        print("C")


obj = C()
obj.method_a()
obj.method_b()
obj.method_c()


# ------------------------------------------------------------
# 4. MULTIPLE INHERITANCE
# ------------------------------------------------------------

class Human:
    def human_info(self):
        print("Human behavior")


class Machine:
    def machine_info(self):
        print("Machine behavior")


class Robot(Human, Machine):
    pass


robot = Robot()
robot.human_info()
robot.machine_info()


# Constructor example with multiple inheritance:
class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id


class Developer(Person, Employee):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)


developer = Developer("Aman", 101)
print(developer.name, developer.employee_id)


# ------------------------------------------------------------
# 5. HIERARCHICAL INHERITANCE
# ------------------------------------------------------------

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


Car().start()
Bike().start()


# ------------------------------------------------------------
# 6. METHOD OVERRIDING
# ------------------------------------------------------------

class Parent:
    def speak(self):
        print("Parent speaking")


class Child(Parent):
    def speak(self):
        print("Child speaking")


child = Child()
child.speak()  # Child's implementation wins


# ------------------------------------------------------------
# 7. MRO — METHOD RESOLUTION ORDER
# ------------------------------------------------------------

class X:
    pass

class Y(X):
    pass

class Z(Y):
    pass


print(Z.mro())

# Python searches methods according to the MRO.
# Multiple inheritance uses C3 linearization to build this order.
