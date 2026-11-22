import unittest
from app import Figure


class TestFigure(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(Figure("трикутник", 5).get_angles, 3)

    def test_square(self):
        self.assertEqual(Figure("квадрат", 5).get_angles, 4)

    def test_rectangle(self):
        self.assertEqual(Figure("прямокутник", 5).get_angles, 4)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)


if __name__ == "__main__":
    unittest.main()