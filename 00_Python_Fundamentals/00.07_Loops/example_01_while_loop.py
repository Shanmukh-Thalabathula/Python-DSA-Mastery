"""
Topic      : 00.07 Loops
File       : example_01_while_loop.py
Repository : Python-DSA-Mastery
Python     : 3.12+

Description:
Demonstrates the fundamentals of the while loop.
"""


def count_numbers() -> None:
    """Print numbers from 1 to 5 using a while loop."""
    count = 1

    while count <= 5:
        print(count)
        count += 1


def countdown() -> None:
    """Print a countdown from 5 to 1."""
    number = 5

    while number >= 1:
        print(number)
        number -= 1

    print("Liftoff!")


def main() -> None:
    """Run all examples."""
    print("=== While Loop Examples ===\n")

    count_numbers()

    print()

    countdown()


if __name__ == "__main__":
    main()