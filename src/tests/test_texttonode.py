from src.texttonode import text_to_textnodes
from src.textnode import TextNode, TextType

import unittest

class TestTextToNode(unittest.TestCase):
    def test_text_to_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            node_list,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )
    def test_bold_at_start_italic_at_end(self):
        text = "**Bold** middle _italic_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("Bold", TextType.BOLD),
                TextNode(" middle ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
        )
    def test_code_protects_inner_markup(self):
        text = "Start `code **bold** _it_` end"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("code **bold** _it_", TextType.CODE),
                TextNode(" end", TextType.TEXT),
            ],
        )
    def test_italic_not_parsed_inside_bold(self):
        text = "**bold _italic_ still bold**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("bold _italic_ still bold", TextType.BOLD),
            ],
        )
    def test_multiple_code_and_markup_segments(self):
        text = "`one` **bold** text `two` _it_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("one", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text ", TextType.TEXT),
                TextNode("two", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("it", TextType.ITALIC),
            ],
        )
    def test_image_then_bold_no_space(self):
        text = "![alt](https://img)x**B**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("alt", TextType.IMAGE, "https://img"),
                TextNode("x", TextType.TEXT),
                TextNode("B", TextType.BOLD),
            ],
        )
    def test_image_immediately_followed_by_bold(self):
        text = "![alt](https://img)**B**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("alt", TextType.IMAGE, "https://img"),
                TextNode("B", TextType.BOLD),
            ],
        )
    def test_link_followed_by_italic_no_space(self):
        text = "[site](https://x)_it_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("site", TextType.LINK, "https://x"),
                TextNode("it", TextType.ITALIC),
            ],
        )
    def test_link_then_bold_then_italic_chain(self):
        text = "[a](u)**B**_i_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("a", TextType.LINK, "u"),
                TextNode("B", TextType.BOLD),
                TextNode("i", TextType.ITALIC),
            ],
        )
    def test_trailing_text_after_bold(self):
        text = "Text **B** end"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("B", TextType.BOLD),
                TextNode(" end", TextType.TEXT),
            ],
        )
if __name__ == "__main__":
    unittest.main()