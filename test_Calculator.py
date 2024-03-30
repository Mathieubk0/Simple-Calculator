import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate(5, 3, '+')
        self.assertEqual(result, "5.0 plus 3.0 equals 8.0.")

    def test_subtraction(self):
        result = self.calculator.calculate(5, 3, '-')
        self.assertEqual(result, "5.0 minus 3.0 equals 2.0.")

    def test_multiplication(self):
        result = self.calculator.calculate(5, 3, '*')
        self.assertEqual(result, "5.0 times 3.0 equals 15.0.")

    def test_division(self):
        result = self.calculator.calculate(5, 3, '/')
        self.assertEqual(result, "5.0 divided by 3.0 equals 1.6666666666666667.")

    def test_divide_by_zero(self):
        result = self.calculator.calculate(5, 0, '/')
        self.assertEqual(result, "You can't divide by zero.")

    def test_modulo(self):
        result = self.calculator.calculate(5, 2, '%')
        self.assertEqual(result, "5.0 modulo 2.0 leaves 1.0.")

    def test_invalid_operation(self):
        result = self.calculator.calculate(5, 3, '^')
        self.assertEqual(result, "This isn't a valid operation. Please try again.")

    def test_invalid_input(self):
        result = self.calculator.calculate('lalala', 3, '+')
        self.assertEqual(result, "Invalid input. Please enter valid numbers.")

    def test_negative_numbers(self):
        result = self.calculator.calculate(-5, 3, '+')
        self.assertEqual(result, "-5.0 plus 3.0 equals -2.0.")

    def test_float_numbers(self):
        result = self.calculator.calculate(2.5, 3.5, '+')
        self.assertEqual(result, "2.5 plus 3.5 equals 6.0.")

if __name__ == '__main__':
    unittest.main()