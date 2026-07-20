# 00.06 Conditional Statements

> **"Programs become intelligent when they can make decisions."**

---

# Introduction

So far in this course, every Python program we've written has executed **line by line** from top to bottom.

For example:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Output:

```text
Step 1
Step 2
Step 3
```

The execution order never changes.

No matter who runs the program or what input they provide, these three statements always execute in the same sequence.

This type of execution is called **Sequential Execution**.

However, real-world software rarely behaves this way.

Imagine logging into your email account.

If your password is correct, you are taken to your inbox.

If your password is incorrect, you receive an error message.

The program must decide which path to follow.

Similarly,

- ATM machines decide whether you have enough balance.
- Online stores decide whether a product is in stock.
- Games decide whether the player wins or loses.
- Hospitals decide whether a patient's condition is critical.
- Navigation apps decide which route is the fastest.

These decisions are possible because programming languages provide **Conditional Statements**.

Conditional statements allow a program to execute different blocks of code depending on whether a condition is **True** or **False**.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand decision making in programming.
- Write `if` statements.
- Write `if...else` statements.
- Write `if...elif...else` statements.
- Create nested `if` statements.
- Use conditional expressions (ternary operator).
- Understand truthy and falsy values.
- Write clean decision-making logic.
- Avoid common mistakes.

---

# Prerequisites

Before studying this chapter, you should understand:

- Variables
- Data Types
- Operators
- User Input

These concepts are necessary because conditions are created using variables, operators, and user input.

---

# Why Do Conditional Statements Exist?

Imagine a traffic signal.

```
          Traffic Light

         🔴  Stop

         🟡  Wait

         🟢  Go
```

The signal behaves differently depending on its current color.

If the light is green:

```
Go
```

If the light is red:

```
Stop
```

It does **not** perform every action at the same time.

Programming follows exactly the same principle.

A program often needs to choose one action from several possibilities.

Conditional statements make these choices possible.

---

# Real-World Analogy

Suppose you're entering a movie theater.

The staff member asks:

```
What is your age?
```

If your age is 18 or above:

```
Entry Allowed
```

Otherwise:

```
Entry Denied
```

Notice something important.

Only **one** decision is taken.

The staff member never says both:

```
Entry Allowed

AND

Entry Denied
```

Programming behaves the same way.

Only one path is executed.

---

# Sequential Execution vs Conditional Execution

Sequential Execution:

```text
Start

↓

Statement 1

↓

Statement 2

↓

Statement 3

↓

End
```

Conditional Execution:

```text
          Condition
              │
      ┌───────┴────────┐
      │                │
   True              False
      │                │
      ▼                ▼
Block A            Block B
      │                │
      └───────┬────────┘
              ▼
             End
```

---

# What is a Condition?

A **condition** is an expression that evaluates to either:

```python
True
```

or

```python
False
```

Examples:

```python
age >= 18
```

```python
marks > 40
```

```python
password == "python"
```

Each of these expressions produces a Boolean value.

Example:

```python
print(20 >= 18)
```

Output:

```text
True
```

Example:

```python
print(5 > 10)
```

Output:

```text
False
```

Conditional statements use these Boolean results to decide which block of code should execute.

---

# The `if` Statement

The simplest conditional statement is the `if` statement.

Syntax:

```python
if condition:
    # Code to execute if the condition is True
```

The word `if` tells Python:

> "Execute the following block only if the condition is True."

---

# Flow of an `if` Statement

```text
          Start
             │
             ▼
     Evaluate Condition
             │
      ┌──────┴──────┐
      │             │
    True          False
      │             │
      ▼             │
 Execute Block      │
      │             │
      └──────┬──────┘
             ▼
            End
```

---

# First `if` Statement

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```text
You are eligible to vote.
```

The condition:

```python
age >= 18
```

evaluates to:

```python
True
```

Therefore, Python executes the indented block.

---

# When the Condition is False

```python
age = 15

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```text
No Output
```

Nothing is printed because the condition is `False`.

Python simply skips the indented block and continues with the next statement.

---

# Understanding Indentation

Unlike many programming languages that use braces `{}` to define blocks of code, Python uses **indentation**.

Example:

```python
age = 20

