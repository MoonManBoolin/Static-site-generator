from src.extractmarkdownlinks import *
import unittest

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll]a(https://i.imgur.com/aKaOqIh.gif) and ![[obi wan]sadf(https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertEqual([], matches)
    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev]asdf(https://www.boot.dev) and [to youtube]asdf(https://www.youtube.com/@bootdotdev))"
        )
        self.assertEqual([], matches)
if __name__ == "__main__":
    unittest.main()