import unittest
from app import fatorial


class TestSimples(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(3), 6)
        self.assertEqual(fatorial(4), 24)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(6), 720)


if __name__ == '__main__':
    unittest.main()
