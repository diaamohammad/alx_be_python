import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  
        self.assertEqual(self.calc.subtract(10, 4), 6)  

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(4,5), 20)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(8,4), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)  # يجب أن تثير قيمة خطأ عند القسمة على صفر

if __name__ == '__main__':
    unittest.main()