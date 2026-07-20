"""
00.05 User Input - Multiple Inputs

Demonstrates reading multiple values from a single line.
"""


def read_two_numbers() -> None:
    """
    Read two integers from one line.
    """
    first, second = map(
        int,
        input("Enter two integers separated by a space: ").split(),
    )

    print(f"First Number : {first}")
    print(f"Second Number: {second}")
    print(f"Sum          : {first + second}")


def read_list_of_numbers() -> None:
    """
    Read a list of integers.
    """
    numbers = list(
        map(
            int,
            input("\nEnter numbers separated by spaces: ").split(),
        )
    )

    print(f"Numbers: {numbers}")
    print(f"Total Numbers: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")


def main() -> None:
    """
    Execute all examples.
    """
    read_two_numbers()
    read_list_of_numbers()


if __name__ == "__main__":
    main()