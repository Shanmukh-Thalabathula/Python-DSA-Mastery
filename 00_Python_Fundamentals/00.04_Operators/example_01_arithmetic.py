"""
00.04 Operators - Arithmetic Operators

This module demonstrates Python's arithmetic operators.

Topics covered:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Floor Division (//)
- Modulus (%)
- Exponent (**)

Author: Python-DSA-Mastery
Python Version: 3.12+
"""


def addition_example() -> None:
    """
    Demonstrate the addition operator.
    """
    first_number = 15
    second_number = 10

    result = first_number + second_number

    print("=== Addition ===")
    print(f"{first_number} + {second_number} = {result}")
    print()


def subtraction_example() -> None:
    """
    Demonstrate the subtraction operator.
    """
    first_number = 20
    second_number = 8

    result = first_number - second_number

    print("=== Subtraction ===")
    print(f"{first_number} - {second_number} = {result}")
    print()


def multiplication_example() -> None:
    """
    Demonstrate the multiplication operator.
    """
    length = 5
    width = 4

    area = length * width

    print("=== Multiplication ===")
    print(f"Rectangle Area = {area}")
    print()


def division_example() -> None:
    """
    Demonstrate floating-point division.
    """
    number = 7
    divisor = 2

    result = number / divisor

    print("=== Division ===")
    print(f"{number} / {divisor} = {result}")
    print()


def floor_division_example() -> None:
    """
    Demonstrate floor division.
    """
    number = 7
    divisor = 2

    result = number // divisor

    print("=== Floor Division ===")
    print(f"{number} // {divisor} = {result}")
    print()


def modulus_example() -> None:
    """
    Demonstrate the modulus operator.
    """
    number = 17

    remainder = number % 5

    print("=== Modulus ===")
    print(f"17 % 5 = {remainder}")

    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

    print()


def exponent_example() -> None:
    """
    Demonstrate the exponent operator.
    """
    base = 2
    power = 5

    result = base ** power

    print("=== Exponent ===")
    print(f"{base}^{power} = {result}")
    print()


def string_operator_example() -> None:
    """
    Demonstrate arithmetic operators with strings.
    """
    language = "Python"

    print("=== String Operators ===")
    print(language + " Programming")
    print(language * 3)
    print()


def operator_precedence_example() -> None:
    """
    Demonstrate operator precedence.
    """
    result_one = 2 + 3 * 4
    result_two = (2 + 3) * 4

    print("=== Operator Precedence ===")
    print(f"2 + 3 * 4 = {result_one}")
    print(f"(2 + 3) * 4 = {result_two}")
    print()


def main() -> None:
    """
    Execute all arithmetic operator examples.
    """
    print("=" * 60)
    print("ARITHMETIC OPERATORS")
    print("=" * 60)
    print()

    addition_example()
    subtraction_example()
    multiplication_example()
    division_example()
    floor_division_example()
    modulus_example()
    exponent_example()
    string_operator_example()
    operator_precedence_example()


if __name__ == "__main__":
    main()