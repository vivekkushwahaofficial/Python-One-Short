# Mutable vs Immutable

## Mutable

A **mutable object** can be changed after it is created.

### Examples

- `list`
- `dict`
- `set`
- `bytearray`

```python
my_list = [1, 2, 3]

my_list[0] = 10

print(my_list)  # [10, 2, 3]
````

The existing object is modified.

---

## Immutable

An **immutable object** cannot be changed after it is created.

### Examples

* `int`
* `float`
* `complex`
* `bool`
* `str`
* `tuple`
* `bytes`
* `frozenset`

```python
name = "Python"

# name[0] = "J"  # TypeError
```

If we assign a new value, the variable refers to another object.

```python
x = 10
x = 20
```

---

## Mutable vs Immutable

| Mutable     | Immutable   |
| ----------- | ----------- |
| `list`      | `int`       |
| `dict`      | `float`     |
| `set`       | `complex`   |
| `bytearray` | `bool`      |
|             | `str`       |
|             | `tuple`     |
|             | `bytes`     |
|             | `frozenset` |

---

## Important Example

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

`a` and `b` refer to the **same mutable list object**.

```python
a = 10
b = a

a = 20

print(a)  # 20
print(b)  # 10
```

Integers are **immutable**.

---

## Quick Revision

**Mutable → object can be changed**

**Immutable → object cannot be changed**

```text
Mutable   → list, dict, set
Immutable → int, float, str, tuple, bool
```

### Remember

> **Mutation changes the existing object.**
>
> **Reassignment changes what a variable refers to.**