"""
00.06 Conditional Statements - match-case

Demonstrates Python's match-case statement (Python 3.10+).
"""


def day_of_week() -> None:
    """
    Display the day of the week based on a number.
    """
    day = int(input("Enter a number (1-7): "))

    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day number.")


def simple_calculator() -> None:
    """
    Perform a basic arithmetic operation using match-case.
    """
    first = float(input("\nFirst number: "))
    second = float(input("Second number: "))
    operator = input("Operator (+, -, *, /): ").strip()

    match operator:
        case "+":
            print(f"Result: {first + second}")
        case "-":
            print(f"Result: {first - second}")
        case "*":
            print(f"Result: {first * second}")
        case "/":
            if second != 0:
                print(f"Result: {first / second}")
            else:
                print("Division by zero is not allowed.")
        case _:
            print("Invalid operator.")


def main() -> None:
    """Run all examples."""
    day_of_week()
    simple_calculator()


if __name__ == "__main__":
    main()