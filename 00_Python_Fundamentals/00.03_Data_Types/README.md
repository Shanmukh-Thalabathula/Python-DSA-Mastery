# 00.03 Data Types

> **"Variables tell us where data is stored. Data types tell us what kind of data is stored."**

---

# Introduction

In the previous lesson, we learned about **variables** and how they allow us to store values in memory.

Consider the following example:

```python
name = "Alice"
age = 20
price = 99.99
```

Although all three values are stored inside variables, they are not the same kind of information.

- `"Alice"` is text.
- `20` is a whole number.
- `99.99` is a decimal number.

Python must understand the difference between these values because each one behaves differently.

For example:

```python
print(age + 5)
```

Output:

```
25
```

But:

```python
print(name + " Smith")
```

Output:

```
Alice Smith
```

Python knows how to add numbers together and how to join text together because it knows the **data type** of each value.

Understanding data types is one of the most important concepts in programming because every program stores, processes, and manipulates data.

Without data types, a computer would not know how to interpret the information stored in memory.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Explain what a data type is.
- Understand why data types are necessary.
- Identify Python's built-in data types.
- Check the type of any object using `type()`.
- Understand how Python stores different kinds of values.
- Distinguish between mutable and immutable data types (overview).
- Select the appropriate data type for different situations.

---

# Prerequisites

Before learning data types, you should already understand:

- Variables
- Assignment operator (`=`)
- Basic Python syntax
- Running Python programs

If you have completed the previous lesson (**00.02 Variables**), you are ready for this topic.

---

# What is a Data Type?

A **data type** defines the kind of value being stored and determines:

- How the value is represented in memory.
- What operations can be performed on it.
- How Python interprets the value.
- How much memory it may require internally.

Simply put,

> A data type tells Python **what a value is**.

For example,

```python
age = 25
```

Python recognizes:

- `25` is an integer.
- Integers support mathematical operations such as addition, subtraction, multiplication, and division.

Another example:

```python
name = "Alice"
```

Python recognizes:

- `"Alice"` is a string.
- Strings support operations such as concatenation, slicing, and searching.

Each data type has its own behavior.

---

# Why Do Data Types Exist?

Imagine a supermarket.

Different products are stored in different sections.

```
Fruits
Vegetables
Frozen Foods
Dairy Products
Electronics
```

Everything is organized because each category requires different handling.

Programming works the same way.

A computer stores many kinds of information:

- Numbers
- Text
- Images
- Audio
- Videos
- Dates
- Files
- True/False values

Each requires different processing.

For example,

Adding two numbers:

```python
10 + 20
```

Result:

```
30
```

Joining two strings:

```python
"Hello" + " World"
```

Result:

```
Hello World
```

Although both use the `+` operator, Python performs completely different operations depending on the data type.

This is why data types are essential.

---

# Real-World Analogy

Imagine your kitchen.

You have several containers.

```
Rice Container

Sugar Jar

Water Bottle

Oil Bottle

Salt Box
```

Each container is designed for a specific purpose.

You wouldn't store water inside the sugar jar.

Similarly, Python stores different kinds of information using different data types.

For example:

```
Age
↓

Integer

Name
↓

String

Salary
↓

Float

Is Student
↓

Boolean
```

Choosing the correct data type makes programs easier to understand and more efficient.

---

# Variables vs Data Types

Beginners often think variables have data types.

Technically, this is not true.

Variables are simply names that refer to objects.

The **object** has the data type.

Example:

```python
x = 10
```

Here,

```
Variable
↓

x

↓

Integer Object

↓

10
```

Later,

```python
x = "Python"
```

Now,

```
Variable

↓

x

↓

String Object

↓

"Python"
```

The variable remains the same.

Only the object it references changes.

This is possible because Python is a **dynamically typed language**.

---

# Dynamic Typing

Python automatically determines the data type of a value.

Unlike languages such as C or Java, we do not need to declare the type explicitly.

Example:

```python
score = 100
```

Python understands that `100` is an integer.

Later,

```python
score = 99.5
```

Now `score` refers to a floating-point number.

Later again,

```python
score = "Excellent"
```

Now it refers to a string.

