""" Custom Module: Math Utility Package

Create a module with:
- Prime check
- Fibonacci generator
- Factorial
"""


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def fibonacci(count):
    result = []
    a, b = 0, 1
    for _ in range(count):
        result.append(a)
        a, b = b, a + b
    return result


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value