if age >= 18:
    print("Eligible")
```

The `print()` statement is indented, so it belongs to the `if` block.

Incorrect:

```python
age = 20

if age >= 18:
print("Eligible")
```

This raises an `IndentationError` because Python expects an indented block after the `if` statement.

The standard indentation in Python is **4 spaces**.

---

# Dry Run

Program:

```python
age = 22

if age >= 18:
    print("Adult")
```

### Step 1

Variable:

```text
age = 22
```

---

### Step 2

Evaluate:

```python
22 >= 18
```

Result:

```text
True
```

---

### Step 3

Condition is True.

Execute:

```python
print("Adult")
```

Output:

```text
Adult
```

---

# Memory Representation

Before evaluation:

```text
+--------------------+
| age                |
+--------------------+
| 22                 |
| int                |
+--------------------+
```

Condition:

```python
age >= 18
```

Evaluation:

```text
22 >= 18

↓

True
```

Python then decides to execute the indented block.

---

# Important Rule

An `if` statement **does not** execute its block unless the condition evaluates to `True`.

If the condition is `False`, Python skips the block entirely.

This simple idea forms the foundation of decision-making in programming.

---

# The `if...else` Statement

The `if` statement executes a block of code only when the condition is `True`.

But what if we also want to perform another action when the condition is `False`?

That's where the `else` statement comes in.

Think of it like a fork in the road.

```
             Is it raining?
                    │
         ┌──────────┴──────────┐
         │                     │
       Yes                    No
         │                     │
         ▼                     ▼
  Take an Umbrella      Wear Sunglasses
```

Only one path is chosen.

The same idea applies to Python.

---

# Syntax

```python
if condition:
    # Executes if condition is True
else:
    # Executes if condition is False
```

Notice that:

- The `else` statement does **not** have a condition.
- It automatically executes when the `if` condition is `False`.

---

# Example: Voting Eligibility

```python
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

Output:

```text
You are not eligible to vote.
```

---

# Execution Flow

```text
          Start
             │
             ▼
     Evaluate Condition
             │
      ┌──────┴──────┐
      │             │
    True          False
      │             │
      ▼             ▼
 Execute IF     Execute ELSE
      │             │
      └──────┬──────┘
             ▼
            End
```

---

# Dry Run

Program:

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

### Step 1

Store:

```text
marks = 35
```

---

### Step 2

Evaluate:

```python
35 >= 40
```

Result:

```text
False
```

---

### Step 3

Skip the `if` block.

---

### Step 4

Execute the `else` block.

Output:

```text
Fail
```

---

# The `if...elif...else` Statement

Real-world decisions often involve more than two choices.

Imagine a grading system.

```
Marks ≥ 90

↓

Grade A

Marks ≥ 75

↓

Grade B

Marks ≥ 60

↓

Grade C

Otherwise

↓

Grade D
```

Using only `if...else` would become difficult to read.

Python solves this problem with the `elif` statement.

The word `elif` means:

> **Else If**

---

# Syntax

```python
if condition_1:
    # Block 1

elif condition_2:
    # Block 2

elif condition_3:
    # Block 3

else:
    # Default block
```

Python evaluates the conditions **from top to bottom**.

As soon as one condition is `True`, Python executes that block and skips the remaining conditions.

---

# Example: Student Grades

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade D")
```

Output:

```text
Grade B
```

---

# How Python Evaluates `elif`

Given:

```python
marks = 82
```

Python checks:

```
82 >= 90 ?

↓

False
```

Next:

```
82 >= 75 ?

↓

True
```

Python prints:

```text
Grade B
```

The remaining conditions are **not checked**.

---

# Flow of `if...elif...else`

```text
                 Condition 1
                     │
          ┌──────────┴──────────┐
          │                     │
       True                  False
          │                     │
          ▼                     ▼
      Block 1             Condition 2
                                │
                    ┌───────────┴───────────┐
                    │                       │
                 True                    False
                    │                       │
                    ▼                       ▼
                Block 2              Condition 3
                                          │
                                ┌─────────┴─────────┐
                                │                   │
                              True               False
                                │                   │
                                ▼                   ▼
                            Block 3          ELSE Block
