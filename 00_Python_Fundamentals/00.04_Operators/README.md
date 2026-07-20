# 00.04 Operators

> **"Data is meaningless unless we can perform operations on it."**

---

# Introduction

In the previous chapter, we learned about **data types** and how Python stores different kinds of values such as integers, floating-point numbers, strings, lists, dictionaries, and Boolean values.

However, simply storing data is not enough.

Imagine a calculator that can only display numbers but cannot add, subtract, multiply, or divide them.

It would not be very useful.

Programming works the same way.

After storing data inside variables, we need a way to **perform operations** on that data.

These operations include:

- Adding numbers
- Comparing values
- Checking conditions
- Assigning values
- Combining logical expressions
- Manipulating binary data

Python provides **operators** to perform these tasks.

Operators are one of the most fundamental concepts in programming because every program—from a simple calculator to a complex artificial intelligence system—uses operators to process data.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what operators are.
- Identify different categories of operators.
- Perform arithmetic operations.
- Assign values using assignment operators.
- Compare values using comparison operators.
- Write logical expressions.
- Understand identity and membership operators.
- Perform basic bitwise operations.
- Understand operator precedence.
- Avoid common beginner mistakes.

---

# Prerequisites

Before studying operators, you should understand:

- Variables
- Data Types
- Basic Python syntax

If you have completed the previous chapters, you are ready for this topic.

---

# Why Do Operators Exist?

Imagine you have two numbers.

```
25

10
```

Simply storing these numbers is not enough.

You may want to:

- Add them
- Subtract them
- Multiply them
- Divide them
- Compare them

Without operators, Python would not know what action you want to perform.

Operators tell Python exactly **how values should be processed**.

---

# Real-World Analogy

Think of a calculator.

```
        +------------+
        |   10       |
        |   20       |
        |------------|
        |  +  -  × ÷ |
        +------------+
```

The numbers are called **operands**.

The buttons (`+`, `-`, `×`, `÷`) are operators.

Pressing different buttons performs different operations on the same numbers.

Programming follows the same principle.

---

# What is an Operator?

An **operator** is a special symbol or keyword that tells Python to perform a specific operation on one or more values.

Example:

```python
10 + 5
```

Here,

```
10     +
│      │
│      └── Operator
│
└──────── Operand
```

Result:

```
15
```

---

# What is an Operand?

The values on which operators work are called **operands**.

Example:

```python
50 - 20
```

```
50       20
│         │
└──Operands──┘

      -

   Operator
```

The operator performs an action using the operands.

---

# Expression

When operators and operands are combined, they form an **expression**.

Example:

```python
price * quantity
```

Another example:

```python
age >= 18
```

Expressions always produce a result.

Examples:

```python
10 + 5
```

Result:

```
15
```

```python
20 > 10
```

Result:

```
True
```

---

# Categories of Operators

Python provides several categories of operators.

| Category | Purpose |
|----------|---------|
| Arithmetic | Mathematical calculations |
| Assignment | Assign values |
| Comparison | Compare values |
| Logical | Combine conditions |
| Identity | Compare object identity |
| Membership | Check membership |
| Bitwise | Operate on binary values |

Each category solves a different problem.

---

# Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `5 + 2` |
| `-` | Subtraction | `5 - 2` |
| `*` | Multiplication | `5 * 2` |
| `/` | Division | `5 / 2` |
| `//` | Floor Division | `5 // 2` |
| `%` | Modulus | `5 % 2` |
| `**` | Exponent | `5 ** 2` |

---

# Addition (`+`)

Adds two values.

```python
a = 10
b = 20

print(a + b)
```

Output:

```text
30
```

Addition also works with strings.

```python
first = "Hello"
second = " World"

print(first + second)
```

Output:

```text
Hello World
```

This process is called **concatenation**.

---

# Subtraction (`-`)

Subtracts one value from another.

```python
a = 25
b = 10

print(a - b)
```

Output:

```text
15
```

---

# Multiplication (`*`)

Multiplies values.

```python
length = 5
width = 4

area = length * width

print(area)
```

Output:

```text
20
```

Strings can also be multiplied.

```python
print("*" * 10)
```

Output:

```text
**********
```

---

# Division (`/`)

Performs floating-point division.

```python
print(10 / 2)
```

Output:

```text
5.0
```

Notice that the result is a float, even when the division is exact.

Another example:

```python
print(7 / 2)
```

Output:

```text
3.5
```

---

# Floor Division (`//`)

Returns only the whole-number part of the division.

```python
print(7 // 2)
```

Output:

```text
3
```

Python discards the decimal portion.

---

# Modulus (`%`)

Returns the remainder after division.

Example:

```python
print(10 % 3)
```

Output:

```text
1
```

Why?

```
10 ÷ 3

Quotient = 3

Remainder = 1
```

