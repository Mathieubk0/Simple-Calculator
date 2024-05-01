import unittest
from CalculatorWithGUI import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def cleanAfterEachTest(self):
        pass

    def test_press(self):
        self.calculator.press('5')
        self.assertEqual(self.calculator.expression, '5')
        self.assertEqual(self.calculator.operation.get(), '5')

    def test_clear(self):
        self.calculator.press('5')
        self.calculator.press('+')
        self.calculator.press('7')
        self.calculator.clear()
        self.assertEqual(self.calculator.expression, '')
        self.assertEqual(self.calculator.operation.get(), '')

    def test_addition(self):
        self.calculator.press('5')
        self.calculator.press('+')
        self.calculator.press('7')
        self.calculator.calculate()
        self.assertEqual(self.calculator.expression, '')
        self.assertEqual(self.calculator.operation.get(), '12')

    def test_subtraction(self):
        self.calculator.press('9')
        self.calculator.press('-')
        self.calculator.press('4')
        self.calculator.calculate()
        self.assertEqual(self.calculator.expression, '')
        self.assertEqual(self.calculator.operation.get(), '5')

    def test_multiplication(self):
        self.calculator.press('6')
        self.calculator.press('*')
        self.calculator.press('3')
        self.calculator.calculate()
        self.assertEqual(self.calculator.expression, '')
        self.assertEqual(self.calculator.operation.get(), '18')

    def test_division(self):
        self.calculator.press('10')
        self.calculator.press('/')
        self.calculator.press('2')
        self.calculator.calculate()
        self.assertEqual(self.calculator.expression, '')
        self.assertEqual(self.calculator.operation.get(), '5.0')

    def test_division_by_zero(self):
        self.calculator.press('8')
        self.calculator.press('/')
        self.calculator.press('0')
        self.calculator.calculate()
        self.assertEqual(self.calculator.operation.get(), 'Error')

    def test_wrong_input(self):
        self.calculator.press('5')
        self.calculator.press('+')
        self.calculator.press('abc')
        self.calculator.calculate()
        self.assertEqual(self.calculator.operation.get(), 'Error')

    def test_memory_operations(self):
        self.calculator.operation.set('15')
        self.calculator.save_to_memory()
        self.calculator.clear()
        self.calculator.retrieve_from_memory()
        self.assertEqual(self.calculator.expression, '15')

    def test_clear_memory(self):
        self.calculator.operation.set('15')
        self.calculator.save_to_memory()
        self.calculator.clear_memory()
        with open("memory.txt", "r") as file:
            memory_contents = file.read()
            self.assertEqual(memory_contents, '') 

    def test_memory_empty_recall(self):
        self.calculator.retrieve_from_memory()
        self.assertEqual(self.calculator.operation.get(), 'Nothing stored yet 🤓')

if __name__ == '__main__':
    unittest.main()