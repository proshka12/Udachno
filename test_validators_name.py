import unittest
from validators import is_valid_name

class TestValidators(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_name("John"))  # True name
        self.assertTrue(is_valid_name("Alice123"))  # True name
        self.assertTrue(is_valid_name("Bob_25"))  # True name
        self.assertFalse(is_valid_name("Jo"))  # So short
        self.assertFalse(is_valid_name("ThisIsAVeryLongNameWithMoreThan20Characters"))  # So long

if __name__ == '__main__':
    unittest.main()