```

---

# Order Matters

The order of conditions is extremely important.

Incorrect:

```python
marks = 95

if marks >= 60:
    print("Grade C")

elif marks >= 75:
    print("Grade B")

elif marks >= 90:
    print("Grade A")
```

Output:

```text
Grade C
```

This is incorrect because the first condition (`marks >= 60`) is already `True`.

Python never reaches the later conditions.

---

# Correct Order

Always check the most specific or highest condition first.

```python
if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade D")
```

This produces the expected result.

---

# Nested `if` Statements

An `if` statement can contain another `if` statement inside it.

This is called a **nested `if` statement**.

Think of it as making a decision inside another decision.

Example:

```
Are you logged in?

↓

Yes

↓

Are you an administrator?

↓

Yes

↓

Show Admin Panel
```

---

# Syntax

```python
if condition_1:

    if condition_2:
        # Nested block
```

Notice that the inner `if` is indented one level further.

---

# Example

```python
age = 22
has_license = True

if age >= 18:

    if has_license:
        print("You can drive.")
```

Output:

```text
You can drive.
```

---

# Execution Flow

```
Is age >= 18?

↓

Yes

↓

Is license available?

↓

Yes

↓

Allow Driving
```

If the first condition is `False`, Python never checks the nested condition.

---

# Dry Run

Variables:

```text
age = 17

license = True
```

Python evaluates:

```
17 >= 18

↓

False
```

The outer condition fails.

The nested `if` is skipped completely.

Output:

```text
No Output
```

---

# When Should You Use Nested `if`?

Nested `if` statements are useful when one condition depends on another.

Examples include:

- User authentication
- Banking transactions
- ATM withdrawal
- Online shopping checkout
- Multi-level permissions
- Game levels
- Student admission systems

However, avoid excessive nesting because it can make code harder to read.

In many cases, logical operators (`and`, `or`) provide a cleaner solution.

---

# Conditional Expression (Ternary Operator)

Sometimes, a decision is simple enough to fit on a single line.

Instead of writing:

```python
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

Python allows us to write the same logic more concisely using a **conditional expression**, also known as the **ternary operator**.

Syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

---

# How It Works

Python evaluates the condition first.

```
age >= 18

↓

True
```

Since the condition is `True`, Python chooses:

```python
"Adult"
```

If the condition were `False`, Python would choose:

```python
"Minor"
```

---

# When Should You Use the Ternary Operator?

Use it only for **simple decisions**.

Good example:

```python
maximum = a if a > b else b
```

Avoid using it for long or complex logic because readability is more important than writing fewer lines.

---

# Truthy and Falsy Values

So far, we've used conditions that explicitly return `True` or `False`.

Example:

```python
age >= 18
```

However, Python allows many values to be used directly in conditions.

Some values behave as `True`, while others behave as `False`.

These are called **truthy** and **falsy** values.

---

# Falsy Values

The following values are considered **False** in a condition:

```python
False
```

```python
None
```

```python
0
```

```python
0.0
```

```python
""
```

(Empty string)

```python
[]
```

(Empty list)

```python
()
```

(Empty tuple)

```python
{}
```

(Empty dictionary)

```python
set()
```

(Empty set)

---

# Truthy Values

Almost everything else is considered `True`.

Examples:

```python
1
```

```python
100
```

```python
-5
```

```python
"Python"
```

```python
[1, 2, 3]
```

```python
{"name": "Alice"}
```

---

# Examples

```python
name = "Alice"

if name:
    print("Name is available.")
```

Output:

```text
Name is available.
```

---

```python
name = ""

if name:
    print("Available")
else:
    print("Empty")
```

Output:

```text
Empty
```

---

# The `match-case` Statement (Python 3.10+)

Python 3.10 introduced the `match-case` statement.

It provides a cleaner alternative to long chains of `if...elif...else` statements when comparing one value against multiple possible cases.

Syntax:

```python
match value:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:
        ...
```

The underscore (`_`) acts as the default case, similar to `else`.

---

