"""
Topic      : 00.07 Loops
File       : example_02_for_loop.py
Repository : Python-DSA-Mastery
Python     : 3.12+

Description:
Demonstrates the fundamentals of the for loop.
"""


def print_numbers() -> None:
    """Print numbers from 1 to 5."""
    for number in range(1, 6):
        print(number)


def print_fruits() -> None:
    """Iterate through a list."""
    fruits = [
        "Apple",
        "Banana",
        "Orange",
        "Mango",
    ]

    for fruit in fruits:
        print(fruit)


def print_characters() -> None:
    """Iterate through a string."""
    word = "Python"

    for character in word:
        print(character)


def main() -> None:
    """Run all examples."""
    print("=== For Loop Examples ===\n")

    print_numbers()

    print()

    print_fruits()

    print()

    print_characters()


if __name__ == "__main__":
    main()