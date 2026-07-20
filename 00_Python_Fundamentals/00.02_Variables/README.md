# 00.02 Variables

> "Variables are the containers that allow a program to remember information."

---

# Introduction

Imagine you have a labeled box.

You write **Age** on the box and put the number **20** inside it.

Whenever you need the age, you simply look inside the **Age** box.

Variables work in exactly the same way.

A variable stores data so that it can be used later in a program.

Without variables, a program cannot remember names, numbers, user input, or calculations.

Variables are one of the most fundamental concepts in every programming language.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand what a variable is.
- Create variables in Python.
- Assign values to variables.
- Update variable values.
- Follow Python variable naming rules.
- Understand dynamic typing.
- Write readable variable names.

---

# Why Do We Need Variables?

Imagine building a calculator without variables.

```
print(10 + 20)
print(10 + 20)
print(10 + 20)
```

If the numbers change, every line must be edited.

Instead:

```python
a = 10
b = 20

print(a + b)
```

Now only one place needs updating.

Variables make programs:

- Easier to read
- Easier to maintain
- Easier to modify

---

# Real-World Analogy

Imagine a school.

Each student has a locker.

```
Locker A → Alice
Locker B → Bob
Locker C → Charlie
```

The locker label is like the **variable name**.

The item inside is the **value**.

```
student = "Alice"
```

```
Variable Name
     │
     ▼
 student
     │
     ▼
 "Alice"
```

---

# What is a Variable?

A variable is a named reference to an object in memory.

In simple words:

A variable gives a name to a value so we can use it later.

Example:

```python
name = "Alice"
```

Here:

- `name` is the variable.
- `"Alice"` is the value.

---

# Variable Assignment

The assignment operator is:

```python
=
```

Example:

```python
age = 20
```

Read it as:

> Assign the value `20` to the variable `age`.

It does **not** mean "equals" as in mathematics.

---

# Memory Representation

```text
age = 20

Memory

+---------+
|   20    |
+---------+
     ▲
     │
    age
```

Another example:

```python
city = "London"
```

```text
+-----------+
| "London"  |
+-----------+
      ▲
      │
     city
```

---

# Creating Variables

```python
name = "Alice"

age = 25

height = 5.6

is_student = True
```

Python automatically determines the data type.

This is called **dynamic typing**.

---

# Dynamic Typing

Unlike languages such as C or Java, Python does not require you to declare the data type.

```python
message = "Hello"

number = 100

price = 9.99
```

Python figures out the type automatically.

---

# Changing Variable Values

Variables can be updated.

```python
score = 10

print(score)

score = 20

print(score)
```

Output:

```
10
20
```

---

# Multiple Assignment

Python allows assigning multiple variables in one line.

```python
x, y, z = 1, 2, 3
```

---

# Assign One Value to Multiple Variables

```python
a = b = c = 100
```

Now all three variables refer to the same value.

---

# Variable Naming Rules

Allowed:

```python
student
student_name
student1
_student
```

Not Allowed:

```python
1student

student-name

student name

class
```

---

# Naming Conventions (PEP 8)

Good:

```python
student_name
total_marks
user_age
```

Avoid:

```python
x
abc
temp12345
```

Use meaningful names.

---

# Common Mistakes

❌ Using spaces

```python
student name = "John"
```

❌ Starting with numbers

```python
1name = "John"
```

❌ Using keywords

```python
class = "A"
```

---

# Best Practices

- Use descriptive names.
- Keep names lowercase.
- Use underscores between words.
- Avoid unnecessary abbreviations.
- Follow PEP 8.

---

# Summary

In this lesson, you learned:

- What variables are.
- Why variables exist.
- How Python stores values.
- Assignment.
- Dynamic typing.
- Naming rules.
- Best practices.

Variables are the foundation of every Python program.
