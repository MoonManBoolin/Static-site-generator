from src.textnode import *
from src.splitnodes import *
import unittest

class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://a.example) and another [second link](https://b.example)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://a.example"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://b.example"),
            ],
            new_nodes,
        )
    def test_no_links(self):
        node = TextNode("Just plain text, no links here.", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))
    def test_link_at_start(self):
        node = TextNode("[start](u1) begins the line", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.LINK, "u1"),
                TextNode(" begins the line", TextType.TEXT),
            ],
            out,
        )
    def test_link_at_end(self):
        node = TextNode("Ends with a [final](u2)", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Ends with a ", TextType.TEXT),
                TextNode("final", TextType.LINK, "u2"),
            ],
            out,
        )
    def test_multiple_adjacent_links(self):
        node = TextNode("[one](u1)[two](u2)[three](u3)", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.LINK, "u1"),
                TextNode("two", TextType.LINK, "u2"),
                TextNode("three", TextType.LINK, "u3"),
            ],
            out,
        )
    def test_non_text_node(self):
        node = TextNode("already", TextType.LINK, "uZ")
        self.assertListEqual([node], split_nodes_link([node]))
    def test_mixed_nodes_one_with_links(self):
        n1 = TextNode("Alpha [l1](u1) beta", TextType.TEXT)
        n2 = TextNode("Gamma delta (no links here)", TextType.TEXT)
        out = split_nodes_link([n1, n2])
        self.assertListEqual(
            [
                TextNode("Alpha ", TextType.TEXT),
                TextNode("l1", TextType.LINK, "u1"),
                TextNode(" beta", TextType.TEXT),
                TextNode("Gamma delta (no links here)", TextType.TEXT),
            ],
            out,
        )
    def test_interleaved_links_trailing_text(self):
        node = TextNode("Start [a](u1) mid [b](u2) end", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("a", TextType.LINK, "u1"),
                TextNode(" mid ", TextType.TEXT),
                TextNode("b", TextType.LINK, "u2"),
                TextNode(" end", TextType.TEXT),
            ],
            out,
        )
    def test_adjacent_links_no_empty_text_nodes(self):
        node = TextNode("[one](u1)[two](u2)", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.LINK, "u1"),
                TextNode("two", TextType.LINK, "u2"),
            ],
            out,
        )
    def test_non_text_nodes_passthrough(self):
        link_node = TextNode("existing", TextType.LINK, "uX")
        txt_node = TextNode("Prefix [a](u1)", TextType.TEXT)
        out = split_nodes_link([link_node, txt_node])
        self.assertListEqual(
            [
                link_node,
                TextNode("Prefix ", TextType.TEXT),
                TextNode("a", TextType.LINK, "u1"),
            ],
            out,
        )
    def test_images_unchanged_with_links(self):
        node = TextNode("See [link](https://x.y) and ![logo](img.png)", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("See ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://x.y"),
                TextNode(" and ![logo](img.png)", TextType.TEXT),
            ],
            out,
        )
    def test_long_link_text_and_url(self):
        txt = "very-long_text-123_XYZ"
        url = "https://example.com/path/to/resource-v1.2.3.html?query=1&x=2"
        node = TextNode(f"[{txt}]({url})", TextType.TEXT)
        out = split_nodes_link([node])
        self.assertListEqual(
            [TextNode(txt, TextType.LINK, url)],
            out,
        )
    def test_multiple_nodes_no_links(self):
        nodes = [
            TextNode("First block.", TextType.TEXT),
            TextNode("Second block.", TextType.TEXT),
        ]
        out = split_nodes_link(nodes)
        self.assertListEqual(nodes, out)
    def test_empty_input_list_links(self):
        out = split_nodes_link([])
        self.assertEqual("Error, no nodes", out)

if __name__ == "__main__":
    unittest.main()
