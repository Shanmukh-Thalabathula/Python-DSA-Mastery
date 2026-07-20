"""
Solutions for Practice Questions - Conditional Statements

These solutions demonstrate one possible implementation for selected
practice problems from this chapter.
"""


def even_or_odd() -> None:
    """Determine whether a number is even or odd."""
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def largest_of_two() -> None:
    """Display the larger of two numbers."""
    first = float(input("First number: "))
    second = float(input("Second number: "))

    if first > second:
        print(f"Largest: {first}")
    else:
        print(f"Largest: {second}")


def student_grade() -> None:
    """Assign a grade based on marks."""
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")


def login_system() -> None:
    """Validate simple login credentials."""
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "python123":
        print("Login Successful")
    else:
        print("Invalid Credentials")


def atm_withdrawal() -> None:
    """Simulate a simple ATM withdrawal."""
    balance = float(input("Account Balance: "))
    amount = float(input("Withdrawal Amount: "))

    if amount <= balance:
        print("Transaction Successful")
        print(f"Remaining Balance: ₹{balance - amount:.2f}")
    else:
        print("Insufficient Balance")


def main() -> None:
    """Run sample solutions."""
    print("Conditional Statements - Practice Solutions")

    # Uncomment the function you want to test.

    # even_or_odd()
    # largest_of_two()
    # student_grade()
    # login_system()
    # atm_withdrawal()


if __name__ == "__main__":
    main()