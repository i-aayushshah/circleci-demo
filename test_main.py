import pytest
from main import Calculator, greet


@pytest.fixture
def calc():
    return Calculator()


# ──────────────────────────────────────────────
# Addition
# ──────────────────────────────────────────────
class TestAdd:
    def test_positive_numbers(self, calc):
        assert calc.add(3, 4) == 7

    def test_negative_numbers(self, calc):
        assert calc.add(-2, -5) == -7

    def test_mixed_sign(self, calc):
        assert calc.add(-10, 15) == 5

    def test_floats(self, calc):
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)


# ──────────────────────────────────────────────
# Subtraction
# ──────────────────────────────────────────────
class TestSubtract:
    def test_basic(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_result_negative(self, calc):
        assert calc.subtract(3, 10) == -7


# ──────────────────────────────────────────────
# Multiplication
# ──────────────────────────────────────────────
class TestMultiply:
    def test_basic(self, calc):
        assert calc.multiply(6, 7) == 42

    def test_by_zero(self, calc):
        assert calc.multiply(99, 0) == 0

    def test_negative(self, calc):
        assert calc.multiply(-3, 4) == -12


# ──────────────────────────────────────────────
# Division
# ──────────────────────────────────────────────
class TestDivide:
    def test_basic(self, calc):
        assert calc.divide(20, 4) == 5.0

    def test_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)


# ──────────────────────────────────────────────
# Power
# ──────────────────────────────────────────────
class TestPower:
    def test_square(self, calc):
        assert calc.power(4, 2) == 16

    def test_zero_exponent(self, calc):
        assert calc.power(100, 0) == 1

    def test_large(self, calc):
        assert calc.power(2, 8) == 256


# ──────────────────────────────────────────────
# is_even
# ──────────────────────────────────────────────
class TestIsEven:
    def test_even(self, calc):
        assert calc.is_even(4) is True

    def test_odd(self, calc):
        assert calc.is_even(7) is False

    def test_zero(self, calc):
        assert calc.is_even(0) is True


# ──────────────────────────────────────────────
# Factorial
# ──────────────────────────────────────────────
class TestFactorial:
    def test_zero(self, calc):
        assert calc.factorial(0) == 1

    def test_one(self, calc):
        assert calc.factorial(1) == 1

    def test_five(self, calc):
        assert calc.factorial(5) == 120

    def test_negative_raises(self, calc):
        with pytest.raises(ValueError, match="not defined for negative"):
            calc.factorial(-3)


# ──────────────────────────────────────────────
# greet
# ──────────────────────────────────────────────
class TestGreet:
    def test_normal_name(self):
        assert greet("Alice") == "Hello, Alice! Welcome to the CI/CD demo."

    def test_strips_whitespace(self):
        assert greet("  Bob  ") == "Hello, Bob! Welcome to the CI/CD demo."

    def test_empty_name_raises(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")

    def test_blank_spaces_raises(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("   ")
