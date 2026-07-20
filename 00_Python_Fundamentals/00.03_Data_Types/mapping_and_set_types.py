"""
Dictionary and Set Examples
"""


def dictionary_example() -> None:
    student = {
        "name": "Alice",
        "age": 20,
        "course": "Computer Science",
    }

    print(student)
    print(student["name"])


def set_example() -> None:
    numbers = {1, 2, 2, 3, 4, 4}

    print(numbers)


def frozenset_example() -> None:
    values = frozenset([1, 2, 3])

    print(values)


if __name__ == "__main__":
    dictionary_example()
    set_example()
    frozenset_example()