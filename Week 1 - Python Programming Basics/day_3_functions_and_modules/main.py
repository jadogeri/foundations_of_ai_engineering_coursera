# 1. Built-in module imports
import math
import math as m
from math import sqrt

# 2. Custom module import (using an alias, just like `import math as m`)
import math_operations as mo

from common.utils import print_header, print_toc_entry, print_sub_section

# Global variable
greeting: str = "Hi"


def add_numbers(a: int, b: int) -> int:
    return a + b


def greet() -> None:
    message: str = "Hello World"
    print(f"Inside greet(): {message}")


def say_hello() -> None:
    print(f"{greeting} from inside the function")


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def print_factorial(n: int) -> None:
    result: int = factorial(n)
    print(f"Factorial of {n} is {result}")


def main() -> None:
    print_header("Day 3: Functions and Modules in Python")
    print_toc_entry(1, "Defining Functions (def, parameters, return)")
    print_toc_entry(2, "Variable Scope (Local vs. Global)")
    print_toc_entry(3, "Importing Built-in Modules")
    print_toc_entry(4, "Importing Custom Modules")
    print_toc_entry(5, "Exercise 1: Recursive Factorial Function")

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

    print_sub_section(4, "Importing Custom Modules")
    num1: int = 10
    num2: int = 5
    print(f"Custom variable (DEFAULT_TAX_RATE): {mo.DEFAULT_TAX_RATE}")
    print(f"Custom add: {mo.add(num1, num2)}")
    print(f"Custom subtract: {mo.subtract(num1, num2)}")
    print(f"Custom multiply: {mo.multiply(num1, num2)}")
    print(f"Custom divide: {mo.divide(num1, num2)}")

    print_sub_section(5, "Exercise 1: Recursive Factorial Function")
    print_factorial(5)
    print_factorial(10)


if __name__ == '__main__':
    main()
