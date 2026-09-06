# 🐍 Python OOP
### From Classes & Objects → Software Design → Real-World Python

<div align="center">

**A complete, structured OOP learning path for Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Topic-OOP-FFB000)](#-the-four-pillars-of-oop)
[![Level](https://img.shields.io/badge/Level-Scratch%20%2B%20Advanced-8A2BE2)](#-learning-roadmap)

> **Don't learn OOP just to write classes.  
> Learn OOP to design software.**

</div>

---

## 🧭 What is this?

This folder is my **complete Python Object-Oriented Programming journey**.

It starts with the basics:

```text
Class → Object → Attribute → Method
```

and gradually moves toward:

```text
Encapsulation
      ↓
Inheritance
      ↓
Polymorphism
      ↓
Abstraction
      ↓
Object Model
      ↓
Advanced Python OOP
      ↓
SOLID & Design Patterns
      ↓
Software Architecture
      ↓
Real-World Projects
```

The README is designed as a **permanent roadmap**, so it does not need to be rewritten every time a new OOP concept is learned.

---

# 📁 Repository Structure

```text
OOP/
│
├── 📄 README.md
│
├── 🟢 01_oop_basics.py
├── 🔵 02_encapsulation.py
├── 🟣 03_inheritance.py
├── 🟠 04_polymorphism.py
├── 🔴 05_abstraction.py
│
└── 🚧 More advanced OOP topics
    ├── object model
    ├── dunder methods
    ├── descriptors
    ├── dataclasses
    ├── protocols
    ├── SOLID
    ├── design patterns
    ├── testing
    └── architecture
```

> The numbered files represent the main learning sequence.  
> Advanced concepts can be added later without changing the overall roadmap.

---

# 🧠 The Four Pillars of OOP

These are the **four major pillars** that form the foundation of Object-Oriented Programming.

| Pillar | What it means | Main question |
|:---|:---|:---|
| 🔒 **Encapsulation** | Bundle data + behavior and control access | *How do I protect/manage state?* |
| 🧬 **Inheritance** | Reuse and extend existing classes | *How can one class build on another?* |
| 🔄 **Polymorphism** | One interface, different behavior | *How can different objects respond differently?* |
| 🎭 **Abstraction** | Expose essential behavior, hide implementation | *What should this object do?* |

### The simple mental model

```text
                 🧱 OOP
                   │
       ┌───────────┼───────────┐
       │           │           │
   🔒 Encapsulation 🧬 Inheritance
       │           │
       └──────┬────┘
              │
        🔄 Polymorphism
              │
        🎭 Abstraction
```

---

# 🚀 Learning Roadmap

## 01 · OOP Fundamentals

**Start here.**

- What is OOP?
- Why OOP?
- Procedural vs OOP
- Classes
- Objects / instances
- Attributes
- Methods
- `self`
- `__init__`
- Constructors / initializers
- Instance attributes
- Class attributes
- Instance methods
- Class methods
- Static methods
- `cls`
- `type()`
- `isinstance()`
- `issubclass()`
- Object identity
- `id()`
- `__str__`
- `__repr__`

📄 `01_oop_basics.py`

---

## 02 · 🔒 Encapsulation

Learn how objects manage and protect their internal state.

- Public attributes
- Protected convention: `_name`
- Private attributes: `__name`
- Name mangling
- Getters
- Setters
- `@property`
- Property setters
- Property deleters
- Read-only properties
- Data validation
- Internal state
- Interface vs implementation

📄 `02_encapsulation.py`

---

## 03 · 🧬 Inheritance

Learn how classes reuse and extend other classes.

### Types

- Single inheritance
- Multilevel inheritance
- Multiple inheritance
- Hierarchical inheritance
- Hybrid inheritance

### Core concepts

- Parent / base / superclass
- Child / derived / subclass
- Constructor inheritance
- Constructor overriding
- `super()`
- Method overriding
- Attribute inheritance
- `isinstance()`
- `issubclass()`

### Advanced

- MRO
- `ClassName.mro()`
- `__mro__`
- Diamond problem
- Cooperative inheritance
- C3 linearization
- Mixins

📄 `03_inheritance.py`

---

## 04 · 🔄 Polymorphism

**One interface → many forms.**

- Method overriding
- Duck typing
- Common interfaces
- Polymorphic functions
- EAFP style
- Default arguments
- `*args`
- `**kwargs`
- `functools.singledispatch`
- `singledispatchmethod`
- Operator overloading
- Rich comparisons

Examples include:

```python
animal.speak()
shape.area()
payment.pay()
```

The caller does not need to know the exact implementation.

📄 `04_polymorphism.py`

---

## 05 · 🎭 Abstraction

Focus on **what** an object must do instead of exposing **how** it does it.

- `ABC`
- `@abstractmethod`
- Abstract classes
- Abstract methods
- Concrete methods
- Abstract constructors
- Abstract properties
- Abstract class methods
- Abstract static methods
- Interfaces
- `typing.Protocol`
- Structural typing
- Runtime-checkable protocols

📄 `05_abstraction.py`

---

# ⚙️ Advanced OOP

After the four pillars, go deeper into Python's object model.

## 06 · Python Object Model

- Everything is an object
- Objects and types
- `object`
- `type`
- Class namespaces
- Instance namespaces
- `__dict__`
- `__class__`
- `__bases__`
- `__subclasses__`
- Attribute lookup
- Attribute shadowing
- MRO
- Descriptor-based lookup

---

## 07 · 🪄 Dunder / Magic Methods

Learn how custom objects interact naturally with Python.

### Representation

```text
__str__
__repr__
__format__
__bytes__
```

### Comparison

```text
__eq__
__ne__
__lt__
__le__
__gt__
__ge__
__hash__
```

### Arithmetic

```text
__add__
__sub__
__mul__
__truediv__
__floordiv__
__mod__
__pow__
__radd__
...
```

### Containers

```text
__len__
__getitem__
__setitem__
__delitem__
__contains__
__iter__
__next__
```

### Other behavior

```text
__call__
__enter__
__exit__
__getattr__
__getattribute__
__setattr__
__delattr__
__new__
__init__
```

---

# 🧩 08 · Composition & Object Relationships

Not every problem should be solved with inheritance.

### Inheritance

```text
Car IS-A Vehicle
```

### Composition

```text
Car HAS-A Engine
```

### Aggregation

```text
Department HAS Employees
```

### Association

```text
Teacher WORKS WITH Students
```

Learn when to choose:

```text
Inheritance
     vs
Composition
```

This becomes extremely important in real software design.

---

# 🏭 09 · Object Creation

Go deeper into how Python creates objects.

- `__new__`
- `__init__`
- Alternative constructors
- `@classmethod` constructors
- Factory methods
- Factory pattern
- Copying objects
- `copy.copy()`
- `copy.deepcopy()`
- Mutable vs immutable objects
- Object lifecycle

---

# 🧰 10 · Properties & Descriptors

Move beyond simple getters and setters.

- `property`
- Computed properties
- Validation
- Read-only properties
- Custom descriptors
- `__get__`
- `__set__`
- `__delete__`
- `__set_name__`
- Data descriptors
- Non-data descriptors
- Why functions become methods

---

# 🧠 11 · Advanced Class Features

- Class decorators
- Method decorators
- `@classmethod`
- `@staticmethod`
- `@property`
- `__init_subclass__`
- `__set_name__`
- Dynamic class creation
- `type()` for creating classes
- `__slots__`
- Custom metaclasses

---

# 📦 12 · Dataclasses

Modern Python provides `dataclasses` for classes that primarily represent data.

- `@dataclass`
- `field()`
- Default values
- Default factories
- Frozen dataclasses
- Ordering
- `__post_init__`
- Dataclass inheritance
- `asdict()`
- `astuple()`
- Dataclass vs normal class

---

# 🧬 13 · Deep Dive: Multiple Inheritance

Understand what actually happens when several classes are involved.

```text
        A
       /       B   C
       \ /
        D
```

Topics:

- Diamond problem
- MRO
- C3 linearization
- Cooperative `super()`
- Mixin design
- Multiple inheritance pitfalls

---

# 🔌 14 · Interfaces & Protocols

Python does not require Java-style interfaces to achieve interface-based design.

Learn:

- ABCs
- Abstract interfaces
- `typing.Protocol`
- Structural subtyping
- Nominal vs structural typing
- Protocol composition
- `@runtime_checkable`

---

# 🏗️ 15 · SOLID Principles

Once the OOP foundation is strong, learn the principles behind maintainable object-oriented systems.

| Principle | Meaning |
|:---|:---|
| **S** | Single Responsibility |
| **O** | Open / Closed |
| **L** | Liskov Substitution |
| **I** | Interface Segregation |
| **D** | Dependency Inversion |

> SOLID is about **design quality**, not just syntax.

---

# 🧰 16 · Design Patterns

Learn patterns as solutions to recurring design problems.

### Creational

- Factory
- Factory Method
- Abstract Factory
- Builder
- Singleton — including why it can be overused

### Structural

- Adapter
- Decorator
- Facade
- Proxy
- Composite

### Behavioral

- Strategy
- Observer
- Command
- State
- Template Method
- Iterator

**Goal:** understand *why* a pattern is useful instead of memorizing names.

---

# 🧹 17 · OOP Best Practices

Good OOP is not about making everything a class.

Learn to:

- Keep classes focused
- Prefer composition when appropriate
- Avoid unnecessary inheritance
- Avoid extremely deep inheritance trees
- Keep public APIs small
- Validate state
- Use meaningful names
- Use type hints
- Write docstrings
- Handle errors clearly
- Test behavior
- Reduce coupling
- Prefer simple designs

---

# 🧪 18 · Testing OOP

Learn to prove that objects behave correctly.

- Unit testing
- `unittest`
- `pytest`
- Fixtures
- Mocking
- Testing properties
- Testing inheritance
- Testing polymorphism
- Testing composition
- Testing exceptions
- Test-driven development basics

---

# 🏛️ 19 · OOP Architecture

Move from individual classes to complete systems.

- Separation of concerns
- Layered architecture
- Service classes
- Repository pattern
- Dependency injection
- Dependency inversion
- Domain models
- DTO-style objects
- Configuration objects
- Package organization
- Public vs internal APIs
- Loose coupling
- High cohesion

---

# 💻 20 · Real-World OOP Projects

The final test of OOP knowledge is **building things**.

Possible projects:

```text
📁 File Manager
🏦 Banking System
📚 Library Management System
🛒 E-Commerce System
👨‍💼 Employee Management System
🎮 Game Architecture
💻 CLI Application
🌐 API Client
🗄️ Database Application
⚙️ Automation Tool
```

The progression should be:

```text
I know classes
      ↓
I can create objects
      ↓
I understand the 4 pillars
      ↓
I can design interacting objects
      ↓
I can choose composition vs inheritance
      ↓
I can design maintainable systems
```

---

# 🤖 Why OOP Matters for AI/ML

OOP becomes especially useful when you start working with larger Python libraries.

You will frequently encounter APIs like:

```python
model = Model(...)
model.fit(...)
model.predict(...)
```

or:

```python
dataset = Dataset(...)
loader = DataLoader(...)
```

Understanding OOP helps you recognize:

```text
Model        → Object
Model(...)   → Constructor
.fit()       → Method
.predict()   → Method
parameters   → Attributes
```

Many advanced Python and AI/ML libraries are built around objects, classes, inheritance, composition, and interfaces.

So OOP is not a side topic.

It is part of the foundation for understanding **large Python codebases and frameworks**.

---

# 📊 Learning Progress

Use this as a permanent checklist.

### 🟢 Foundations

- [ ] Classes
- [ ] Objects
- [ ] Attributes
- [ ] Methods
- [ ] `self`
- [ ] `__init__`
- [ ] Class attributes
- [ ] Instance attributes
- [ ] Class methods
- [ ] Static methods
- [ ] `__str__`
- [ ] `__repr__`

### 🔵 Four Pillars

- [ ] Encapsulation
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Abstraction

### 🟣 Intermediate

- [ ] `super()`
- [ ] Method overriding
- [ ] Method overloading alternatives
- [ ] Duck typing
- [ ] Operator overloading
- [ ] Composition
- [ ] Aggregation
- [ ] Association
- [ ] MRO
- [ ] Multiple inheritance

### 🟠 Advanced Python OOP

- [ ] Dunder methods
- [ ] Object model
- [ ] Properties
- [ ] Descriptors
- [ ] `__new__`
- [ ] Dataclasses
- [ ] `__slots__`
- [ ] Mixins
- [ ] Protocols
- [ ] Metaclasses
- [ ] `__init_subclass__`

### 🔴 Software Design

- [ ] SOLID
- [ ] Design patterns
- [ ] Dependency injection
- [ ] Testing
- [ ] Architecture
- [ ] Real-world projects

---

# 🧭 How to Use This Repository

### Step 1 — Learn

Understand the concept before memorizing syntax.

### Step 2 — Type

Write the code yourself.

### Step 3 — Break it

Change the code and intentionally create errors.

### Step 4 — Fix it

Understand *why* the error happened.

### Step 5 — Experiment

Create your own examples.

### Step 6 — Build

Use the concept inside a small project.

### Step 7 — Connect

Ask how the same concept appears in real Python libraries.

---

# ⭐ Core Philosophy

```text
                         PYTHON
                            │
                 ┌──────────┴──────────┐
                 │                     │
             Fundamentals           OOP
                                       │
                         ┌─────────────┼─────────────┐
                         │             │             │
                  Encapsulation   Inheritance   Polymorphism
                         │             │             │
                         └─────────────┼─────────────┘
                                       │
                                  Abstraction
                                       │
                                Advanced OOP
                                       │
                              Software Design
                                       │
                              Real Applications
                                       │
                                    AI / ML
```

---

## 🏁 Final Goal

By the end of this section, you should be able to open an unfamiliar Python project and ask:

```text
1. What are the objects?
2. What data does each object own?
3. What behavior does each object provide?
4. Which classes inherit from which?
5. Where is polymorphism being used?
6. Where is data encapsulated?
7. Where are abstractions/interfaces defined?
8. Should this relationship use inheritance or composition?
9. Is the design loosely coupled?
10. Is the code maintainable and testable?
```

If you can answer those questions, you are no longer just learning **Python class syntax**.

You are learning **object-oriented software design**.

---

<div align="center">

### 🐍 Keep learning. Keep building. Keep breaking things.

**Python Scratch → Advanced → AI/ML**

</div>
