from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        HTMLNode.__init__(self, tag, value, None, props)
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html() if self.props else ""}>{self.value}</{self.tag}>"