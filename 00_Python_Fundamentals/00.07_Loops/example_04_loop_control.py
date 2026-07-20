"""
Topic      : 00.07 Loops
File       : example_04_loop_control.py

Demonstrates break, continue, and pass.
"""


def break_example() -> None:
    """Stop the loop early."""
    print("Break Example")

    for number in range(1, 11):
        if number == 6:
            break

        print(number)


def continue_example() -> None:
    """Skip one iteration."""
    print("\nContinue Example")

    for number in range(1, 6):
        if number == 3:
            continue

        print(number)


def pass_example() -> None:
    """Placeholder statement."""
    print("\nPass Example")

    for number in range(5):
        if number == 2:
            pass

        print(number)


def main() -> None:
    """Run all examples."""
    break_example()
    continue_example()
    pass_example()


if __name__ == "__main__":
    main()