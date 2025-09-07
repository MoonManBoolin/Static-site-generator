

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        result = ""
        if not self.props:
            return ""
        for item in self.props:
            result = result + f' {item}="{self.props[item]}"'
        return result
    def __eq__(self, node2):
        if self.tag == node2.tag and self.value == node2.value and self.children == node2.children and self.props == node2.props:
            return True
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"