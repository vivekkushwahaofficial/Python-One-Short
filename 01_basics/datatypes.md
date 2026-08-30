# Python Object Types / Data Types

## 1. Numeric Types

- `int` → whole numbers
  - `1234`
  - `0b111`

- `float` → decimal numbers
  - `3.1415`

- `complex` → complex numbers
  - `3 + 4j`

- `Decimal` → precise decimal arithmetic
- `Fraction` → rational numbers

---

## 2. String / Text Types

- `str` → text
  - `'spam'`
  - `"Bob's"`

- `bytes` → binary data
  - `b'a\x01c'`

> In modern Python, `str` is used for text and `bytes` for binary data.

---

## 3. List

A list is an ordered and mutable collection.

```python
[1, [2, 'three'], 4.5]
````

```python
list(range(10))
```

---

## 4. Tuple

A tuple is an ordered and immutable collection.

```python
(1, 'spam', 4, 'U')
```

```python
tuple('spam')
```

`namedtuple` provides tuple-like objects with named fields.

---

## 5. Dictionary

A dictionary stores data as **key-value pairs**.

```python
{'food': 'spam', 'taste': 'yum'}
```

```python
dict(hours=10)
```

---

## 6. Set

A set is an unordered collection of unique elements.

```python
set('abc')
```

```python
{'a', 'b', 'c'}
```

---

## 7. Boolean

Boolean represents logical values.

```python
True
False
```

---

## 8. None

`None` represents the absence of a value.

```python
result = None
```

---

## 9. File Objects

Files are handled using file objects.

```python
file = open('eggs.txt')
```

Binary mode:

```python
file = open(r'C:\ham.bin', 'wb')
```

> A file is not a built-in data type like `list` or `dict`; `open()` returns a file object.

---

# Important Python Concepts

Python also provides:

* Functions
* Modules
* Classes
* Iterators
* Generators
* Decorators
* Metaprogramming

These are **Python concepts/features**, not basic data types.

---

## Quick Classification

| Category          | Examples                                              |
| ----------------- | ----------------------------------------------------- |
| Numeric           | `int`, `float`, `complex`, `Decimal`, `Fraction`      |
| Text/Binary       | `str`, `bytes`                                        |
| Sequence          | `list`, `tuple`                                       |
| Mapping           | `dict`                                                |
| Set               | `set`                                                 |
| Boolean           | `bool`                                                |
| Null value        | `None`                                                |
| File handling     | File objects                                          |
| Advanced concepts | Functions, classes, iterators, generators, decorators |

---
## Remember

**Python has many built-in object types, and everything in Python is an object.**

