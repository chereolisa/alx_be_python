# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a fresh calculator instance before each test method."""
        self.calc = SimpleCalculator()

    # ==================== ADD TESTS ====================
    def test_addition_positive_numbers(self):
        """Test addition with positive integers and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertEqual(self.calc.add(7, -2), 5)

    def test_addition_with_zero(self):
        """Test addition when one or both numbers are zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # ==================== SUBTRACT TESTS ====================
    def test_subtraction_positive(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(100, 27), 73)

    def test_subtraction_negative_result(self):
        """Test when result is negative."""
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 8), -8)

    def test_subtraction_with_zero(self):
        """Test subtracting zero or from zero."""
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # ==================== MULTIPLY TESTS ====================
    def test_multiplication_basic(self):
        """Test multiplication with normal numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 8), 40)

    def test_multiplication_by_zero(self):
        """Test multiplication involving zero."""
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_negatives(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(4, -6), -24)
        self.assertEqual(self.calc.multiply(-7, -2), 14)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(1.1, 2), 2.2)

    # ==================== DIVIDE TESTS ====================
    def test_division_normal(self):
        """Test regular division cases."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

    def test_division_by_zero(self):
        """Test that division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-15, 5), -3.0)
        self.assertEqual(self.calc.divide(20, -4), -5.0)
        self.assertEqual(self.calc.divide(-9, -3), 3.0)

    def test_division_float_result(self):
        """Test division that results in a float."""
        self.assertEqual(self.calc.divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=10)


if __name__ == '__main__':
    unittest.main(verbosity=2)