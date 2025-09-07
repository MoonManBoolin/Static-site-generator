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
    def __eg__(self, textnode1, textnode2):
        if textnode1.text == textnode2.text and textnode1.text_type == textnode2.text_type and textnode1.url == textnode2.url:
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    