# Example

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")
```

Output:

```text
Wednesday
```

---

# When to Use `match-case`

Use `match-case` when:

- Comparing one variable against many fixed values.
- Replacing long `if...elif...else` chains that test equality.

Continue using `if` statements when:

- Conditions involve ranges (`marks >= 90`)
- Conditions use logical operators (`and`, `or`)
- Comparisons are more complex than simple equality.

---

# Common Beginner Mistakes

## 1. Forgetting the Colon (`:`)

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

## 2. Incorrect Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

Python uses indentation to define code blocks.

---

## 3. Using `=` Instead of `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## 4. Wrong Order of `elif` Conditions

Incorrect:

```python
if marks >= 60:
    print("C")
elif marks >= 90:
    print("A")
```

The first condition already matches marks of 90.

Always place more specific conditions before broader ones.

---

## 5. Deeply Nested Conditions

Avoid excessive nesting like this:

```python
if a:
    if b:
        if c:
            if d:
                ...
```

Instead, consider combining conditions with logical operators when appropriate.

---

# Best Practices

- Write clear and meaningful conditions.
- Keep nesting to a minimum.
- Prefer readability over clever one-line solutions.
- Use descriptive variable names.
- Order `elif` conditions carefully.
- Use parentheses for complex logical expressions.
- Test both the `True` and `False` paths.

---

# Real-World Applications

Conditional statements are used in almost every software system.

Examples include:

- ATM withdrawal validation
- Login authentication
- Student grading systems
- Shopping cart discounts
- Weather alerts
- Email spam filtering
- Medical diagnosis support
- Traffic signal control
- Online examination systems
- Mobile app navigation

---

# Interview Tips

Frequently asked interview questions include:

1. What is the difference between `if`, `elif`, and `else`?
2. What is a nested `if` statement?
3. What are truthy and falsy values?
4. Explain the ternary operator.
5. When should you use `match-case`?
6. What happens if multiple `if` conditions are `True`?
7. Why is indentation important in Python?
8. How can logical operators reduce nested `if` statements?

---

# Frequently Asked Questions

## Can an `if` statement exist without an `else`?

Yes.

`else` is optional.

---

## Can there be multiple `elif` statements?

Yes.

A single `if` statement can have zero, one, or many `elif` blocks.

---

## Is `else` always required?

No.

Use `else` only when there is a default action to perform.

---

## Can an `if` statement contain another `if`?

Yes.

This is called a nested `if` statement.

---

# Chapter Summary

In this chapter, you learned:

- Why conditional statements are needed
- The `if` statement
- The `if...else` statement
- The `if...elif...else` statement
- Nested `if` statements
- Conditional (ternary) expressions
- Truthy and falsy values
- The `match-case` statement
- Common mistakes
- Best practices

Conditional statements are one of the most important concepts in programming. They allow software to make decisions, respond to user input, and implement business rules. Almost every algorithm you will study later—from searching and sorting to graph traversal—relies on decision-making.

---

# Practice Questions

## Easy

1. Check whether a number is positive or negative.
2. Determine if a person is eligible to vote.
3. Find the larger of two numbers.
4. Check whether a number is even or odd.
5. Display a grade based on marks.

---

## Medium

1. Determine the largest of three numbers.
2. Check whether a year is a leap year.
3. Create a simple login system.
4. Classify a person's BMI.
5. Build a menu using `match-case`.

---

## Hard

1. Build a mini ATM system.
2. Create a student result processing program.
3. Design a movie ticket pricing system based on age.
4. Create a shipping cost calculator using nested conditions.
5. Implement a tax calculator using multiple conditions.

---

# Further Reading

- Python Official Documentation – Control Flow
- PEP 8 Style Guide
- Python `match-case` Documentation
- Next Chapter: Loops (`for` and `while`)

---

# Key Takeaways

- Conditional statements allow programs to make decisions.
- `if` executes code only when a condition is `True`.
- `else` provides an alternative path when the condition is `False`.
- `elif` allows multiple decision branches.
- Nested `if` statements enable multi-level decision-making.
- Truthy and falsy values simplify many conditions.
- The ternary operator is useful for simple one-line decisions.
- `match-case` offers a clean alternative for equality-based branching.
- Good indentation and clear logic are essential for readable Python code.