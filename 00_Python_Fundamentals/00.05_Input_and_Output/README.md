# 00.05 User Input

> **"A program becomes truly interactive when it can communicate with its users."**

---

# Introduction

So far in this course, our programs have worked with **hard-coded values**.

For example:

```python
age = 20
name = "Alice"

print(age)
print(name)
```

Here, the values are already written inside the program.

But imagine developing a calculator.

Would you write:

```python
number1 = 10
number2 = 20
```

every single time someone wants to perform a calculation?

Of course not.

Instead, the calculator should ask the user:

```text
Enter the first number:
```

The user enters a value.

Then the calculator asks:

```text
Enter the second number:
```

Now the program can perform calculations using the values provided by the user.

This ability to receive information from users is called **User Input**.

Without user input, programs would always produce the same results every time they run.

With user input, programs become **interactive**, **dynamic**, and **useful**.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what user input is.
- Use Python's `input()` function.
- Read data entered by the user.
- Convert input into different data types.
- Read multiple values.
- Handle simple input validation.
- Avoid common beginner mistakes.
- Build interactive Python programs.

---

# Prerequisites

Before studying this chapter, you should understand:

- Variables
- Data Types
- Operators

These concepts are necessary because user input is usually stored in variables and processed using operators.

---

# Why Does User Input Exist?

Imagine a vending machine.

When you approach it, the machine waits for you to:

- Choose a drink
- Insert money
- Select the quantity

The machine cannot decide these values on its own.

It must receive information from you before it can continue.

Programs work in exactly the same way.

Many programs cannot continue until the user provides the required information.

Examples include:

- Logging into a website
- Entering a password
- Searching on Google
- Using an ATM
- Booking a flight
- Filling out an online form

All of these applications rely on user input.

---

# Real-World Analogy

Imagine a conversation.

```
Person A:
What is your name?

↓

Person B:
Alice

↓

Person A:
Nice to meet you, Alice!
```

A Python program behaves similarly.

```
Program:
Enter your name:

↓

User:
Alice

↓

Program:
Hello, Alice!
```

The program asks a question, waits for the user's response, and then continues.

---

# What is User Input?

**User input** is information entered by a user while a program is running.

This information can include:

- Names
- Numbers
- Passwords
- Email addresses
- Choices
- Commands

The program receives this information and uses it to make decisions or perform calculations.

---

# The `input()` Function

Python provides the built-in `input()` function to read data from the keyboard.

Syntax:

```python
input(prompt)
```

The `prompt` is the message displayed to the user.

Example:

```python
name = input("Enter your name: ")
```

When this program runs:

```text
Enter your name:
```

Suppose the user types:

```text
Alice
```

The variable `name` now stores:

```text
Alice
```

---

# How `input()` Works Internally

Let's understand what happens behind the scenes when Python executes the following line:

```python
name = input("Enter your name: ")
```

The execution flow is:

### Step 1

Python prints the prompt.

```text
Enter your name:
```

---

### Step 2

Python pauses execution.

The program waits for the user to type something.

No further code is executed during this time.

---

### Step 3

The user types:

```text
Alice
```

and presses the **Enter** key.

---

### Step 4

Python reads everything the user typed.

```
"Alice"
```

---

### Step 5

Python stores the entered text in the variable.

```
name

↓

"Alice"
```

---

### Step 6

The program continues executing the remaining statements.

---

# Program Flow

The execution can be visualized as:

```text
Program Starts
       │
       ▼
Display Prompt
       │
       ▼
Wait for User Input
       │
       ▼
User Types Data
       │
       ▼
Store Data in Variable
       │
       ▼
Continue Program
```

---

# First Example

```python
name = input("Enter your name: ")

print("Hello,", name)
```

Example execution:

```text
Enter your name: Alice

Hello, Alice
```

---

# Example Without a Prompt

The prompt is optional.

```python
name = input()

print(name)
```

Although this works, it is not recommended because the user has no idea what they should enter.

Always provide a meaningful prompt.

Good example:

```python
age = input("Enter your age: ")
```

---

# Return Type of `input()`

This is one of the most important concepts in this chapter.

Regardless of what the user enters, the `input()` function **always returns a string**.

Example:

```python
age = input("Enter your age: ")
```

Suppose the user enters:

```text
25
```

Many beginners think:

```
25
```

