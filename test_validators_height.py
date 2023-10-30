import unittest
from validators import is_valid_height

class TestValidators(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_height(10))  # True height
        self.assertTrue(is_valid_height(250))  # True height
        self.assertTrue(is_valid_height(249.99))  # True height
        self.assertFalse(is_valid_height(251))  # False so long 
        self.assertFalse(is_valid_height(9))  # False so short

if __name__ == '__main__':
    unittest.main()