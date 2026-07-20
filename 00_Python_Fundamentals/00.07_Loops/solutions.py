"""
Solutions for Practice Questions - Loops

These solutions demonstrate one possible approach to selected
practice exercises from this chapter.
"""


def multiplication_table(number: int) -> None:
    """Print the multiplication table of a number."""
    print(f"\nMultiplication Table for {number}")

    for multiplier in range(1, 11):
        print(f"{number} × {multiplier} = {number * multiplier}")


def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def fibonacci(count: int) -> None:
    """Print the first 'count' Fibonacci numbers."""
    first = 0
    second = 1

    for _ in range(count):
        print(first, end=" ")

        first, second = second, first + second

    print()


def is_prime(number: int) -> bool:
    """Return True if the given number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def star_pattern(rows: int) -> None:
    """Print a right-angled triangle pattern."""
    for row in range(1, rows + 1):
        print("*" * row)


def main() -> None:
    """Run sample solutions."""
    print("Loop Practice Solutions")

    multiplication_table(5)

    print(f"\nFactorial of 5 = {factorial(5)}")

    print("\nFirst 10 Fibonacci Numbers:")
    fibonacci(10)

    print(f"\nIs 29 Prime? {is_prime(29)}")

    print("\nStar Pattern:")
    star_pattern(5)


if __name__ == "__main__":
    main()