is stored as an integer.

It is not.

Python actually stores:

```text
"25"
```

Notice the quotation marks.

It is a **string**, not an integer.

You can verify this:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

Even if the user enters:

```text
100
```

the result is still:

```python
<class 'str'>
```

---

# Memory Representation

Suppose the user enters:

```text
Alice
```

Memory can be visualized as:

```text
+----------------------+
| Variable : name      |
+----------------------+
| Value    : "Alice"   |
+----------------------+
| Type     : str       |
+----------------------+
```

Now consider:

```python
age = input("Enter age: ")
```

User enters:

```text
21
```

Memory becomes:

```text
+--------------------+
| Variable : age     |
+--------------------+
| Value    : "21"    |
+--------------------+
| Type     : str     |
+--------------------+
```

Although the value looks like a number, it is still stored as a string.

This is why type conversion is often required before performing mathematical operations.

---

# Why This Matters

Suppose the user enters:

```text
10
```

and then:

```text
20
```

If you write:

```python
first = input("First: ")
second = input("Second: ")

print(first + second)
```

The output is:

```text
1020
```

instead of:

```text
30
```

Why?

Because Python is joining two strings together.

This process is called **string concatenation**.

To perform arithmetic operations, the input must first be converted to a numeric type.

We'll learn how to do that in the next section.

---

# Type Conversion

In the previous section, we learned that the `input()` function **always returns a string**.

This is true even if the user enters a number.

For example:

```python
age = input("Enter your age: ")

print(type(age))
```

User enters:

```text
25
```

Output:

```text
<class 'str'>
```

If we want to perform mathematical operations, we must first convert the string into a numeric data type.

This process is called **type conversion** or **type casting**.

---

# Why Type Conversion is Necessary

Consider this program:

```python
first = input("Enter first number: ")
second = input("Enter second number: ")

result = first + second

print(result)
```

User enters:

```text
10
20
```

Output:

```text
1020
```

Many beginners expect:

```text
30
```

Why didn't Python add the numbers?

Because:

```
"10"

+

"20"
```

are strings.

Python joins them together.

This is called **string concatenation**.

To perform addition, we must convert both strings into integers.

---

# Converting to Integer

Python provides the `int()` function.

Syntax:

```python
int(value)
```

Example:

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print(first + second)
```

User enters:

```text
10
20
```

Output:

```text
30
```

Now Python performs arithmetic because both variables are integers.

---

# How `int(input())` Works

Many beginners memorize:

```python
int(input())
```

without understanding what happens internally.

Let's break it down.

```python
age = int(input("Enter age: "))
```

Execution steps:

### Step 1

Display the prompt.

```text
Enter age:
```

↓

### Step 2

User enters:

```text
21
```

↓

### Step 3

`input()` returns:

```python
"21"
```

↓

### Step 4

`int()` converts:

```python
"21"
```

to

```python
21
```

↓

### Step 5

Store the integer.

```text
age

↓

21
```

Now the variable contains an integer instead of a string.

---

# Memory Representation

Before conversion:

```text
+----------------------+
| age                  |
+----------------------+
| "21"                 |
| str                  |
+----------------------+
```

After conversion:

```text
+----------------------+
| age                  |
+----------------------+
| 21                   |
| int                  |
+----------------------+
```

---

# Converting to Float

Sometimes users enter decimal numbers.

Example:

```text
98.75
```

To store decimal values correctly, use `float()`.

```python
price = float(input("Enter price: "))

print(price)
```

User enters:

```text
99.99
```

Output:

```text
99.99
```

Type:

```python
<class 'float'>
```

---

# Converting to String

Sometimes we already have numbers but want to convert them into strings.

Example:

```python
age = 21

text = str(age)

print(text)
print(type(text))
```

Output:

```text
21
<class 'str'>
```

---

# Converting to Boolean

Python also provides the `bool()` function.

```python
print(bool(1))
```

Output:

```text
True
```

```python
print(bool(0))
```

Output:

```text
False
```

However, be careful when converting user input directly.

Example:

```python
value = bool(input("Enter value: "))