The variable name stays the same, but the object it points to changes.

This flexibility makes Python easier to learn and write.

---

# Memory Representation

Consider the following code:

```python
name = "Alice"
```

A simplified memory representation is:

```
+------------------+
| Variable: name   |
+------------------+
          |
          |
          ▼
+------------------+
| String Object    |
| "Alice"          |
+------------------+
```

Another example:

```python
age = 25
```

```
+------------------+
| Variable: age    |
+------------------+
          |
          ▼
+------------------+
| Integer Object   |
| 25               |
+------------------+
```

Variables store references.

Objects store:

- Value
- Type
- Internal metadata

---

# Python Built-in Data Types

Python provides several built-in data types.

These can be grouped into categories.

| Category | Data Types |
|----------|------------|
| Numeric | int, float, complex |
| Boolean | bool |
| Text | str |
| Sequence | list, tuple, range |
| Mapping | dict |
| Set | set, frozenset |
| Binary | bytes, bytearray, memoryview |
| Special | NoneType |

Each category serves a different purpose.

Throughout this chapter, we will study each one in detail with examples, diagrams, and practical exercises.

---

# Data Type Hierarchy (Overview)

```
Python Data Types

│
├── Numeric
│   ├── int
│   ├── float
│   └── complex
│
├── Boolean
│   └── bool
│
├── Text
│   └── str
│
├── Sequence
│   ├── list
│   ├── tuple
│   └── range
│
├── Mapping
│   └── dict
│
├── Set
│   ├── set
│   └── frozenset
│
├── Binary
│   ├── bytes
│   ├── bytearray
│   └── memoryview
│
└── Special
    └── NoneType
```
---

# Numeric Data Types

Numbers are one of the most commonly used types of data in programming.

Python provides three built-in numeric data types:

```
int
float
complex
```

Each type is designed to represent a different kind of numerical value.

---

# Integer (`int`)

An **integer** is a whole number without a decimal point.

Examples:

```python
age = 25
temperature = -10
population = 1400000000
```

Integers can be:

- Positive
- Negative
- Zero

Examples:

```python
100
0
-250
999999999999999999999
```

Unlike some programming languages, Python integers can grow to very large sizes (limited mainly by available memory).

### Memory Representation

```text
age = 25

+------------------+
| Variable: age    |
+------------------+
          |
          ▼
+------------------+
| int              |
| 25               |
+------------------+
```

### Common Operations

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

# Floating-Point Number (`float`)

A **float** represents numbers that contain a decimal point.

Examples:

```python
price = 99.99
height = 5.8
temperature = -12.5
```

Examples of valid floats:

```python
10.5
0.75
-4.25
3.14159
```

### Why Are Floats Needed?

Many real-world values are not whole numbers.

Examples:

- Weight
- Height
- Price
- Distance
- Temperature

These require decimal values.

### Memory Representation

```text
price = 99.99

+------------------+
| Variable: price  |
+------------------+
          |
          ▼
+------------------+
| float            |
| 99.99            |
+------------------+
```

### Floating-Point Precision

Computers cannot represent every decimal number perfectly.

Example:

```python
print(0.1 + 0.2)
```

Output:

```text
0.30000000000000004
```

This surprises many beginners.

It happens because floating-point numbers are stored internally in binary format.

This is normal behavior and not a Python bug.

---

# Complex Number (`complex`)

Python also supports **complex numbers**, which are commonly used in mathematics, engineering, and scientific computing.

A complex number has two parts:

- Real part
- Imaginary part

Example:

```python
z = 3 + 4j
```

Here:

```
Real Part      → 3
Imaginary Part → 4j
```

Examples:

```python
2 + 5j
-1 + 7j
4j
```

Accessing the parts:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

Output:

```text
3.0
4.0
```

Although complex numbers are not commonly used in beginner programs, Python provides full support for them.

---

# Boolean (`bool`)

A Boolean represents one of only two possible values:

```python
True
False
```

Booleans are extremely important because they control decision-making in programs.

Example:

```python
is_logged_in = True
```

Another example:

```python
is_raining = False
```

### Boolean in Decision Making

