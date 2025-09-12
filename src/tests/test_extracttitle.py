import unittest
from src.extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title_extraction(self):
        md = """
# Hello
"""    
        title = extract_title(md)
        self.assertEqual(title, "Hello")
    def test_incorrect_title(self):
        md = """
## Hello
"""    
        with self.assertRaises(Exception):
            extract_title(md)
    
if __name__ == "__main__":
    unittest.main()

