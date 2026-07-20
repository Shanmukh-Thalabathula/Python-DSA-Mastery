# 00.07 Loops

> **"Computers are excellent at performing repetitive tasks. Loops allow us to automate repetition instead of writing the same code over and over again."**

---

# Introduction

Imagine you want to print the message:

```text
Welcome to Python-DSA-Mastery
```

only once.

You can write:

```python
print("Welcome to Python-DSA-Mastery")
```

Now suppose you want to print it **10 times**.

One approach is:

```python
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
print("Welcome to Python-DSA-Mastery")
```

Although this works, it has several problems:

- The code is repetitive.
- It is difficult to maintain.
- It is easy to make mistakes.
- Updating the message requires changing it in many places.

Now imagine printing the message **10,000 times**.

Writing 10,000 `print()` statements is clearly impossible.

This is exactly why loops exist.

A **loop** allows a block of code to execute repeatedly until a specified condition changes or until all items in a collection have been processed.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why loops are needed.
- Differentiate between `while` and `for` loops.
- Use the `range()` function effectively.
- Control loop execution with `break`.
- Skip iterations using `continue`.
- Understand the purpose of `pass`.
- Write nested loops.
- Avoid infinite loops.
- Analyze the time complexity of loops.

---

# Prerequisites

Before starting this chapter, you should understand:

- Variables
- Data Types
- Operators
- User Input
- Conditional Statements

Loops often rely on variables, conditions, and user input to determine how many times they should repeat.

---

# Why Do Loops Exist?

Consider a classroom attendance system.

Without loops, a teacher would need to write code like this:

```text
Read Student 1
Read Student 2
Read Student 3
...
Read Student 100
```

With a loop:

```text
Repeat 100 times:

↓

Read Student
```

One small block of code can now perform the same task many times.

---

# Real-World Analogy

Imagine a washing machine.

It does not wash clothes only once.

Instead, it repeats several actions:

```text
Fill Water

↓

Wash

↓

Drain

↓

Rinse

↓

Spin

↓

Repeat if Required
```

The machine performs the same steps repeatedly until the washing cycle is complete.

A programming loop works in exactly the same way.

---

# What is a Loop?

A **loop** is a programming construct that repeatedly executes a block of code.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

we can write:

```python
for _ in range(5):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
Hello
Hello
```

The code is shorter, cleaner, and easier to maintain.

---

# Types of Loops in Python

Python provides two primary looping constructs:

1. `while` loop
2. `for` loop

Both repeat code, but they are used in different situations.

---

# When Should You Use Each Loop?

Use a **while loop** when:

- You do not know in advance how many times the loop should execute.
- The loop depends on a condition.

Examples:

- Password validation
- ATM transactions
- Game loops
- User menus

Use a **for loop** when:

- You know how many times the loop should run.
- You want to iterate over a sequence such as a list, string, tuple, or range.

Examples:

- Printing numbers from 1 to 100
- Processing a list of students
- Reading characters in a string

---

# The `while` Loop

The `while` loop repeatedly executes a block of code **as long as its condition remains `True`.**

Syntax:

```python
while condition:
    # Loop Body
```

Python performs the following steps:

1. Evaluate the condition.
2. If the condition is `True`, execute the loop body.
3. Return to Step 1.
4. Repeat until the condition becomes `False`.

---

# Flow of a While Loop

```text
             Start
               │
               ▼
      Evaluate Condition
               │
       ┌───────┴────────┐
       │                │
     True             False
       │                │
       ▼                ▼
 Execute Loop         Exit Loop
       │
       │
       └───────────────┐
                       │
                       ▼
             Evaluate Again
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# Internal Working

Initially:

```text
count = 1
```

Python checks:

```
count <= 5

↓

True
```

The loop executes:

```
Print 1

↓

count = 2
```

Python checks again:

```
2 <= 5

↓

True
```

This process continues until:

```
count = 6

↓

6 <= 5

↓

False
```

The loop stops.

---

# Memory Representation

Before the loop:

```text
+----------------------+
| count                |
+----------------------+
| 1                    |
| int                  |
+----------------------+
```

After each iteration:

```text
Iteration 1

count = 2
```

```text
Iteration 2

count = 3
```

```text
Iteration 3

count = 4
```

Eventually:

```text
count = 6
```

Condition:

```python
count <= 5
```

becomes:

```text
False
```

The loop exits.

---

# Dry Run

Program:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

### Iteration 1

```
count = 1

1 <= 3

↓

True
```

Output:

```text
1
```

Update:

```
count = 2
```

---

### Iteration 2

```
2 <= 3

↓

