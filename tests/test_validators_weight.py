import unittest
from validators import is_valid_weight

class TestValidators(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_weight(0.01))  # True weight
        self.assertTrue(is_valid_weight(0.02))  # True weight
        self.assertTrue(is_valid_weight(249.99))  # True weight
        self.assertFalse(is_valid_weight(350,1))  # False so fat 
        self.assertFalse(is_valid_weight(0))  # False so thin

if __name__ == '__main__':
    unittest.main()