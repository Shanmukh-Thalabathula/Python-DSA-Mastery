"""
Topic      : 00.07 Loops
File       : example_05_nested_loops.py

Demonstrates nested loops.
"""


def star_rectangle() -> None:
    """Print a rectangle of stars."""
    rows = 4
    columns = 5

    for _ in range(rows):
        for _ in range(columns):
            print("*", end=" ")

        print()


def multiplication_table() -> None:
    """Print a multiplication table."""
    print()

    for row in range(1, 6):
        for column in range(1, 6):
            print(f"{row * column:2}", end=" ")

        print()


def main() -> None:
    """Run all examples."""
    print("Rectangle Pattern\n")

    star_rectangle()

    print("\nMultiplication Table\n")

    multiplication_table()


if __name__ == "__main__":
    main()