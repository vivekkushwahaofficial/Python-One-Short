# Python Scope — Short Overview

## 1. What is Scope?

Scope defines **where a variable can be accessed** in a Python program.

---

## 2. Local Scope

A variable created inside a function belongs to the local scope.

```python
def greet():
    name = "Vivek"
    print(name)

greet()
```

`name` can be accessed inside `greet()`.

---

## 3. Global Scope

A variable created outside functions belongs to the global scope.

```python
name = "Vivek"

def greet():
    print(name)

greet()
```

The function can read the global variable.

---

## 4. Local vs Global

```python
name = "Global"

def test():
    name = "Local"
    print(name)

test()
print(name)
```

Output:

```text
Local
Global
```

The local variable does not change the global variable.

---

## 5. `global` Keyword

Use `global` when you want to modify a global variable inside a function.

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

Output:

```text
1
```

---

## 6. `nonlocal` Keyword

`nonlocal` is used inside a nested function to modify a variable from the enclosing function.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print(count)

outer()
```

Output:

```text
1
```

---

## 7. LEGB Rule

Python searches for variables in this order:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Example:

```python
def outer():
    x = "Enclosing"

    def inner():
        print(x)

    inner()

outer()
```

Python finds `x` in the **Enclosing** scope.

---

# Quick Reference

```text
Local     → inside current function
Enclosing → outer function
Global    → outside all functions
Built-in  → Python's built-in names

global    → modify global variable
nonlocal  → modify enclosing variable
LEGB      → Local → Enclosing → Global → Built-in
```