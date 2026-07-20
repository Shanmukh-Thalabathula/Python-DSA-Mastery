"""
Assignment, Identity and Membership Operators
"""


def assignment_examples() -> None:
    """
    Demonstrate assignment operators.
    """
    score = 10

    print("=== Assignment Operators ===")

    score += 5
    print(score)

    score *= 2
    print(score)

    score -= 4
    print(score)

    score //= 3
    print(score)

    print()


def identity_examples() -> None:
    """
    Demonstrate identity operators.
    """
    first = [1, 2, 3]
    second = first
    third = [1, 2, 3]

    print("=== Identity Operators ===")

    print(first is second)
    print(first == second)

    print(first is third)
    print(first == third)

    print()


def membership_examples() -> None:
    """
    Demonstrate membership operators.
    """
    fruits = ["Apple", "Banana", "Orange"]

    print("=== Membership Operators ===")

    print("Apple" in fruits)

    print("Mango" not in fruits)

    print("Banana" in fruits)

    print()


def main() -> None:
    assignment_examples()
    identity_examples()
    membership_examples()


if __name__ == "__main__":
    main()