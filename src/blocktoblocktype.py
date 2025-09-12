from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(markdown_text_block):
    markdown_text_block = markdown_text_block.strip()
    if markdown_text_block.startswith("- "):
        correct_syntax = True
        for i in markdown_text_block.split("\n"):
            correct_syntax = False
            if i.startswith("- "):
                correct_syntax = True
        if correct_syntax:
            return BlockType.UNORDERED_LIST
    elif markdown_text_block.startswith("1. "):
        correct_syntax = True
        text_split = markdown_text_block.split("\n")
        count = 0
        for i in text_split:
            correct_syntax = False
            count += 1
            if i.startswith(f"{count}. "):
                correct_syntax = True
        if correct_syntax:
            return BlockType.ORDERED_LIST
    elif markdown_text_block.startswith(">"):
        correct_syntax = True
        for i in markdown_text_block.split("\n"):
            correct_syntax = False
            if i.startswith(">"):
                correct_syntax = True
        if correct_syntax:
            return BlockType.QUOTE
    elif markdown_text_block.startswith("```") and markdown_text_block.endswith("```"):
        return BlockType.CODE
    elif re.search(r"^#{1,6}\s.*", markdown_text_block):
        return BlockType.HEADING
    return BlockType.PARAGRAPH