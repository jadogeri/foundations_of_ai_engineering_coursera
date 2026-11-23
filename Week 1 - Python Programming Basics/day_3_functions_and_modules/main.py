import math
import math as m
from math import sqrt
from common.utils import print_header, print_toc_entry, print_sub_section

# Global variable for Sub-section 2
greeting: str = "Hi"


# --- Sub-section 1: Basic Function ---
def add_numbers(a: int, b: int) -> int:
    return a + b


# --- Sub-section 2: Local & Global Scope Functions ---
def greet() -> None:
    message: str = "Hello World"
    print(f"Inside greet(): {message}")


def say_hello() -> None:
    print(f"{greeting} from inside the function")


# --- Sub-section 4: Exercise 1 (Recursive Factorial) ---
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def print_factorial(n: int) -> None:
    result: int = factorial(n)
    print(f"Factorial of {n} is {result}")


# --- Sub-section 5: Exercise 2 (Math Operations Functions) ---
# (In a multi-file setup, these would live in math_operations.py and be imported as `mo`)
def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> float | str:
    if b != 0:
        return a / b
    return "Division by zero is not allowed"


# --- Sub-section 6: Practice 1 (Even/Odd Checker) ---
def is_even(n: int) -> bool:
    return n % 2 == 0


def print_even_or_odd(n: int) -> None:
    if is_even(n):
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")


# --- Sub-section 7: Practice 2 (String Operations Functions) ---
# (In a multi-file setup, these would live in string_operations.py and be imported as `so`)
def reverse_string(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels: str = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    cleaned: str = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def main() -> None:
    print_header("Day 3: Functions and Modules in Python")
    print_toc_entry(1, "Defining Functions (def, parameters, return)")
    print_toc_entry(2, "Variable Scope (Local vs. Global)")
    print_toc_entry(3, "Importing Built-in Modules")
    print_toc_entry(4, "Exercise 1: Recursive Factorial Function")
    print_toc_entry(5, "Exercise 2: Math Operations")
    print_toc_entry(6, "Practice 1: Even or Odd Checker")
    print_toc_entry(7, "Practice 2: String Operations")

    print_sub_section(1, "Defining Functions (def, parameters, return)")
    sum_result: int = add_numbers(45, 3)
    print(f"Sum of 45 and 3 is: {sum_result}")

    print_sub_section(2, "Variable Scope (Local vs. Global)")
    greet()
    # print(message)  # Raises NameError: 'message' is local to greet()
    say_hello()
    print(f"{greeting} from outside the function")

    print_sub_section(3, "Importing Built-in Modules")
    print(f"Full import (math.sqrt): {math.sqrt(16)}")
    print(f"Specific import (sqrt): {sqrt(16)}")
    print(f"Alias import (m.sqrt): {m.sqrt(16)}")

    print_sub_section(4, "Exercise 1: Recursive Factorial Function")
    print_factorial(5)
    print_factorial(10)

    print_sub_section(5, "Exercise 2: Math Operations")
    num1: int = 10
    num2: int = 5
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraction: {subtract(num1, num2)}")
    print(f"Multiplication: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")

    print_sub_section(6, "Practice 1: Even or Odd Checker")
    print_even_or_odd(10)
    print_even_or_odd(7)

    print_sub_section(7, "Practice 2: String Operations")
    sample_word: str = "Racecar"
    print(f"Original word: {sample_word}")
    print(f"Reversed: {reverse_string(sample_word)}")
    print(f"Vowel count: {count_vowels(sample_word)}")
    print(f"Is palindrome?: {is_palindrome(sample_word)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
