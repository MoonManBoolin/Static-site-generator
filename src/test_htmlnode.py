import unittest

from htmlnode import HTMLNode

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
if __name__ == "__main__":
    unittest.main()