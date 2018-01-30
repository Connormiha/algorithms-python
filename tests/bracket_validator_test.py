import unittest
from src.bracket_validator import *

class TestStringMethods(unittest.TestCase):
    def test_is_valid_bracket(self):
        for item in [
            "()", "{}", "[]",
            "(())([])({}){}",
            "([{[()]}])",
            "",
        ]:
            self.assertTrue(is_valid_bracket(item))
        
        for item in [
            "()(", "(", ")(", ")", "{()]}",
            "((())))", "[]{}()(]",
        ]:
            self.assertFalse(is_valid_bracket(item))

if __name__ == '__main__':
    unittest.main()
