"""
Bitwise Operators
"""


def bitwise_examples() -> None:
    """
    Demonstrate bitwise operators.
    """
    first = 5
    second = 3

    print("=== Bitwise Operators ===")

    print(f"{first} & {second} = {first & second}")
    print(f"{first} | {second} = {first | second}")
    print(f"{first} ^ {second} = {first ^ second}")
    print(f"~{first} = {~first}")
    print(f"{first} << 1 = {first << 1}")
    print(f"{first} >> 1 = {first >> 1}")

    print()


def binary_representation() -> None:
    """
    Display binary representation of integers.
    """
    number = 13

    print("=== Binary Representation ===")
    print(f"Decimal : {number}")
    print(f"Binary  : {bin(number)}")
    print()


def main() -> None:
    binary_representation()
    bitwise_examples()


if __name__ == "__main__":
    main()