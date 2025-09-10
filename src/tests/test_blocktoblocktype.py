

from src.blocktoblocktype import block_to_block_type, BlockType
import unittest

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_unordered_list(self):
            block = "- This is a list\n- with items\n- multiple items\n- so many items"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.UNORDERED_LIST
            )
    def test_block_to_invalid_unordered_list(self):
            block = "- This is a list\n* with items\n- multiple items\n* so many items"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_block_to_one_item_unordered_list(self):
            block = "- This is a list with 1 item"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.UNORDERED_LIST
            )
    def test_block_to_ordered_list(self):
            block = "1. This is a list\n2. with items\n3. multiple items\n4. so many items"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.ORDERED_LIST
            )
    def test_block_to_out_of_order_ordered_list(self):
            block = "1. This is a list\n2. with items\n5. multiple items\n10. so many items"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_block_to_last_out_of_order_ordered_list(self):
            block = "1. This is a list\n2. with items\n3. multiple items\n10. so many items"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_block_to_one_item_ordered_list(self):
            block = "1. This is a list with 1 item"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.ORDERED_LIST
            )
    def test_block_to_quote(self):
            block = "> These are some quotes\n>with stuff\n>and things\n> so many quotes"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.QUOTE
            )
    def test_invalid_quote(self):
            block = "<This is a quote\ncAnother quote"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_single_quote(self):
            block = ">This is a single quote"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.QUOTE
            )
    def test_block_to_heading(self):
            block = "## This is a heading"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.HEADING
            )
    def test_block_to_heading2(self):
            block = "# This is a heading"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.HEADING
            )
    def test_invalid_heading(self):
            block = "######### This is an EXTREME heading"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_invalid_heading2(self):
            block = "##This is an EXTREME heading"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )
    def test_max_chars_heading(self):
            block = "###### This is a heading"
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.HEADING
            )
    

if __name__ == "__main__":
    unittest.main()