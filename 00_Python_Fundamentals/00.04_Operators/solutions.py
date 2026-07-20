"""
Solutions for Practice Questions - Operators

These solutions demonstrate one possible approach to solving the
practice problems from this chapter.
"""


def add_two_numbers(first: int, second: int) -> int:
    """Return the sum of two integers."""
    return first + second


def rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width


def is_even(number: int) -> bool:
    """Return True if the number is even."""
    return number % 2 == 0


def compare_numbers(first: int, second: int) -> str:
    """Compare two integers and describe their relationship."""
    if first > second:
        return "First number is greater."
    if first < second:
        return "Second number is greater."
    return "Both numbers are equal."


def update_score(score: int) -> int:
    """Perform a sequence of compound assignment operations."""
    score += 10
    score *= 2
    score -= 15
    score //= 5
    return score


def can_vote(age: int) -> bool:
    """Return True if the person is eligible to vote."""
    return age >= 18


def has_passed(marks: int) -> bool:
    """Return True if the student has passed."""
    return marks >= 40


def authenticate(
    username: str,
    password: str,
) -> bool:
    """Validate username and password."""
    return username == "admin" and password == "python123"


def check_membership(item: str) -> bool:
    """Check whether an item exists in the fruits list."""
    fruits = ["Apple", "Banana", "Orange"]
    return item in fruits


def calculator(first: float, second: float) -> None:
    """Display results of common arithmetic operations."""
    print(f"Addition: {first + second}")
    print(f"Subtraction: {first - second}")
    print(f"Multiplication: {first * second}")

    if second != 0:
        print(f"Division: {first / second}")
        print(f"Floor Division: {first // second}")
        print(f"Modulus: {first % second}")
    else:
        print("Division, floor division, and modulus are undefined for zero.")

    print(f"Exponent: {first ** second}")


def admission_eligible(
    age: int,
    marks: int,
    citizen: bool,
) -> bool:
    """Check admission eligibility."""
    return age >= 18 and marks >= 60 and citizen


def main() -> None:
    """Run sample demonstrations."""
    print("=== Practice Solutions ===")

    print(add_two_numbers(10, 20))
    print(rectangle_area(5, 4))
    print(is_even(18))
    print(compare_numbers(10, 20))
    print(update_score(50))
    print(can_vote(21))
    print(has_passed(75))
    print(authenticate("admin", "python123"))
    print(check_membership("Apple"))
    print(admission_eligible(20, 75, True))

    calculator(10, 3)


if __name__ == "__main__":
    main()