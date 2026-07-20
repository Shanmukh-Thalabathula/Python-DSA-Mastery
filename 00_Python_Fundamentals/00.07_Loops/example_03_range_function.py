"""
Topic      : 00.07 Loops
File       : example_03_range_function.py

Demonstrates the different ways to use range().
"""


def stop_only() -> None:
    """Use range(stop)."""
    print("range(5):")

    for number in range(5):
        print(number)


def start_stop() -> None:
    """Use range(start, stop)."""
    print("\nrange(2, 8):")

    for number in range(2, 8):
        print(number)


def start_stop_step() -> None:
    """Use range(start, stop, step)."""
    print("\nrange(2, 11, 2):")

    for number in range(2, 11, 2):
        print(number)


def reverse_count() -> None:
    """Count backwards."""
    print("\nrange(10, 0, -1):")

    for number in range(10, 0, -1):
        print(number)


def main() -> None:
    """Run all examples."""
    stop_only()
    start_stop()
    start_stop_step()
    reverse_count()


if __name__ == "__main__":
    main()