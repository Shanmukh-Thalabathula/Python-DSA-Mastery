"""
Solutions for Practice Questions - User Input

These solutions demonstrate one possible approach to solving the
practice exercises from this chapter.
"""

from math import pi


def add_two_numbers() -> None:
    """Read two integers and display their sum."""
    first = int(input("First Number: "))
    second = int(input("Second Number: "))

    print(f"Sum = {first + second}")


def rectangle_area() -> None:
    """Calculate the area of a rectangle."""
    length = float(input("Length: "))
    width = float(input("Width: "))

    print(f"Area = {length * width}")


def circle_area() -> None:
    """Calculate the area of a circle."""
    radius = float(input("Radius: "))

    print(f"Area = {pi * radius ** 2:.2f}")


def average_of_three() -> None:
    """Calculate the average of three numbers."""
    first = float(input("First: "))
    second = float(input("Second: "))
    third = float(input("Third: "))

    average = (first + second + third) / 3

    print(f"Average = {average:.2f}")


def bmi_calculator() -> None:
    """Calculate the Body Mass Index."""
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = weight / (height ** 2)

    print(f"BMI = {bmi:.2f}")


def shopping_bill() -> None:
    """Calculate the total shopping bill."""
    product = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item: "))

    total = quantity * price

    print(f"\nProduct : {product}")
    print(f"Total   : ₹{total:.2f}")


def main() -> None:
    """Run sample solutions."""
    print("Practice Solutions")

    # Uncomment the function you want to test.

    # add_two_numbers()
    # rectangle_area()
    # circle_area()
    # average_of_three()
    # bmi_calculator()
    # shopping_bill()


if __name__ == "__main__":
    main()