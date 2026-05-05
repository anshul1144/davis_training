"""Main Program for Math Utility Package

Imports math_utility_package and uses:
- Prime check
- Fibonacci generator
- Factorial
"""

from math_utility_package import factorial, fibonacci, is_prime


if __name__ == "__main__":
    num = 11
    print(f"Is {num} prime?", is_prime(num))
    print("Fibonacci (10 terms):", fibonacci(10))
    print("Factorial of 5:", factorial(5))
