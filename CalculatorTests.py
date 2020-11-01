import unittest

from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method(self):
        add_data = CSVReader('csv/Unit Test Addition.csv')
        for row in add_data.data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_subtract_method(self):
        sub_data = CSVReader('csv/Unit Test Subtraction.csv')
        for row in sub_data.data:
            self.assertEqual(self.calculator.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))


if __name__ == '__main__':
    unittest.main()
