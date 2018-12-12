import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 3), 6)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()