```python
is_logged_in = True

if is_logged_in:
    print("Welcome!")
```

Output:

```text
Welcome!
```

Without Boolean values, programs would not be able to make decisions.

---

# NoneType

Sometimes a variable intentionally contains **no value**.

Python represents this using:

```python
None
```

Example:

```python
result = None
```

This means:

> "No value has been assigned yet."

Later:

```python
result = 95
```

Now the variable refers to an integer instead of `None`.

### Common Uses

- Placeholder values
- Function return values
- Missing information
- Initialization

Example:

```python
user = None
```

Later:

```python
user = "Alice"
```

---

# Checking a Data Type

Python provides the built-in `type()` function.

Syntax:

```python
type(object)
```

Example:

```python
age = 25

print(type(age))
```

Output:

```text
<class 'int'>
```

More examples:

```python
print(type(10))
print(type(3.14))
print(type(True))
print(type("Python"))
print(type(None))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
<class 'NoneType'>
```

---

# Using `isinstance()`

Although `type()` is useful, Python programmers often prefer `isinstance()`.

Syntax:

```python
isinstance(object, type)
```

Example:

```python
age = 20

print(isinstance(age, int))
```

Output:

```text
True
```

Another example:

```python
price = 19.99

print(isinstance(price, float))
```

Output:

```text
True
```

Example with strings:

```python
name = "Alice"

print(isinstance(name, str))
```

Output:

```text
True
```

`isinstance()` is generally preferred because it also works correctly with inheritance, which you'll learn later in Object-Oriented Programming.

---

# Summary of Primitive Data Types

| Data Type | Example | Description |
|-----------|---------|-------------|
| `int` | `25` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `complex` | `2 + 3j` | Complex numbers |
| `bool` | `True` | Logical values |
| `NoneType` | `None` | Represents no value |

---

# Common Beginner Mistakes

## Mistake 1: Confusing Integers and Strings

```python
age = "25"
```

This is a string, not an integer.

Correct:

```python
age = 25
```

---

## Mistake 2: Comparing Floating-Point Numbers Directly

Avoid:

```python
0.1 + 0.2 == 0.3
```

Because floating-point arithmetic may introduce tiny precision errors.

---

## Mistake 3: Writing `true` Instead of `True`

Incorrect:

```python
is_valid = true
```

Correct:

```python
is_valid = True
```

Python is case-sensitive.

---

# Best Practices

- Use `int` for whole numbers.
- Use `float` for decimal values.
- Use `bool` for decision-making.
- Use `None` when a value is intentionally missing.
- Use `type()` and `isinstance()` while learning and debugging.
---

# Sequence Data Types

A **sequence** is a collection of values arranged in a specific order.

Think of a sequence as a row of numbered boxes.

```
+-----+-----+-----+-----+
|  A  |  B  |  C  |  D  |
+-----+-----+-----+-----+
   0     1     2     3
```

Each item has a position called an **index**.

Python provides several sequence data types:

- `str`
- `list`
- `tuple`
- `range`

Although they all store multiple values, each has different characteristics and use cases.

---

# String (`str`)

A **string** is a sequence of characters used to represent text.

Examples:

```python
name = "Alice"
city = "London"
language = "Python"
```

A string can contain:

- Letters
- Numbers
- Symbols
- Spaces
- Unicode characters

Example:

```python
message = "Hello, World!"
```

---

## Creating Strings

Strings can be created using either single quotes or double quotes.

```python
name = "Alice"
city = 'London'
```

Both are valid.

For multi-line strings, use triple quotes:

```python
paragraph = """
Python is easy to learn.
It is widely used.
"""
```

---

## String Indexing

Every character has an index.

```text
String: "Python"

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
```

Example:

```python
word = "Python"

print(word[0])
print(word[3])
```

Output:

```text
P
h
```

---

## String Slicing

You can extract a part of a string using slicing.

Syntax:

```python
string[start:end]
```

Example:

```python
language = "Python"

print(language[0:3])
```

Output:

```text
Pyt
```

Example:

```python
print(language[2:])
```

Output:

```text
thon
```

---

## Strings Are Immutable

One of the most important properties of strings is:

> **Strings are immutable.**

