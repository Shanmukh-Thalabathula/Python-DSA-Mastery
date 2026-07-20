"""
00.05 User Input - Practical Examples

Real-world examples demonstrating the use of user input.
"""


def simple_calculator() -> None:
    """
    Add two numbers entered by the user.
    """
    print("\n=== Simple Calculator ===")

    first = float(input("First Number : "))
    second = float(input("Second Number: "))

    print(f"Sum: {first + second}")


def rectangle_area() -> None:
    """
    Calculate the area of a rectangle.
    """
    print("\n=== Rectangle Area ===")

    length = float(input("Length: "))
    width = float(input("Width : "))

    area = length * width

    print(f"Area = {area}")


def temperature_converter() -> None:
    """
    Convert Celsius to Fahrenheit.
    """
    print("\n=== Temperature Converter ===")

    celsius = float(input("Temperature (°C): "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"Temperature (°F): {fahrenheit:.2f}")


def bmi_calculator() -> None:
    """
    Calculate Body Mass Index (BMI).
    """
    print("\n=== BMI Calculator ===")

    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))

    bmi = weight / (height ** 2)

    print(f"BMI: {bmi:.2f}")


def main() -> None:
    """
    Execute all practical examples.
    """
    simple_calculator()
    rectangle_area()
    temperature_converter()
    bmi_calculator()


if __name__ == "__main__":
    main()