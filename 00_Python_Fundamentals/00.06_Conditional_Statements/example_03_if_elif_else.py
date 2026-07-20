"""
00.06 Conditional Statements - if...elif...else

Demonstrates handling multiple conditions.
"""


def student_grade() -> None:
    """
    Assign a grade based on marks.
    """
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


def traffic_signal() -> None:
    """
    Demonstrate multiple choices using user input.
    """
    color = input("\nEnter traffic light color: ").strip().lower()

    if color == "red":
        print("Stop")
    elif color == "yellow":
        print("Get Ready")
    elif color == "green":
        print("Go")
    else:
        print("Invalid traffic light color.")


def main() -> None:
    """Run all examples."""
    student_grade()
    traffic_signal()


if __name__ == "__main__":
    main()