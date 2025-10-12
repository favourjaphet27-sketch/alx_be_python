"""
Calculator class demonstrating static and class methods.
"""


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print calculation type and return product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
