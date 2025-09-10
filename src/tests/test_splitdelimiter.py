from src.splitdelimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType
import unittest

class TestTextNode(unittest.TestCase):
    def test_code_split_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),])
    def test_bold_split_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT),])
    def test_italic_split_delimiter(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),])
    def test_no_split_delimiter_in_text(self):
        node = TextNode("This is text with no split word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with no split word", TextType.TEXT)])
    def test_non_text_node_in_list(self):
        node1 = TextNode("This is *italic*", TextType.TEXT)
        node2 = TextNode("Already italic", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node1, node2], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode("Already italic", TextType.ITALIC),])
    def test_multiple_delimiter_pairs(self):
        node = TextNode("A `code` and `more code` here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("A ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" and ", TextType.TEXT), TextNode("more code", TextType.CODE), TextNode(" here", TextType.TEXT),])
    def test_adjacent_delimiters(self):
        node = TextNode("**bold****bold2**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("bold", TextType.BOLD), TextNode("bold2", TextType.BOLD),])
    def test_unmatched_split_delimiter_in_text(self):
        node = TextNode("This is text with an *unmatched split word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)
if __name__ == "__main__":
    unittest.main()