True
```

Output:

```text
2
```

Update:

```
count = 3
```

---

### Iteration 3

```
3 <= 3

↓

True
```

Output:

```text
3
```

Update:

```
count = 4
```

---

### Iteration 4

```
4 <= 3

↓

False
```

The loop terminates.

---

# Infinite Loops

Consider this code:

```python
count = 1

while count <= 5:
    print(count)
```

What went wrong?

The value of `count` never changes.

Therefore:

```text
count <= 5

↓

Always True
```

The loop never ends.

This is called an **infinite loop**.

Always ensure that something inside the loop eventually causes the condition to become `False`.

---

# Key Rule

A `while` loop needs three essential components:

1. **Initialization** – Create the loop variable.

```python
count = 1
```

2. **Condition** – Decide whether the loop should continue.

```python
count <= 5
```

3. **Update** – Change the loop variable.

```python
count += 1
```

If any of these components are missing or incorrect, the loop may produce incorrect results or run forever.

---

# The `for` Loop

The `while` loop is useful when you **do not know in advance** how many times a task should repeat.

However, many programming tasks involve processing every element in a collection or repeating a fixed number of times.

Examples include:

- Printing numbers from 1 to 100
- Displaying every student's name
- Processing every item in a shopping cart
- Reading every character of a string

For these situations, Python provides the **`for` loop**.

---

# What is a `for` Loop?

A `for` loop repeatedly executes a block of code by taking one item at a time from a sequence.

Think of a basket of fruits.

```
Basket

🍎 🍌 🍇 🍊 🥭
```

Instead of picking every fruit manually, imagine someone hands you one fruit at a time.

```
Apple

↓

Banana

↓

Grapes

↓

Orange

↓

Mango
```

The same idea applies to a `for` loop.

Python automatically retrieves one item after another until there are no items left.

---

# Syntax

```python
for variable in sequence:
    # Loop Body
```

The loop variable stores the current item during each iteration.

---

# Flow of a `for` Loop

```text
              Start
                 │
                 ▼
        Get Next Item
                 │
        ┌────────┴─────────┐
        │                  │
     Item Exists      No More Items
        │                  │
        ▼                  ▼
 Execute Loop         Exit Loop
        │
        └──────────────────┘
```

---

# First Example

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

Notice that the loop executes **five times**.

---

# Understanding `range()`

The `range()` function generates a sequence of numbers.

It does **not** immediately create a list in memory. Instead, it produces numbers one at a time as the loop requests them, making it memory-efficient.

Basic syntax:

```python
range(stop)
```

Example:

```python
range(5)
```

Produces:

```text
0
1
2
3
4
```

Notice that the **stop value is excluded**.

---

# Why Does `range(5)` Start at Zero?

Programming languages commonly use **zero-based indexing**.

This means counting usually starts from zero.

```
Position

0   1   2   3   4
```

Therefore:

```python
range(5)
```

produces:

```
0

↓

1

↓

2

↓

3

↓

4
```

Five numbers are generated:

```
0
1
2
3
4
```

---

# Different Forms of `range()`

Python supports three forms.

## 1. `range(stop)`

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

## 2. `range(start, stop)`

```python
for number in range(2, 7):
    print(number)
```

Output:

```text
2
3
4
5
6
```

The loop starts at `2` and stops **before** `7`.

---

## 3. `range(start, stop, step)`

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

The third argument specifies how much the value changes after each iteration.

---

# Negative Step

A negative step allows counting backwards.

```python
for number in range(10, 0, -1):
    print(number)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

# Dry Run

Program:

```python
for number in range(3):
    print(number)
```

### Iteration 1

```
number = 0
```

Output:

```text
0
```

---

### Iteration 2

```
number = 1
```

Output:

```text
1
```

---

### Iteration 3

```
number = 2
```

Output:

```text
2
```

---

No more numbers remain.

The loop ends.

---

# Memory Representation

Initially:

```text
range(3)

↓

0
1
2
```

During execution:

```text
Iteration 1

number = 0
```

```text
Iteration 2

number = 1
```

```text
Iteration 3

number = 2
```

The loop variable changes automatically.

You never update it manually.

---

# Iterating Over a String

Strings are sequences of characters.

Example:

```python
word = "Python"

for character in word:
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

Python retrieves one character at a time.

Visualization:

```text
Python

↓

P

↓

y

↓

t

↓

h

↓

o

↓

n
```

---

# Iterating Over a List

Lists are also sequences.

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Orange
```

---

# Iterating Over a Tuple

```python
numbers = (10, 20, 30)

for value in numbers:
    print(value)
```

Output:

```text
10
20
30
```

---

# Iterating Over a Dictionary

By default, a dictionary loop iterates over its keys.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

