from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type).value
        self.url = url
    def __eq__(self, node2):
        if self.text is node2.text and self.text_type is node2.text_type and self.url is node2.url:
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    