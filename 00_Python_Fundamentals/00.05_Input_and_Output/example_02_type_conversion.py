"""
00.05 User Input - Type Conversion

Demonstrates converting user input into different data types.
"""


def integer_input() -> None:
    """
    Read an integer from the user.
    """
    age = int(input("Enter your age: "))

    print(f"Next year you will be {age + 1} years old.")


def float_input() -> None:
    """
    Read a floating-point number.
    """
    height = float(input("\nEnter your height (in meters): "))

    print(f"Your height is {height:.2f} meters.")


def string_conversion() -> None:
    """
    Convert an integer to a string.
    """
    number = 100

    text = str(number)

    print("\nString Conversion")
    print(text)
    print(type(text))


def main() -> None:
    """
    Run all examples.
    """
    integer_input()
    float_input()
    string_conversion()


if __name__ == "__main__":
    main()