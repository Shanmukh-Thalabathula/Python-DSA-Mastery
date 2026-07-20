"""
00.06 Conditional Statements - if Statement

This module demonstrates the basic usage of the `if` statement.

Topics covered:
- Simple conditions
- Boolean expressions
- Conditional execution

Author: Python-DSA-Mastery
Python Version: 3.12+
"""


def check_voting_eligibility() -> None:
    """
    Check whether a person is eligible to vote.
    """
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote.")


def check_positive_number() -> None:
    """
    Check whether a number is positive.
    """
    number = float(input("\nEnter a number: "))

    if number > 0:
        print("The number is positive.")


def main() -> None:
    """Run all examples."""
    print("=" * 60)
    print("IF STATEMENT EXAMPLES")
    print("=" * 60)

    check_voting_eligibility()
    check_positive_number()


if __name__ == "__main__":
    main()