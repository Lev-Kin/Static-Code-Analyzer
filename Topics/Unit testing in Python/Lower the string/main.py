import unittest

def string_to_lower(s):
    if not isinstance(s, str):
        raise ValueError("Input is not a string")
    return s.lower()

class TestStringToLower(unittest.TestCase):
    def test_string_to_lower(self):
        # Testing for an exception using assertRaises
        self.assertRaises(ValueError, string_to_lower, 123)
        self.assertRaises(ValueError, string_to_lower, True)
        self.assertRaises(ValueError, string_to_lower, None)
        self.assertRaises(ValueError, string_to_lower, [1, 2, 3])

        # Testing for an exception using context manager
        with self.assertRaises(ValueError):
            string_to_lower(123)
        with self.assertRaises(ValueError):
            string_to_lower(True)
        with self.assertRaises(ValueError):
            string_to_lower(None)
        with self.assertRaises(ValueError):
            string_to_lower([1, 2, 3])

if __name__ == '__main__':
    unittest.main()