for key in student:
    print(key)
```

Output:

```text
name
age
course
```

To access both keys and values:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Alice
age 20
course Python
```

---

# Iterating Over a Set

Sets are unordered collections.

```python
colors = {"red", "green", "blue"}

for color in colors:
    print(color)
```

The order of the output is **not guaranteed** because sets are unordered.

---

# Comparing `while` and `for`

| Feature | `while` | `for` |
|---------|---------|--------|
| Controlled by | Condition | Sequence |
| Number of iterations | Usually unknown | Usually known |
| Manual update required | Yes | No |
| Risk of infinite loop | Higher | Lower |
| Best use | Menus, validation, game loops | Collections, ranges, fixed repetition |

---

# Best Practices

- Use `for` when iterating over a sequence.
- Use `while` when repetition depends on a condition.
- Choose meaningful loop variable names (`student`, `fruit`, `item`) instead of generic names like `x` whenever possible.
- Avoid modifying a collection while iterating over it unless you understand the consequences.
- Keep loop bodies focused on a single responsibility.

---

# Loop Control Statements

Sometimes, we need more control over how a loop behaves.

Instead of always executing every iteration from beginning to end, we may want to:

- Stop the loop immediately.
- Skip the current iteration.
- Leave a placeholder for future code.

Python provides three statements for this purpose:

- `break`
- `continue`
- `pass`

---

# The `break` Statement

The `break` statement immediately terminates the nearest enclosing loop.

Once `break` executes:

- The current loop stops.
- Control moves to the first statement after the loop.

---

## Syntax

```python
for item in sequence:
    if condition:
        break
```

---

## Example

```python
for number in range(1, 11):
    if number == 6:
        break

    print(number)
```

Output:

```text
1
2
3
4
5
```

### Dry Run

Iteration:

```
1 → Print

2 → Print

3 → Print

4 → Print

5 → Print

6 → break

↓

Loop Ends
```

---

# Real-World Analogy

Imagine searching for a book in a library.

```
Shelf 1

↓

Shelf 2

↓

Shelf 3

↓

Book Found

↓

Stop Searching
```

There is no reason to continue searching once the book has been found.

That is exactly how `break` works.

---

# The `continue` Statement

The `continue` statement skips the remainder of the current iteration and immediately starts the next iteration.

The loop itself does **not** stop.

---

## Example

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

Notice that `3` is skipped.

---

## Dry Run

```
1 → Print

2 → Print

3 → continue

↓

Skip Printing

↓

Next Iteration

4 → Print

5 → Print
```

---

# Real-World Analogy

Imagine taking attendance.

```
Student 1

↓

Present

↓

Student 2

↓

Absent

↓

Skip

↓

Student 3
```

The teacher does not stop taking attendance because one student is absent.

The teacher simply continues with the next student.

---

# The `pass` Statement

Sometimes Python expects a block of code, but we have not implemented it yet.

The `pass` statement acts as a placeholder.

It does nothing.

---

## Example

```python
for number in range(5):

    if number == 3:
        pass

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

The loop behaves as if `pass` were not there.

---

# Why Use `pass`?

During development, you may know that code belongs in a particular place but have not written it yet.

Example:

```python
if user_is_admin:
    pass
```

This allows the program to run without syntax errors while the implementation is incomplete.

---

# Nested Loops

A loop can contain another loop.

This is called a **nested loop**.

---

# Visualization

```
Outer Loop

↓

Iteration 1

↓

Inner Loop

↓

Iteration 1

Iteration 2

Iteration 3

↓

Outer Loop Iteration 2

↓

Inner Loop Again
```

Notice that the inner loop runs completely for **each** iteration of the outer loop.

---

# Example

```python
for row in range(3):

    for column in range(4):
        print("*", end=" ")

    print()
```

Output:

```text
* * * *
* * * *
* * * *
```

---

# Multiplication Table

```python
for row in range(1, 4):

    for column in range(1, 4):

        print(row * column, end="\t")

    print()
```

Output:

```text
1   2   3
2   4   6
3   6   9
```

---

# Execution Flow

```
Outer Loop

↓

Inner Loop

↓

Complete

↓

Outer Loop Next Iteration

↓

Inner Loop Again
```

The inner loop always finishes before the outer loop moves to its next iteration.

---

# Loop `else` Clause

Python has a feature that surprises many beginners.

A loop can have an `else` block.

The `else` block executes **only if the loop finishes normally**.

It does **not** execute if the loop exits using `break`.

---

## Example Without `break`

```python
for number in range(3):
    print(number)
else:
    print("Loop Completed")