Modulus is useful for:

- Checking even or odd numbers
- Circular indexing
- Cyclic operations

Example:

```python
number = 8

print(number % 2 == 0)
```

Output:

```text
True
```

---

# Exponent (`**`)

Raises a number to a power.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because

```
2 × 2 × 2 = 8
```

Another example:

```python
print(10 ** 2)
```

Output:

```text
100
```

---

# Arithmetic Operators Summary

| Expression | Result |
|------------|--------|
| `10 + 5` | `15` |
| `10 - 5` | `5` |
| `10 * 5` | `50` |
| `10 / 5` | `2.0` |
| `10 // 3` | `3` |
| `10 % 3` | `1` |
| `2 ** 4` | `16` |

---

# Assignment Operators

Assignment operators store values inside variables.

The most common assignment operator is:

```python
=
```

Example:

```python
age = 20
```

Read this as:

> Assign the value `20` to the variable `age`.

Remember:

The assignment operator (`=`) is **not** the mathematical equals sign.

It tells Python to store a value.

---

# Compound Assignment Operators

Python provides shortcut assignment operators.

| Operator | Equivalent To |
|----------|---------------|
| `+=` | `x = x + value` |
| `-=` | `x = x - value` |
| `*=` | `x = x * value` |
| `/=` | `x = x / value` |
| `//=` | `x = x // value` |
| `%=` | `x = x % value` |
| `**=` | `x = x ** value` |

Example:

```python
score = 10

score += 5

print(score)
```

Output:

```text
15
```

This is equivalent to:

```python
score = score + 5
```

Compound assignment operators make code shorter and easier to read.

---

# Comparison Operators

Comparison operators compare two values and return a **Boolean** result (`True` or `False`).

These operators are frequently used in:

- Decision making
- Conditional statements
- Loops
- Searching algorithms
- Sorting algorithms

Whenever Python needs to answer a question such as:

- Is one value greater than another?
- Are two values equal?
- Is this number less than 100?

comparison operators are used.

---

## Comparison Operators Table

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |
| `>` | Greater than | `20 > 10` |
| `<` | Less than | `5 < 8` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `8 <= 10` |

Every comparison operator returns either:

```python
True
```

or

```python
False
```

---

# Equal To (`==`)

Checks whether two values are equal.

Example:

```python
a = 10
b = 10

print(a == b)
```

Output:

```text
True
```

Another example:

```python
print(5 == 8)
```

Output:

```text
False
```

### Common Beginner Mistake

Do **not** confuse:

```python
=
```

with

```python
==
```

- `=` assigns a value.
- `==` compares two values.

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

# Not Equal To (`!=`)

Checks whether two values are different.

Example:

```python
print(10 != 5)
```

Output:

```text
True
```

Example:

```python
print(20 != 20)
```

Output:

```text
False
```

---

# Greater Than (`>`)

Checks whether the left value is larger than the right value.

```python
print(15 > 10)
```

Output:

```text
True
```

---

# Less Than (`<`)

Checks whether the left value is smaller than the right value.

```python
print(5 < 20)
```

Output:

```text
True
```

---

# Greater Than or Equal To (`>=`)

Returns `True` if the left value is greater than or equal to the right value.

```python
print(18 >= 18)
```

Output:

```text
True
```

---

# Less Than or Equal To (`<=`)

Returns `True` if the left value is less than or equal to the right value.

```python
print(7 <= 10)
```

Output:

```text
True
```

---

# Comparison Operators Summary

| Expression | Result |
|------------|--------|
| `10 == 10` | `True` |
| `10 != 5` | `True` |
| `20 > 10` | `True` |
| `5 < 2` | `False` |
| `8 >= 8` | `True` |
| `4 <= 2` | `False` |

---

# Logical Operators

Logical operators combine multiple conditions.

Imagine a university admission system.

A student must satisfy two conditions:

- Age must be at least 18.
- Marks must be at least 60.

Python combines these conditions using logical operators.

There are three logical operators.

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the result |

---

# Logical AND (`and`)

Returns `True` only if **both conditions** are true.

Example:

```python
age = 20
marks = 85

print(age >= 18 and marks >= 60)
```

Output:

```text
True
```

If either condition becomes false,

the entire expression becomes false.

Example:

```python
age = 16
marks = 90

print(age >= 18 and marks >= 60)
```

Output:

```text
False
```

---

## AND Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# Logical OR (`or`)

Returns `True` if **at least one condition** is true.

Example:

```python
marks = 45
sports_quota = True

print(marks >= 60 or sports_quota)
```

Output:

```text
True
```

Only when **both conditions are false** does `or` return `False`.

---

## OR Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# Logical NOT (`not`)

`not` reverses a Boolean value.

Example:

```python
is_logged_in = True

print(not is_logged_in)
```

Output:

```text
False
```