print(value)
```

If the user enters:

```text
False
```

The output is:

```text
True
```

Why?

Because any **non-empty string** is considered `True` in Python.

We'll learn better ways to handle Boolean input in later chapters.

---

# Reading Multiple Inputs

Many programs need more than one value.

Example:

```python
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
```

Execution:

```text
Name: Alice
Age: 20
City: London
```

The program stores all three values separately.

---

# Reading Multiple Values on One Line

Sometimes users enter several values on the same line.

Example:

```text
10 20
```

Python reads this as one string:

```text
"10 20"
```

To separate the values, use the `split()` method.

---

# The `split()` Method

`split()` divides a string into smaller pieces using a separator.

Example:

```python
numbers = input("Enter two numbers: ").split()

print(numbers)
```

User enters:

```text
10 20
```

Output:

```python
['10', '20']
```

Notice that both values are still strings.

---

# Storing Multiple Values

Python allows unpacking.

```python
first, second = input("Enter two numbers: ").split()

print(first)
print(second)
```

User enters:

```text
10 20
```

Output:

```text
10
20
```

Again, both variables contain strings.

---

# Using `map()`

To convert multiple inputs at once, use `map()`.

Example:

```python
first, second = map(int, input("Enter two numbers: ").split())

print(first + second)
```

User enters:

```text
10 20
```

Output:

```text
30
```

### How It Works

```text
Input

↓

"10 20"

↓

split()

↓

["10", "20"]

↓

map(int, ...)

↓

[10, 20]

↓

Store in variables
```

---

# Reading a List of Numbers

A very common interview pattern is reading a list of integers.

```python
numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)
```

User enters:

```text
5 10 15 20
```

Output:

```python
[5, 10, 15, 20]
```

This pattern appears frequently in competitive programming and coding interviews.

---

# Common Conversion Errors

Suppose the user enters:

```text
Twenty
```

Now consider:

```python
age = int(input("Age: "))
```

Python raises an error because `"Twenty"` cannot be converted into an integer.

```text
ValueError
```

Always ensure the entered value matches the expected type.

Later, we'll learn how to handle these errors gracefully using exception handling.

---

# Dry Run

Program:

```python
first = int(input("First: "))
second = int(input("Second: "))

print(first + second)
```

Execution:

```text
First:
```

User enters:

```text
15
```

Python stores:

```text
15
```

↓

Next prompt:

```text
Second:
```

User enters:

```text
25
```

Python stores:

```text
25
```

↓

Computation:

```text
15 + 25

↓

40
```

Output:

```text
40
```

---

# Input Validation Basics

User input is unpredictable.

A program should never assume that the user will always enter the correct information.

For example, consider this program:

```python
age = int(input("Enter your age: "))
```

If the user enters:

```text
Twenty
```

Python raises:

```text
ValueError
```

This happens because `"Twenty"` cannot be converted into an integer.

In professional applications, user input should always be validated before using it.

For now, remember this simple rule:

> **Never trust user input. Always expect mistakes.**

Later in this course, we'll learn **exception handling (`try` and `except`)** to manage invalid input safely.

---

# Practical Examples

## Example 1: Greeting the User

```python
name = input("Enter your name: ")

print(f"Welcome, {name}!")
```

Example Output:

```text
Enter your name: Alice

Welcome, Alice!
```

---

## Example 2: Add Two Numbers

```python
first = int(input("First Number: "))
second = int(input("Second Number: "))

print("Sum =", first + second)
```

Example Output:

```text
First Number: 15
Second Number: 25

Sum = 40
```

---

## Example 3: Calculate Age Next Year

```python
age = int(input("Enter your age: "))

print("Next year you will be", age + 1)
```

---

## Example 4: Area of a Rectangle

```python
length = float(input("Length: "))
width = float(input("Width: "))

area = length * width

