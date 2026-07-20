"""
00.04 Operators

Comparison and Logical Operators
"""

def comparison_examples() -> None:
    """
    Demonstrate comparison operators.
    """
    first = 20
    second = 15

    print("=== Comparison Operators ===")
    print(f"{first} == {second}: {first == second}")
    print(f"{first} != {second}: {first != second}")
    print(f"{first} > {second}: {first > second}")
    print(f"{first} < {second}: {first < second}")
    print(f"{first} >= {second}: {first >= second}")
    print(f"{first} <= {second}: {first <= second}")
    print()


def logical_examples() -> None:
    """
    Demonstrate logical operators.
    """
    age = 21
    marks = 82

    print("=== Logical Operators ===")

    print(age >= 18 and marks >= 60)

    print(age >= 18 or marks >= 90)

    print(not (age < 18))

    print()


def short_circuit_example() -> None:
    """
    Demonstrate short-circuit evaluation.
    """
    print("=== Short Circuit ===")

    print(False and print("Will not execute"))

    print(True or print("Will not execute"))

    print()


def main() -> None:
    comparison_examples()
    logical_examples()
    short_circuit_example()


if __name__ == "__main__":
    main()