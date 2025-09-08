from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        HTMLNode.__init__(self, tag, None, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("tag error")
        if not self.children or not all(isinstance(c, HTMLNode) for c in self.children ):
            raise ValueError("children error")
        result = ""
        for i in self.children:
            result = result + i.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"