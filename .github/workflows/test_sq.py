import unittest
from sq import square

class TestSquareFunction(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(5), 25)

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_negative(self):
        self.assertEqual(square(-3), 9)

if __name__ == '__main__':
    unittest.main()
