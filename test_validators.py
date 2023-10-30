import unittest
from validators import is_valid_name

class TestValidators(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_name("Sasha"))  # True name
        self.assertTrue(is_valid_name("Sasha123"))  # True name
        self.assertTrue(is_valid_name("Alex_25"))  # True name
        self.assertFalse(is_valid_name("Ja"))  # So short
        self.assertFalse(is_valid_name("ThisIsAVeryLongNameWithMoreThan20Characters"))  # So long

if __name__ == '__main__':
    unittest.main()