Another example:

```python
print(not False)
```

Output:

```text
True
```

---

## NOT Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# Combining Logical Operators

Example:

```python
age = 22
marks = 75
citizen = True

eligible = (
    age >= 18
    and marks >= 60
    and citizen
)

print(eligible)
```

Output:

```text
True
```

Complex conditions become easy to express using logical operators.

---

# Identity Operators

Identity operators compare **whether two variables refer to the same object in memory**, not just whether their values are equal.

Python provides two identity operators.

| Operator | Meaning |
|----------|---------|
| `is` | Same object |
| `is not` | Different objects |

---

# The `is` Operator

Example:

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Both variables refer to the **same list object**.

Memory illustration:

```text
a ───────┐
         │
         ▼
     +-----------+
     | [1,2,3]   |
     +-----------+
         ▲
         │
b ───────┘
```

---

# The `is not` Operator

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)
```

Output:

```text
True
```

Although both lists contain the same values, they are **different objects**.

---

# Equality (`==`) vs Identity (`is`)

This is one of the most common interview questions.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
```

Comparison:

```python
print(a == b)
```

Output:

```text
True
```

Identity:

```python
print(a is b)
```

Output:

```text
False
```

Explanation:

- `==` compares **values**.
- `is` compares **object identity** (memory reference).

---

# Membership Operators

Membership operators check whether a value exists inside a collection.

They work with:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

Python provides two membership operators.

| Operator | Meaning |
|----------|---------|
| `in` | Value exists |
| `not in` | Value does not exist |

---

# The `in` Operator

Example with a list:

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

Example with a string:

```python
language = "Python"

print("Py" in language)
```

Output:

```text
True
```

---

# The `not in` Operator

Example:

```python
numbers = [10, 20, 30]

print(50 not in numbers)
```

Output:

```text
True
```

Example:

```python
name = "Alice"

print("Bob" not in name)
```

Output:

```text
True
```

---

# Practical Example

```python
username = "Alice"

allowed_users = [
    "Alice",
    "Bob",
    "Charlie"
]

if username in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")
```

Output:

```text
Access Granted
```

---

# Bitwise Operators

So far, we've worked with numbers as decimal (base-10) values. However, computers internally represent all data using **binary** (base-2), where each digit is either `0` or `1`.

Bitwise operators perform operations directly on these binary representations.

Although beginners don't use bitwise operators frequently, they are important in:

- Low-level programming
- Operating systems
- Embedded systems
- Networking
- Cryptography
- Performance optimizations
- Technical interviews

---

## Binary Representation

Let's take the decimal number `5`.

```text
Decimal : 5
Binary  : 00000101
```

And the decimal number `3`.

```text
Decimal : 3
Binary  : 00000011
```

Bitwise operators compare these binary digits one bit at a time.

---

# Bitwise Operators Table

| Operator | Meaning | Example |
|----------|---------|---------|
| `&` | Bitwise AND | `5 & 3` |
| `|` | Bitwise OR | `5 | 3` |
| `^` | Bitwise XOR | `5 ^ 3` |
| `~` | Bitwise NOT | `~5` |
| `<<` | Left Shift | `5 << 1` |
| `>>` | Right Shift | `5 >> 1` |

---

# Bitwise AND (`&`)

Returns `1` only if both corresponding bits are `1`.

Example:

```python
print(5 & 3)
```

Binary calculation:

```text
  0101
& 0011
------
  0001
```

Output:

```text
1
```

---

# Bitwise OR (`|`)

Returns `1` if at least one bit is `1`.

```python
print(5 | 3)
```

Binary calculation:

```text
  0101
| 0011
------
  0111
```

Output:

```text
7
```

---

# Bitwise XOR (`^`)

Returns `1` only when the bits are different.

```python
print(5 ^ 3)
```

Binary calculation:

```text
  0101
^ 0011
------
  0110
```

Output:

```text
6
```

---

# Bitwise NOT (`~`)

Flips every bit.

```python
print(~5)
```

Output:

```text
-6
```

> **Note:** Python represents negative integers using an infinite two's complement representation. We'll study this in more detail when we cover bit manipulation algorithms.

---

# Left Shift (`<<`)

Moves all bits to the left.

```python
print(5 << 1)
```

Binary:

```text
00000101

↓

00001010
```

Output:

```text
10
```

Each left shift by one position is equivalent to multiplying by 2.

---

# Right Shift (`>>`)

Moves all bits to the right.

```python
print(8 >> 1)
```

Binary:

```text
00001000

↓

00000100
```

Output:

```text
4
```

Each right shift by one position is roughly equivalent to integer division by 2.

---

# Operator Precedence

When an expression contains multiple operators, Python follows a predefined order of evaluation known as **operator precedence**.

Consider this expression:

```python
print(2 + 3 * 4)
```

