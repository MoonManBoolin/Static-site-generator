from src.textnode import *
from src.splitnodes import *
import unittest

class TestTextNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_no_images(self):
        node = TextNode("Just plain text, no images here.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    def test_image_at_start(self):
        node = TextNode("![img](url) starts the text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img", TextType.IMAGE, "url"),
                TextNode(" starts the text", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_image_at_end(self):
        node = TextNode("Ends with an image ![img](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Ends with an image ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "url"),
            ],
            new_nodes,
        )
    def test_multiple_adjacent_images(self):
        node = TextNode("![one](url1)![two](url2)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.IMAGE, "url1"),
                TextNode("two", TextType.IMAGE, "url2"),
            ],
            new_nodes,
        )
    def test_non_text_node(self):
        node = TextNode("![img](url)", TextType.IMAGE, "url")
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    def test_mixed_nodes_one_with_images(self):
        n1 = TextNode("Alpha ![img1](u1) beta", TextType.TEXT)
        n2 = TextNode("Gamma delta (no images here)", TextType.TEXT)
        out_nodes = split_nodes_image([n1, n2])
        self.assertListEqual(
            [
                TextNode("Alpha ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "u1"),
                TextNode(" beta", TextType.TEXT),
                TextNode("Gamma delta (no images here)", TextType.TEXT),
            ],
            out_nodes,
        )
    def test_interleaved_images_trailing_text(self):
        node = TextNode("Start ![a](u1) mid ![b](u2) end", TextType.TEXT)
        out_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("a", TextType.IMAGE, "u1"),
                TextNode(" mid ", TextType.TEXT),
                TextNode("b", TextType.IMAGE, "u2"),
                TextNode(" end", TextType.TEXT),
            ],
            out_nodes,
        )
    def test_adjacent_images_no_empty_text_nodes(self):
        node = TextNode("![one](u1)![two](u2)![three](u3)", TextType.TEXT)
        out_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.IMAGE, "u1"),
                TextNode("two", TextType.IMAGE, "u2"),
                TextNode("three", TextType.IMAGE, "u3"),
            ],
            out_nodes,
        )
    def test_non_text_nodes_passthrough(self):
        img_node = TextNode("alt", TextType.IMAGE, "uX")
        txt_node = TextNode("Prefix ![a](u1)", TextType.TEXT)
        out_nodes = split_nodes_image([img_node, txt_node])
        self.assertListEqual(
            [
                img_node,
                TextNode("Prefix ", TextType.TEXT),
                TextNode("a", TextType.IMAGE, "u1"),
            ],
            out_nodes,
        )
    def test_links_unchanged_with_images(self):
        node = TextNode("See ![logo](img.png) and [link](https://x.y)", TextType.TEXT)
        out_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("See ", TextType.TEXT),
                TextNode("logo", TextType.IMAGE, "img.png"),
                TextNode(" and [link](https://x.y)", TextType.TEXT),
            ],
            out_nodes,
        )
    def test_long_alt_and_url(self):
        long_alt = "very-long_alt-123_XYZ"
        long_url = "https://example.com/assets/images/path/to/file-name_v1.2.3.png?query=1&x=2"
        node = TextNode(f"![{long_alt}]({long_url})", TextType.TEXT)
        out_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode(long_alt, TextType.IMAGE, long_url)],
            out_nodes,
        )
    def test_multiple_nodes_no_images(self):
        nodes = [
            TextNode("First block.", TextType.TEXT),
            TextNode("Second block.", TextType.TEXT),
        ]
        out_nodes = split_nodes_image(nodes)
        self.assertListEqual(nodes, out_nodes)
    def test_empty_input_list(self):
        out = split_nodes_image([])
        self.assertEqual("Error, no nodes", out)
        
if __name__ == "__main__":
    unittest.main()


