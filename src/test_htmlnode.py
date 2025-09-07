import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "some text here", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "some text here", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode("p", "some text here", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "some text here", None, {"href": "https://www.bing.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_is_html_node(self):
        node = type(HTMLNode("p", "some text here", None, {"href": "https://www.google.com", "target": "_blank"}))
        node2 = type(HTMLNode("p", "some text here", None, {"href": "https://www.bing.com", "target": "_blank"}))
        self.assertEqual(node, node2)
    def test_is_not_html_node(self):
        node = type(HTMLNode("p", "some text here", None, {"href": "https://www.google.com", "target": "_blank"}))
        node2 = type(["p", "some text here", None, {"href": "https://www.bing.com", "target": "_blank"}])
        self.assertNotEqual(node, node2)
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Bing!", {"href": "https://www.bing.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.bing.com">Bing!</a>')
    def test_leaf_to_html_(self):
        node = LeafNode("img", "Bing! Here is an image!", {"src": "https://www.bing.com", "alt": "explaining the image here"})
        self.assertEqual(node.to_html(), '<img src="https://www.bing.com" alt="explaining the image here">Bing! Here is an image!</img>')
    def test_is_not_leaf_to_html_p(self):
        node = LeafNode("h1", "Hello, worlds!")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_is_not_leaf_to_html_a(self):
        node = LeafNode("link", "Bing!", {"href": "http://www.bing.com"})
        self.assertNotEqual(node.to_html(), '<a href="https://www.bing.com">Bing!</a>')
    def test_is_not_leaf_to_html_(self):
        node = LeafNode("image", "Bing! Here is an image!", {"src": "https://www.bing.com", "somthing": "explaining the image here"})
        self.assertNotEqual(node.to_html(), '<img src="https://www.bing.com" alt="explaining the image here">Bing! Here is an image!</img>')
if __name__ == "__main__":
    unittest.main()