Output:

```text
14
```

Python first evaluates:

```text
3 * 4 = 12
```

Then:

```text
2 + 12 = 14
```

If you want addition to happen first, use parentheses.

```python
print((2 + 3) * 4)
```

Output:

```text
20
```

---

## Common Operator Precedence (Highest to Lowest)

| Priority | Operators |
|----------|-----------|
| 1 | `()` |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `|` |
| 10 | Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) |
| 11 | `not` |
| 12 | `and` |
| 13 | `or` |

> **Tip:** When in doubt, use parentheses to make your code clearer.

---

# Short-Circuit Evaluation

Python optimizes logical expressions using **short-circuit evaluation**.

This means Python stops evaluating as soon as it knows the final result.

### Example 1: `and`

```python
False and print("Hello")
```

Output:

```text
False
```

`print("Hello")` is never executed because the first operand is already `False`.

---

### Example 2: `or`

```python
True or print("Hello")
```

Output:

```text
True
```

Again, `print("Hello")` is never executed because the first operand is already `True`.

Short-circuit evaluation improves performance and can prevent unnecessary function calls.

---

# Common Beginner Mistakes

### 1. Confusing `=` and `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

### 2. Using `is` Instead of `==`

Incorrect:

```python
name1 = "Alice"
name2 = "Alice"

print(name1 is name2)
```

Use:

```python
print(name1 == name2)
```

Use `==` when comparing values.

---

### 3. Forgetting Operator Precedence

```python
result = 2 + 3 * 4
```

Many beginners expect:

```text
20
```

But Python returns:

```text
14
```

Use parentheses when needed.

---

### 4. Dividing by Zero

```python
print(10 / 0)
```

This raises a `ZeroDivisionError`.

Always ensure the divisor is not zero.

---

# Best Practices

- Use meaningful variable names.
- Use parentheses to improve readability.
- Prefer `==` for value comparisons.
- Use `is` only when checking object identity (for example, `value is None`).
- Keep logical expressions simple and readable.
- Avoid deeply nested conditions.

---

# Real-World Applications

Operators are used everywhere in programming.

Examples include:

- Calculating totals in shopping carts
- Comparing passwords
- Validating user input
- Finding maximum or minimum values
- Filtering search results
- Performing financial calculations
- Building game logic
- Processing sensor data
- Implementing algorithms

---

# Interview Tips

Here are some common interview questions related to operators:

1. What is the difference between `=` and `==`?
2. Explain `==` versus `is`.
3. What is operator precedence?
4. What is short-circuit evaluation?
5. What is the difference between `/` and `//`?
6. What does the modulus operator (`%`) do?
7. When would you use bitwise operators?
8. What is the difference between `and` and `&`?

---

# Frequently Asked Questions

### Why does `10 / 2` return `5.0` instead of `5`?

The `/` operator always performs floating-point division.

Use `//` if you need integer (floor) division.

---

### Why does `5 // 2` return `2`?

Floor division discards the fractional part of the result.

---

### When should I use `is`?

Use `is` when checking object identity, such as:

```python
if value is None:
    ...
```

Use `==` for comparing values.

---

# Chapter Summary

In this chapter, you learned:

- What operators are
- Operands and expressions
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators
- Operator precedence
- Short-circuit evaluation
- Common mistakes
- Best practices

Operators are one of the most fundamental building blocks of Python. Every algorithm, from searching and sorting to dynamic programming and graph traversal, relies on operators to manipulate and compare data.

---

# Practice Questions

## Easy

1. Add two numbers and display the result.
2. Find the remainder when 25 is divided by 4.
3. Check whether a number is even.
4. Compare two numbers using `>`.
5. Use `and` to combine two conditions.

---

## Medium

1. Write a program to determine if a student passes based on marks and attendance.
2. Check whether a character exists in a string.
3. Use compound assignment operators to update a score.
4. Compare two lists using both `==` and `is`.

---

## Hard

1. Implement a simple calculator using arithmetic operators.
2. Create a login validation program using logical operators.
3. Use bitwise operators to demonstrate setting and clearing bits.
4. Evaluate complex expressions and explain the order of execution.

---

# Further Reading

- Python Official Documentation – Operators
- Python Language Reference – Expressions
- PEP 8 Style Guide
- Upcoming Chapter: Conditional Statements (`if`, `elif`, `else`)

---

# Key Takeaways

- Operators perform actions on values.
- Operands are the values that operators act upon.
- Expressions combine operators and operands to produce a result.
- Comparison operators always return `True` or `False`.
- `==` compares values, while `is` compares object identity.
- `and`, `or`, and `not` are essential for building conditional logic.
- Bitwise operators work directly with binary data.
- Parentheses improve readability and help control operator precedence.
- Understanding operators is essential before learning conditional statements, loops, functions, and data structures.