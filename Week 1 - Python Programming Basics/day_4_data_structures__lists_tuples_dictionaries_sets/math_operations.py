# math_operations.py
DEFAULT_TAX_RATE: float = 0.05


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
