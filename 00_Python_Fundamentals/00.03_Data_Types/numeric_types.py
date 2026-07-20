"""
00.03 Data Types - Numeric Types

This module demonstrates Python's built-in numeric data types:
- int
- float
- complex
- bool
- NoneType
"""


def integer_examples() -> None:
    """Demonstrate integer values."""

    positive = 42
    negative = -15
    zero = 0

    print("=== Integer Examples ===")
    print(f"Positive: {positive}")
    print(f"Negative: {negative}")
    print(f"Zero: {zero}")
    print()


def float_examples() -> None:
    """Demonstrate floating-point values."""

    price = 99.99
    pi = 3.14159
    temperature = -12.5

    print("=== Float Examples ===")
    print(f"Price: {price}")
    print(f"Pi: {pi}")
    print(f"Temperature: {temperature}")
    print()


def complex_examples() -> None:
    """Demonstrate complex numbers."""

    number = 3 + 4j

    print("=== Complex Number Example ===")
    print(number)
    print(f"Real Part: {number.real}")
    print(f"Imaginary Part: {number.imag}")
    print()


def boolean_examples() -> None:
    """Demonstrate Boolean values."""

    is_student = True
    is_logged_in = False

    print("=== Boolean Examples ===")
    print(is_student)
    print(is_logged_in)
    print()


def none_example() -> None:
    """Demonstrate None."""

    value = None

    print("=== None Example ===")
    print(value)
    print(type(value))
    print()


if __name__ == "__main__":
    integer_examples()
    float_examples()
    complex_examples()
    boolean_examples()
    none_example()