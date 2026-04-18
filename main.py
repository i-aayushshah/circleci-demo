class Calculator:
    """A simple calculator with basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def is_even(self, n):
        return n % 2 == 0

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


def greet(name: str) -> str:
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    return f"Hello, {name.strip()}! Welcome to the CI/CD demo."


if __name__ == "__main__":
    calc = Calculator()
    print("Calculator Demo")
    print(f"  5 + 3  = {calc.add(5, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  6 * 7  = {calc.multiply(6, 7)}")
    print(f"  20 / 4 = {calc.divide(20, 4)}")
    print(f"  2 ^ 8  = {calc.power(2, 8)}")
    print(f"  5!     = {calc.factorial(5)}")
    print()
    print(greet("CircleCI"))
