"""
Sequence Data Types
"""


def string_example() -> None:
    language = "Python"

    print(language)
    print(language[0])
    print(language[-1])
    print(language[0:3])


def list_example() -> None:
    numbers = [10, 20, 30]

    numbers.append(40)

    print(numbers)


def tuple_example() -> None:
    coordinates = (10, 20)

    print(coordinates)


def range_example() -> None:
    for number in range(5):
        print(number)


if __name__ == "__main__":
    string_example()
    list_example()
    tuple_example()
    range_example()