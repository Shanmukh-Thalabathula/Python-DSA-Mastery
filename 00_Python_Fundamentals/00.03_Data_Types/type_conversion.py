"""
Type Conversion Examples
"""


def conversion_examples() -> None:
    text = "100"

    number = int(text)

    print(number)
    print(type(number))

    decimal = float(number)

    print(decimal)

    string = str(decimal)

    print(string)

    print(bool(1))
    print(bool(0))


if __name__ == "__main__":
    conversion_examples()