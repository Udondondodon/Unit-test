import unittest
from mathcode import *

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator('1', 5, 3)
        self.assertEqual(result, 'Hasil operasi dari 5 + 3 = 9')

    def test_subtraction(self):
        result = calculator('2', 10, 5)
        self.assertEqual(result, 'Hasil operasi dari 10 - 5 = 5')

    def test_multiplication(self):
        result = calculator('3', 7, 6)
        self.assertEqual(result, 'Hasil operasi dari 7 * 6 = 42')

    def test_division(self):
        result = calculator('4', 20, 4)
        self.assertEqual(result, 'Hasil operasi dari 20 / 4 = 5.0')

    def test_division_by_zero(self):
        result = calculator('4', 10, 0)
        self.assertEqual(result, 'Pembagian oleh nol tidak diizinkan')

    def test_invalid_operation(self):
        result = calculator('5', 10, 5)
        self.assertEqual(result, 'Tidak valid')

if __name__ == '__main__':
    unittest.main()
