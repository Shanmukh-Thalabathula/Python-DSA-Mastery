"""
00.05 User Input - Basic Input

This module demonstrates how to read input from the user using Python's
built-in input() function.

Topics covered:
- Reading text input
- Displaying user input
- Using descriptive prompts

Author: Python-DSA-Mastery
Python Version: 3.12+
"""


def greet_user() -> None:
    """
    Ask the user for their name and greet them.
    """
    name = input("Enter your name: ")

    print("\nHello,", name)
    print("Welcome to Python-DSA-Mastery!")


def favorite_language() -> None:
    """
    Read the user's favorite programming language.
    """
    language = input("\nWhat is your favorite programming language? ")

    print(f"You like {language}. Great choice!")


def city_information() -> None:
    """
    Read the user's city.
    """
    city = input("\nEnter your city: ")

    print(f"You live in {city}.")


def main() -> None:
    """
    Execute all examples.
    """
    print("=" * 60)
    print("BASIC USER INPUT")
    print("=" * 60)

    greet_user()
    favorite_language()
    city_information()


if __name__ == "__main__":
    main()