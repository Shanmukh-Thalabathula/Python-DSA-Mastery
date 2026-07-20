"""
00.06 Conditional Statements - Nested if

Demonstrates nested conditional statements.
"""


def driving_eligibility() -> None:
    """
    Check whether a person can drive.
    """
    age = int(input("Enter your age: "))
    has_license = input("Do you have a driving license? (yes/no): ").strip().lower()

    if age >= 18:
        if has_license == "yes":
            print("You are allowed to drive.")
        else:
            print("You need a valid driving license.")
    else:
        print("You are not old enough to drive.")


def main() -> None:
    """Run the nested if example."""
    driving_eligibility()


if __name__ == "__main__":
    main()