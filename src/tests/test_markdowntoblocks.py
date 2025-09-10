

from src.markdowntoblocks import markdown_to_blocks
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    def test_single_paragraph_no_split(self):
        md = "Single paragraph only"
        self.assertEqual(markdown_to_blocks(md), ["Single paragraph only"])

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_only_newlines(self):
        self.assertEqual(markdown_to_blocks("\n\n\n"), [])

    def test_trailing_blank_lines(self):
        md = """
Paragraph one

Paragraph two

"""
        self.assertEqual(
            markdown_to_blocks(md),
            ["Paragraph one", "Paragraph two"],
        )

    def test_leading_blank_lines(self):
        md = """

- a
- b
- c
"""
        self.assertEqual(
            markdown_to_blocks(md),
            ["- a\n- b\n- c"],
        )

    def test_multiple_consecutive_blank_separators(self):
        md = """
Para one


Para two



Para three
"""
        self.assertEqual(
            markdown_to_blocks(md),
            ["Para one", "Para two", "Para three"],
        )

    def test_spaces_around_paragraphs(self):
        md = "First paragraph   \n\n   Second ones"
        self.assertEqual(
            markdown_to_blocks(md),
            ["First paragraph", "Second ones"],
        )
if __name__ == "__main__":
    unittest.main()