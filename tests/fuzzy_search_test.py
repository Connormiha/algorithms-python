import unittest
from src.fuzzy_search import *

class TestFuzzySearch(unittest.TestCase):
    def test_substrings(self):
        for item in [
            ("python", "ptn"),
            ("python1", "python"),
            ("java", "java"),
            ("ja va", "jaVa"),
            ("jaVa", "jAva"),
            ("javascript", ""),

        ]:
            self.assertTrue(fuzzy_search(*item))
        
        for item in [
            ("python", "ptnj"),
        ]:
            self.assertFalse(fuzzy_search(*item))

if __name__ == '__main__':
    unittest.main()
