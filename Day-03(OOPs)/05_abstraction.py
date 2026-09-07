"""
05 - ABSTRACTION
================

Abstraction focuses on WHAT an object must do rather than HOW
the object does it.

Python's standard way to create abstract base classes:
    ABC
    @abstractmethod
"""

from abc import ABC, abstractmethod


# ------------------------------------------------------------
# 1. BASIC ABSTRACT CLASS
# ------------------------------------------------------------

class Vehicle(ABC):

    @abstractmethod
    def engine_start(self):
        """Every concrete vehicle must implement this."""
        pass


class Bike(Vehicle):
    def engine_start(self):
        print("Bike engine started.")


class Car(Vehicle):
    def engine_start(self):
        print("Car engine started.")


bike = Bike()
car = Car()

bike.engine_start()
car.engine_start()

# Vehicle() would raise TypeError because it is abstract.


# ------------------------------------------------------------
# 2. ABSTRACT METHOD WITH SHARED CONCRETE METHOD
# ------------------------------------------------------------

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self):
        print("Payment receipt generated.")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card.")


payments = [UPI(), Card()]

for payment in payments:
    payment.pay(500)
    payment.receipt()


# ------------------------------------------------------------
# 3. ABSTRACT CLASS CAN HAVE __init__
# ------------------------------------------------------------

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print(f"{self.name} writes code.")


dev = Developer("Aman")
dev.work()


# ------------------------------------------------------------
# 4. YOUR ORIGINAL PATTERN — CORRECTED
# ------------------------------------------------------------

class Enforcer(ABC):

    @abstractmethod
    def engine_start(self):
        pass


class Bikes(Enforcer):

    def engine_start(self):
        print("Bike engine starts with a button.")


class Cars(Enforcer):

    def engine_start(self):
        print("Car engine starts with a key/button.")


class Truck(Enforcer):

    def engine_start(self):
        print("Truck engine starts with a heavy-duty system.")


vehicles = [Bikes(), Cars(), Truck()]

for vehicle in vehicles:
    vehicle.engine_start()


# ------------------------------------------------------------
# IMPORTANT
# ------------------------------------------------------------
# Use:
#     from abc import ABC, abstractmethod
#
# NOT:
#     abstractclassmethod
#
# `@abstractclassmethod` is an old/deprecated-style API.
# For normal abstract instance methods, use @abstractmethod.
#
# Also, abstract methods need `self` when they are instance methods:
#
#     def engine_start(self):
#         pass
#
# not:
#
#     def engine_start():
#         pass
