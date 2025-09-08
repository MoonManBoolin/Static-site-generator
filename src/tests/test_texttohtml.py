from src.textnode import *
from src.htmlnode import *
from src.texttohtml import *
import unittest

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_wrong_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "redirect")
    def test_bold(self):
        node = TextNode("bold!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold!")
    def test_italic(self):
        node = TextNode("italic!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic!")
    def test_code(self):
        node = TextNode("code!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "code!")
    def test_link(self):
        node = TextNode("link!", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link!")
        self.assertEqual(html_node.props["href"], "https://www.google.com")
    def test_image(self):
        node = TextNode("image!", TextType.IMAGE, "https://www.google.com/image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "image!")
        self.assertEqual(html_node.props["src"], "https://www.google.com/image")
    
if __name__ == "__main__":
    unittest.main()


