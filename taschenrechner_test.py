import unittest
from main import addieren, subtraktion, multiplizieren, dividieren

        
class test_taschenrechner(unittest.TestCase):
    def test_multiplikation(self):
        self.assertEqual(multiplizieren(10, 2), 20)
        self.assertEqual(multiplizieren(5, 3), 15)
        self.assertEqual(multiplizieren(4, 2.5), 10)
        
    def test_division(self):
        self.assertEqual(dividieren(10, 2), 5)
        self.assertEqual(dividieren(6, 3), 2)
        self.assertEqual(dividieren(4, 8), 0.5)
        self.assertEqual(dividieren(10, 0), "ERROR: division by zero")

    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtraktion(self):
        self.assertEqual(subtraktion(3, 3), 0)
        self.assertEqual(subtraktion(-1, 1), -2)
        self.assertEqual(subtraktion(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
