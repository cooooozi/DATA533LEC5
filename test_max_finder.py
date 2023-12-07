import unittest
from max_finder import find_max
class TestMaxFinder(unittest.TestCase):
    
    def test_max_with_positive_numbers(self):
        self.assertEqual(find_max(10, 20), 20, "Should be 20")
    
    def test_max_with_negative_numbers(self):
        self.assertEqual(find_max(-10, -20), -10, "Should be -10")
    
    def test_max_with_equal_numbers(self):
        self.assertEqual(find_max(15, 15), 15, "Should be 15")

    def test_max_with_positive_and_negative(self):
        self.assertEqual(find_max(-5, 5), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()