```

Output:

```text
0
1
2
Loop Completed
```

---

## Example With `break`

```python
for number in range(5):

    if number == 2:
        break

    print(number)

else:
    print("Loop Completed")
```

Output:

```text
0
1
```

The `else` block is skipped because the loop ended with `break`.

---

# Common Beginner Mistakes

## 1. Forgetting to Update the Loop Variable

```python
count = 1

while count <= 5:
    print(count)
```

This creates an infinite loop because `count` never changes.

Correct:

```python
count += 1
```

---

## 2. Incorrect `range()` Stop Value

Many beginners expect:

```python
range(5)
```

to produce:

```
1 2 3 4 5
```

Actually, it produces:

```
0 1 2 3 4
```

Remember:

> The stop value is **excluded**.

---

## 3. Modifying a Collection While Iterating

Avoid changing a list while looping over it.

Incorrect:

```python
numbers = [1, 2, 3]

for number in numbers:
    numbers.remove(number)
```

This can skip elements and produce unexpected results.

---

## 4. Misusing `break`

Do not use `break` when you only want to skip one iteration.

Use `continue` instead.

---

## 5. Deeply Nested Loops

Too many nested loops reduce readability.

If possible:

- Extract helper functions.
- Simplify logic.
- Use appropriate data structures.

---

# Complexity Analysis

## `while` Loop

If a loop executes **n** times:

```python
while count < n:
    count += 1
```

Time Complexity:

```
O(n)
```

because one iteration is performed for each value.

Space Complexity:

```
O(1)
```

No additional memory proportional to `n` is allocated.

---

## `for` Loop

```python
for number in range(n):
    print(number)
```

Time Complexity:

```
O(n)
```

The loop body executes `n` times.

Space Complexity:

```
O(1)
```

---

## Nested Loops

```python
for i in range(n):

    for j in range(n):

        print(i, j)
```

The outer loop runs `n` times.

For each outer iteration, the inner loop also runs `n` times.

Total operations:

```
n × n = n²
```

Time Complexity:

```
O(n²)
```

Space Complexity:

```
O(1)
```

---

# Real-World Applications

Loops are used in almost every software application.

Examples include:

- Reading files line by line
- Processing database records
- Training machine learning models
- Rendering game frames
- Sending emails to multiple users
- Processing images pixel by pixel
- Network packet handling
- Data analysis
- Web scraping
- Sensor data collection in IoT devices

---

# Interview Tips

Frequently asked interview questions include:

1. What is the difference between `while` and `for`?
2. Explain the purpose of `break`, `continue`, and `pass`.
3. Why can `while` loops become infinite?
4. What does `range(5)` produce?
5. When should you use nested loops?
6. Explain the loop `else` clause.
7. What is the time complexity of nested loops?
8. How can you avoid infinite loops?

---

# Frequently Asked Questions

## Can a `for` loop become infinite?

Normally, no.

However, if you repeatedly generate new items or intentionally create an endless iterator, a `for` loop can continue indefinitely.

---

## Which loop is faster?

Neither.

Choose the loop that best matches the problem.

Readability and correctness are more important than tiny performance differences.

---

## Can I use `break` inside a `while` loop?

Yes.

`break` works with both `for` and `while` loops.

---

## Is `pass` required?

No.

It is only a placeholder.

---

# Chapter Summary

In this chapter, you learned:

- Why loops exist
- The `while` loop
- The `for` loop
- The `range()` function
- Iterating over sequences
- `break`
- `continue`
- `pass`
- Nested loops
- Loop `else`
- Time and space complexity
- Common mistakes
- Best practices

Loops are one of the fundamental building blocks of programming. They allow software to automate repetitive tasks, process collections efficiently, and implement many core algorithms. Mastering loops is essential before moving on to functions, recursion, and advanced data structures.

---

# Practice Questions

## Easy

1. Print numbers from 1 to 10 using a `while` loop.
2. Print numbers from 1 to 10 using a `for` loop.
3. Print all even numbers between 1 and 20.
4. Calculate the sum of the first 100 natural numbers.
5. Reverse count from 10 to 1.

---

## Medium

1. Print the multiplication table of a given number.
2. Count the number of digits in an integer.
3. Reverse an integer using a loop.
4. Calculate the factorial of a number.
5. Print Fibonacci numbers up to `n` terms.

---

## Hard

1. Print various star (`*`) patterns using nested loops.
2. Determine whether a number is prime.
3. Print all prime numbers within a given range.
4. Implement a menu-driven calculator using a `while` loop.
5. Generate Pascal's Triangle.

---

# Further Reading

- Python Official Documentation – `for` Statement
- Python Official Documentation – `while` Statement
- Python `range()` Function
- Next Chapter: Functions