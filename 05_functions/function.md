````markdown
# Python Functions — Short Overview

## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

---

## 2. Basic Syntax

```python
def function_name(parameters):
    # function body
    return result
````

Example:

```python
def square(number):
    return number * number

print(square(5))
```

---

## 3. Parameters and Arguments

**Parameter:** Variable defined in the function.

```python
def greet(name):
    print(name)
```

**Argument:** Actual value passed to the function.

```python
greet("Vivek")
```

---

## 4. Return Value

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

---

## 5. Default Parameter

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Vivek")
```

---

## 6. Multiple Return Values

Python can return multiple values.

```python
def calculate(a, b):
    return a + b, a - b

sum_value, difference = calculate(10, 5)
```

---

## 7. *args

Accepts a variable number of positional arguments.

```python
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))
```

---

## 8. **kwargs

Accepts a variable number of keyword arguments.

```python
def show_info(**data):
    for key, value in data.items():
        print(key, ":", value)

show_info(name="Vivek", age=22)
```

---

## 9. Lambda Function

A small anonymous function.

```python
square = lambda x: x * x

print(square(5))
```

---

## 10. Recursive Function

A function that calls itself.

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

---

## 11. Generator Function

A function that uses `yield` to produce values one at a time.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

---

## Java → Python

Java:

```java
int add(int a, int b) {
    return a + b;
}
```

Python:

```python
def add(a, b):
    return a + b
```

### Important Differences

* Python uses `def`.
* Return type is not required.
* Parameter types are not required.
* Indentation defines the function body.
* Python functions are objects.

---

## Function Topics
```text
Functions
├── Parameters & Arguments
├── return
├── Default Arguments
├── Keyword Arguments
├── *args
├── **kwargs
├── Lambda
├── Scope
├── Recursion
├── map()
├── filter()
├── zip()
├── enumerate()
└── Generators