print("Area =", area)
```

---

## Example 5: Temperature Converter

```python
celsius = float(input("Temperature (°C): "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature (°F):", fahrenheit)
```

---

# Flow of User Input

The complete process looks like this:

```text
          Start
            │
            ▼
 Display Prompt
            │
            ▼
 Wait for User
            │
            ▼
 Receive Input
            │
            ▼
 Store as String
            │
            ▼
 Type Conversion
            │
            ▼
 Process Data
            │
            ▼
 Display Result
            │
            ▼
           End
```

---

# Common Beginner Mistakes

## 1. Forgetting Type Conversion

Incorrect:

```python
age = input("Age: ")

print(age + 10)
```

This causes an error because `age` is a string.

Correct:

```python
age = int(input("Age: "))

print(age + 10)
```

---

## 2. Assuming `input()` Returns an Integer

Incorrect assumption:

```python
number = input()

# number is an integer ❌
```

Reality:

```python
number

↓

"25"
```

It is a string.

---

## 3. Using `bool(input())`

Many beginners expect:

```python
value = bool(input())
```

If the user types:

```text
False
```

they expect:

```python
False
```

Instead, Python returns:

```python
True
```

because `"False"` is a non-empty string.

---

## 4. Forgetting `split()`

Incorrect:

```python
a, b = input()
```

Correct:

```python
a, b = input().split()
```

---

## 5. Forgetting `map()`

Incorrect:

```python
a, b = input().split()

print(a + b)
```

Output:

```text
1020
```

Correct:

```python
a, b = map(int, input().split())

print(a + b)
```

Output:

```text
30
```

---

# Best Practices

- Always provide meaningful prompts.
- Convert input to the correct data type immediately.
- Use descriptive variable names.
- Keep prompts simple and clear.
- Validate user input whenever possible.
- Avoid unnecessary conversions.
- Use `map()` when reading multiple numeric values.
- Write user-friendly output messages.

---

# Real-World Applications

User input is used in almost every software application.

Examples include:

- ATM systems
- Banking applications
- Online shopping websites
- Login forms
- Search engines
- Flight booking systems
- Hospital management systems
- Student registration portals
- Mobile applications
- Games

Without user input, these applications could not interact with users.

---

# Interview Tips

Some common interview questions related to user input include:

1. What does the `input()` function return?
2. Why is type conversion necessary?
3. What is the difference between `int(input())` and `input()`?
4. How do you read multiple integers on one line?
5. Explain the purpose of `split()`.
6. Explain how `map()` works.
7. What happens if `int()` receives invalid input?
8. Why is input validation important?

---

# Frequently Asked Questions

## Why does `input()` always return a string?

Python keeps `input()` simple by treating all keyboard input as text. The programmer decides how to interpret that text using functions like `int()` or `float()`.

---

## When should I use `float()` instead of `int()`?

Use `float()` whenever decimal values are expected.

Examples:

- Price
- Weight
- Height
- Temperature

---

## What happens if the user presses Enter without typing anything?

`input()` returns an empty string:

```python
""
```

---

## Can I read multiple values using one `input()` call?

Yes.

Example:

```python
numbers = input().split()
```

Or, for integers:

```python
numbers = list(map(int, input().split()))
```

---

# Chapter Summary

In this chapter, you learned:

- What user input is
- How the `input()` function works
- Why `input()` always returns a string
- Type conversion using `int()`, `float()`, `str()`, and `bool()`
- Reading multiple inputs with `split()`
- Converting multiple values using `map()`
- Reading a list of integers
- Input validation basics
- Common mistakes
- Best practices

User input transforms a static program into an interactive application. It is a foundational concept that you'll use throughout your Python journey, from simple scripts to large-scale software systems.

---

# Practice Questions

## Easy

1. Read your name and display a greeting.
2. Read your age and display your age next year.
3. Read two integers and display their sum.
4. Read the length and width of a rectangle and calculate its area.
5. Read a temperature in Celsius and convert it to Fahrenheit.

---

## Medium

1. Read three numbers and calculate their average.
2. Read five integers on one line and display their sum.
3. Create a simple interest calculator.
4. Read a student's marks and calculate the percentage.
5. Read a radius and calculate the area of a circle.

---

## Hard

1. Build a simple calculator using user input.
2. Create a BMI calculator.
3. Read a list of numbers and display the largest value.
4. Build a menu-driven unit converter.
5. Design a simple login program using user input.

---

# Further Reading

- Python Official Documentation – `input()`
- Python Built-in Functions
- Python Data Types
- Exception Handling (`try` / `except`) *(upcoming topic)*
- Conditional Statements (`if`, `elif`, `else`) *(next chapter)*

---

# Key Takeaways

- `input()` allows programs to interact with users.
- `input()` always returns a string.
- Use `int()` or `float()` when numeric calculations are required.
- Use `split()` to separate multiple values.
- Use `map()` to convert multiple values efficiently.
- Always provide clear prompts for users.
- Validate user input whenever possible.
- Understanding user input is essential before learning conditional statements and loops.