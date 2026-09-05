# Python Iterators — Short Notes

## 1. Iterable

An iterable is an object that can provide an iterator.

Examples:
- list
- tuple
- set
- dictionary
- string
- range
- file

Example:

my_list = [1, 2, 3]

I = iter(my_list)


## 2. iter()

`iter()` creates an iterator from an iterable.

Syntax:

iterator = iter(iterable)

Example:

my_list = [1, 2, 3]
I = iter(my_list)


## 3. next()

`next()` returns the next value from an iterator.

Example:

I = iter([1, 2, 3])

next(I)  # 1
next(I)  # 2
next(I)  # 3

When there are no more values, Python raises:

StopIteration


## 4. __next__()

`__next__()` is the method used by an iterator to get the next value.

Example:

I = iter([1, 2, 3])

I.__next__()  # 1
I.__next__()  # 2
I.__next__()  # 3

Usually, prefer:

next(I)

instead of:

I.__next__()


## 5. StopIteration

When an iterator has no more values, it raises `StopIteration`.

Example:

I = iter([1, 2])

next(I)  # 1
next(I)  # 2
next(I)  # StopIteration


## 6. File Objects Are Iterators

A file object is its own iterator.

Example:

f = open("chai.py")

iter(f) is f

Output:

True

Therefore, we can directly use a file in a `for` loop:

for line in open("chai.py"):
    print(line, end="")


## 7. List vs Iterator

A list is an iterable, but it is not its own iterator.

Example:

my_list = [1, 2, 3]

iter(my_list) is my_list

Output:

False

The process is:

list
  ↓
iter()
  ↓
list_iterator
  ↓
next()
  ↓
value


## 8. range() Is Iterable

Example:

R = range(5)

I = iter(R)

next(I)  # 0
next(I)  # 1
next(I)  # 2
next(I)  # 3
next(I)  # 4
next(I)  # StopIteration


## 9. Important Difference

Iterable:
An object that can provide an iterator.

Iterator:
An object that produces values one at a time using `next()`.


## 10. Easy Mental Model

ITERABLE
    ↓
iter()
    ↓
ITERATOR
    ↓
next()
    ↓
VALUE
    ↓
next()
    ↓
VALUE
    ↓
...
    ↓
StopIteration


## Interview Answer

Question:
What is an iterator in Python?

Answer:

"Yes Sir, an iterator is an object that produces values one at a time. We can obtain an iterator using the `iter()` function and retrieve values using `next()`. When there are no more values, the iterator raises `StopIteration`."


## Key Points to Remember

- `iter()` → creates an iterator
- `next()` → gets the next value
- `__next__()` → iterator's next-value method
- `StopIteration` → no more values
- List → iterable
- File → iterator
- range → iterable