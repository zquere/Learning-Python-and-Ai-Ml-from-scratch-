"""
02 - ENCAPSULATION
==================

Encapsulation means keeping related data and behavior together
inside a class and controlling how that data is accessed/changed.

Python access conventions:
    public      -> name
    protected   -> _name       (convention, not strict protection)
    private     -> __name      (name mangling)
"""

# ------------------------------------------------------------
# 1. PUBLIC
# ------------------------------------------------------------

class Car:
    def __init__(self, brand):
        self.brand = brand


car = Car("Nissan")
print(car.brand)
car.brand = "Maruti"   # public data can be changed directly
print(car.brand)


# ------------------------------------------------------------
# 2. PROTECTED (CONVENTION)
# ------------------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def show_balance(self):
        print(f"Balance: {self._balance}")


account = BankAccount(5000)
account.show_balance()

# `_balance` means:
# "This is intended for internal/subclass use."
# Python does NOT strictly block access.


# ------------------------------------------------------------
# 3. PRIVATE + NAME MANGLING
# ------------------------------------------------------------

class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = SecureAccount(1000)
account.deposit(500)
print(account.get_balance())

# account.__balance -> AttributeError
# Internally Python changes the name approximately to:
# _SecureAccount__balance


# ------------------------------------------------------------
# 4. @property — PYTHONIC ENCAPSULATION
# ------------------------------------------------------------

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


product = Product(999)
print(product.price)

product.price = 1200
print(product.price)

# product.price = -50  # ValueError


# ------------------------------------------------------------
# 5. ENCAPSULATION IN A REALISTIC EXAMPLE
# ------------------------------------------------------------

class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    def profile(self):
        return f"{self.username} is {self.age} years old."


user = User("developer", 21)
print(user.profile())
