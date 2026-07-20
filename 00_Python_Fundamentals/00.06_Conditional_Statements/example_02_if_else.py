"""
00.06 Conditional Statements - if...else

Demonstrates choosing between two execution paths.
"""


def even_or_odd() -> None:
    """
    Determine whether a number is even or odd.
    """
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


def login_check() -> None:
    """
    Simulate a simple login check.
    """
    password = input("\nEnter password: ")

    if password == "python123":
        print("Access Granted.")
    else:
        print("Access Denied.")


def main() -> None:
    """Run all examples."""
    even_or_odd()
    login_check()


if __name__ == "__main__":
    main()