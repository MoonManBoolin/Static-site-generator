import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("is a text node?", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("is a text node?", TextType.LINK, "http://google.com")
        self.assertNotEqual(node, node2)
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "http://freecodecamp.org")
        node2 = TextNode("This is a text node", TextType.LINK, "https://freecodecamp.org")
        self.assertNotEqual(node, node2)
    def test_link_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_no_text(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node, node2)
if __name__ == "__main__":
    unittest.main()