Immutable means:

> Once a string is created, its contents cannot be changed.

Example:

```python
name = "Alice"

name[0] = "M"
```

Output:

```text
TypeError
```

Instead, create a new string:

```python
name = "Alice"

name = "Malice"
```

---

# List (`list`)

A **list** is an ordered collection of items.

Unlike strings, a list can store different types of data together.

Example:

```python
student = ["Alice", 20, 92.5, True]
```

Lists are one of the most powerful and frequently used data types in Python.

---

## Creating Lists

```python
numbers = [10, 20, 30]

fruits = ["Apple", "Banana", "Orange"]

mixed = [10, "Python", True, 5.5]
```

---

## List Memory Representation

```text
numbers = [10, 20, 30]

+--------------------------+
| Variable: numbers        |
+--------------------------+
             |
             ▼
+-----+-----+-----+
| 10  | 20  | 30  |
+-----+-----+-----+
```

---

## Accessing List Elements

```python
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## Lists Are Mutable

Unlike strings,

Lists **can be modified**.

Example:

```python
numbers = [10, 20, 30]

numbers[1] = 100

print(numbers)
```

Output:

```text
[10, 100, 30]
```

This ability to modify data makes lists extremely useful.

---

## Common List Operations

Appending an item:

```python
numbers.append(40)
```

Removing an item:

```python
numbers.remove(20)
```

Sorting:

```python
numbers.sort()
```

Length:

```python
len(numbers)
```

Checking membership:

```python
20 in numbers
```

---

# Tuple (`tuple`)

A **tuple** is similar to a list, but it is immutable.

Example:

```python
coordinates = (10, 20)
```

Another example:

```python
student = ("Alice", 20, "Computer Science")
```

---

## Why Use Tuples?

Tuples are useful when data should never change.

Examples:

- GPS coordinates
- Days of the week
- RGB color values
- Database records

---

## Tuple Example

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday"
)
```

Accessing elements:

```python
print(days[1])
```

Output:

```text
Tuesday
```

---

## Tuples Are Immutable

Attempting to modify a tuple results in an error.

```python
days = ("Monday", "Tuesday")

days[0] = "Sunday"
```

Output:

```text
TypeError
```

---

# List vs Tuple

| Feature | List | Tuple |
|----------|------|-------|
| Ordered | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Allows Duplicates | ✅ | ✅ |
| Syntax | `[ ]` | `( )` |

---

# Range (`range`)

The `range` data type generates a sequence of numbers.

Example:

```python
range(5)
```

Represents:

```text
0
1
2
3
4
```

It is commonly used in loops.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

---

## Range with Start and Stop

```python
range(2, 7)
```

Produces:

```text
2
3
4
5
6
```

---

## Range with Step

```python
range(0, 10, 2)
```

Output:

```text
0
2
4
6
8
```

---

# Mutability vs Immutability

Understanding this concept is essential in Python.

## Mutable

A mutable object can be changed after it is created.

Examples:

- list
- dict
- set
- bytearray

Example:

```python
numbers = [1, 2, 3]

numbers.append(4)
```

The original list changes.

---

## Immutable

An immutable object cannot be changed after creation.

Examples:

- int
- float
- bool
- str
- tuple
- frozenset
- bytes

Example:

```python
name = "Alice"

name = name + " Smith"
```

A **new string object** is created.

The original string remains unchanged.

---

# Mutable vs Immutable Comparison

| Mutable | Immutable |
|----------|-----------|
| list | str |
| dict | tuple |
| set | int |
| bytearray | float |
| | bool |
| | bytes |
| | frozenset |

---

# Memory Illustration

Mutable object:

```text
numbers

↓

+----------------------+
| 10 | 20 | 30 | 40 |
+----------------------+

Append 50

↓

+--------------------------+
|10|20|30|40|50|
+--------------------------+
```

Immutable object:

```text
name

↓

"Alice"

Attempt to modify

↓

New Object Created

↓

"Alice Smith"
```

---

# Summary

In this section, you learned:

- What sequence data types are.
- How strings store text.
- How lists store ordered collections.
- Why tuples are immutable.
- How `range()` generates sequences.
- The difference between mutable and immutable objects.

