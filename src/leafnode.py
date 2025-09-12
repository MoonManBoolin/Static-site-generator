from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        HTMLNode.__init__(self, tag, value, None, props)
    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError
            return self.value
        props = self.props_to_html() if self.props else ""
        if self.tag == "img":
            return f"<{self.tag}{props} />"
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"