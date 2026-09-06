# Python OOP — Short Overview

## What is OOP?

**OOP (Object-Oriented Programming)** is a programming style where we organize code around **objects**.

An object contains:

- **Data** → attributes
- **Behavior** → methods

Example:

```text
Car
 ├── Data
 │    ├── brand
 │    └── model
 │
 └── Behavior
      └── display_info()
```

---

## Why OOP?

Suppose we need to represent many cars:

```text
Car 1 → Toyota, Camry
Car 2 → Tesla, Model 3
Car 3 → BMW, X5
```

Instead of managing separate variables and functions, we can create **Car objects**.

```python
car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model 3")
```

Each object has its own data but uses the same class structure.

---

# Core OOP Concepts

## 1. Class

A **class** is a blueprint/template for creating objects.

```python
class Car:
    pass
```

Java:

```java
class Car {
}
```

---

## 2. Object

An **object** is an instance of a class.

```python
car1 = Car()
```

```text
Car       → Blueprint
car1      → Object
```

---

## 3. `self`

`self` refers to the **current object**.

```python
class Car:
    def show(self):
        print("This is a car")
```

Java does not explicitly write `self`.

Python explicitly uses `self`:

```python
def show(self):
    ...
```

---

## 4. `__init__`

`__init__` initializes an object's data when the object is created.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

```python
car1 = Car("Toyota", "Camry")
```

---

## 5. Encapsulation

Encapsulation means keeping data and behavior together and controlling access to data.

Python commonly uses:

```python
__brand
```

for **name-mangled** attributes.

> Python doesn't have Java-style truly private fields.

---

## 6. Inheritance

One class can inherit from another.

```python
class Car:
    pass

class ElectricCar(Car):
    pass
```

```text
Car
 ↓
ElectricCar
```

---

## 7. Polymorphism

Different objects can provide different implementations of the same method.

```python
class Car:
    def fuel_type(self):
        print("Petrol")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric")
```

---

## 8. Class Variables

A variable shared by all objects of a class.

```python
class Car:
    wheels = 4
```

Every `Car` object can access `wheels`.

---

## 9. Static Method

A method that doesn't need access to the object or class.

```python
class Car:
    @staticmethod
    def description():
        print("Cars are vehicles")
```

---

## 10. Property

Allows method-based logic to be accessed like an attribute.

```python
class Car:
    @property
    def model(self):
        return self._model
```

---

# Important Idea

Don't think:

> **Class = just syntax**

Think:

> **Class = blueprint → Object = actual instance → Attributes = data → Methods = behavior**