Sequence data types are used extensively throughout Python programming and will become even more important when we begin studying data structures such as arrays, stacks, queues, linked lists, and trees.

---

# Mapping Data Type (`dict`)

A **dictionary** is a collection of **key-value pairs**.

Unlike lists or tuples, dictionaries store data using **keys** instead of numeric indexes.

Think of a dictionary like a real-world English dictionary.

```
Word        → Meaning

Apple       → A fruit

Python      → A programming language

Car         → A vehicle
```

Instead of searching by position, you search using the key.

---

## Creating a Dictionary

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science"
}
```

Here,

```
Key        Value

name  ---> Alice

age   ---> 20

course ---> Computer Science
```

---

## Accessing Dictionary Values

```python
student = {
    "name": "Alice",
    "age": 20
}

print(student["name"])
```

Output:

```text
Alice
```

Another example:

```python
print(student["age"])
```

Output:

```text
20
```

---

## Dictionary Memory Representation

```text
student

↓

+-------------------------------+
| "name"   → "Alice"            |
| "age"    → 20                 |
| "course" → "Computer Science" |
+-------------------------------+
```

---

## Dictionaries Are Mutable

You can add, remove, or modify entries.

Example:

```python
student["age"] = 21

student["city"] = "London"
```

Result:

```python
{
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "city": "London"
}
```

---

# Set (`set`)

A **set** is an unordered collection of **unique elements**.

Example:

```python
numbers = {1, 2, 3, 4}
```

Notice that sets use curly braces, just like dictionaries.

However,

```python
{1, 2, 3}
```

is a set,

while

```python
{"name": "Alice"}
```

is a dictionary.

---

## Duplicate Values

Sets automatically remove duplicates.

Example:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

---

## Why Use Sets?

Sets are useful when:

- Removing duplicates
- Membership testing
- Mathematical set operations

Example:

```python
fruits = {"Apple", "Banana", "Orange"}

print("Apple" in fruits)
```

Output:

```text
True
```

---

# Frozen Set (`frozenset`)

A **frozenset** is an immutable version of a set.

Example:

```python
numbers = frozenset([1, 2, 3])
```

Unlike a normal set,

```python
numbers.add(4)
```

will produce an error because frozensets cannot be modified.

---

# Binary Data Types

Python also includes binary data types.

These are mostly used for:

- Images
- Audio
- Video
- Network communication
- File processing

The three built-in binary types are:

```
bytes

bytearray

memoryview
```

---

## Bytes

A `bytes` object stores immutable binary data.

Example:

```python
data = b"Python"
```

Each character is stored as a numeric byte.

---

## Bytearray

A `bytearray` is similar to bytes but mutable.

Example:

```python
data = bytearray(b"Python")
```

Unlike `bytes`, the contents can be modified.

---

## Memoryview

A `memoryview` provides direct access to binary data without copying it.

Example:

```python
data = memoryview(bytes(5))
```

This is an advanced feature used for high-performance applications.

---

# Type Conversion

Sometimes we need to convert one data type into another.

Python provides built-in conversion functions.

---

## Convert String to Integer

```python
age = "25"

age = int(age)
```

Now,

```python
type(age)
```

returns

```text
<class 'int'>
```

---

## Convert Integer to Float

```python
number = 10

value = float(number)
```

Result:

```text
10.0
```

---

## Convert Float to Integer

```python
price = 99.95

whole = int(price)
```

Output:

```text
99
```

Notice that the decimal part is removed.

---

## Convert Number to String

```python
age = 20

text = str(age)
```

Now,

```python
type(text)
```

returns

```text
<class 'str'>
```

---

# Common Type Conversion Functions

| Function | Description |
|----------|-------------|
| `int()` | Convert to integer |
| `float()` | Convert to float |
| `str()` | Convert to string |
| `bool()` | Convert to Boolean |
| `list()` | Convert to list |
| `tuple()` | Convert to tuple |
| `set()` | Convert to set |
| `dict()` | Convert to dictionary (when applicable) |

---

# Complete Data Type Summary

| Category | Data Types |
|----------|------------|
| Numeric | int, float, complex |
| Boolean | bool |
| Text | str |
| Sequence | list, tuple, range |
| Mapping | dict |
| Set | set, frozenset |
| Binary | bytes, bytearray, memoryview |
| Special | NoneType |

---

# Choosing the Correct Data Type

| Situation | Recommended Type |
|-----------|------------------|
| Age | int |
| Price | float |
| Name | str |
| Student Record | dict |
| Shopping List | list |
| Coordinates | tuple |
| Unique IDs | set |
| Binary File | bytes |

Choosing the correct data type improves readability, efficiency, and maintainability.

---

# Common Beginner Mistakes

## 1. Mixing Strings and Numbers

Incorrect:

```python
age = "20"

print(age + 5)
```

This produces an error.

Correct:

```python
age = int(age)

print(age + 5)
```

---

## 2. Expecting Strings to Change

Incorrect:

```python
name = "Alice"

name[0] = "M"
```

Strings are immutable.

---

## 3. Forgetting That Sets Remove Duplicates

```python
numbers = {1, 1, 2, 2, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

---

## 4. Using Lists When Tuples Are Better

If the data never changes, use a tuple instead of a list.

Example:

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday"
)
```

---

# Best Practices

- Choose meaningful variable names.
- Store numbers as numeric types, not strings.
- Use dictionaries for structured data.
- Use lists when the collection changes.
- Use tuples for fixed data.
- Use sets to eliminate duplicates.
- Use `type()` and `isinstance()` while learning.

---

# Frequently Asked Questions

### Does every value in Python have a data type?

Yes.

Every object in Python has a data type.

---

### Can a variable change its type?

Yes.

```python
x = 10

x = "Python"
```

Python is dynamically typed.

---

### What is the difference between a list and a tuple?

Lists are mutable.

Tuples are immutable.

---

### Why are strings immutable?

Immutability makes strings safer, more efficient, and easier for Python to optimize.

---

### Which data type is used most in Data Structures and Algorithms?

The most frequently used data types are:

- int
- bool
- list
- tuple
- dict
- set

These will appear throughout this repository.

---

# Interview Tips

Many beginner interviews include questions such as:

- What is the difference between a list and a tuple?
- What is dynamic typing?
- Explain mutable and immutable objects.
- What is the difference between `==` and `is`? *(Covered later.)*
- How do dictionaries work?
- When should you use a set?

Make sure you can explain these concepts without memorizing definitions.

---

# Practice Questions

## Easy

1. Create variables of type `int`, `float`, `str`, and `bool`.
2. Print the type of each variable.
3. Convert a string `"100"` into an integer.
4. Convert the integer `25` into a string.

---

## Medium

1. Create a dictionary representing a student.
2. Create a list of five programming languages.
3. Remove duplicate values from a list using a set.
4. Demonstrate the difference between a mutable and immutable object.

---

## Hard

1. Explain the difference between `list`, `tuple`, and `set` with examples.
2. Write a program that accepts user input and converts it into different data types.
3. Create a dictionary of employees and display all keys and values.

---

# Summary

Congratulations!

In this chapter, you learned one of the most fundamental concepts in Python—**Data Types**.

You now understand:

- What data types are.
- Why they are necessary.
- Python's built-in data types.
- Numeric types (`int`, `float`, `complex`).
- Boolean (`bool`).
- `NoneType`.
- Strings.
- Lists.
- Tuples.
- Dictionaries.
- Sets and frozensets.
- Binary data types.
- Type conversion.
- Mutable vs. immutable objects.
- Best practices for choosing the right data type.

These concepts form the foundation of everything you will build in Python.

As you continue through this repository, you'll repeatedly use these data types while learning algorithms, data structures, and real-world programming techniques.

---

# Further Reading

- Official Python Documentation: Data Types
- Python Standard Library Documentation
- PEP 8 – Style Guide for Python Code
- Python Enhancement Proposals (PEPs)

---

## What's Next?

In the next chapter, **00.04 Operators**, you'll learn how Python performs calculations, comparisons, logical operations, bitwise operations, assignment operations, and more.

Understanding operators is essential because every algorithm relies on them to manipulate data and make decisions.