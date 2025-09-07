import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestTextNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_nested_grandchildren(self):
        grandchild_node1 = LeafNode("h1", "grandchild1")
        grandchild_node2 = LeafNode("h2", "grandchild2")
        inner_parent = ParentNode("div", [grandchild_node1, grandchild_node2])
        outer_parent = ParentNode("div", [inner_parent])
        self.assertEqual(
            outer_parent.to_html(),
            "<div><div><h1>grandchild1</h1><h2>grandchild2</h2></div></div>"
        )
    def test_to_html_with_no_children_in_array(self):
        child_node = None
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    def test_to_html_with_no_children(self):
        child_node = None
        parent_node = ParentNode("div", child_node)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("h1", "child1")
        child_node2 = LeafNode("p", "child2")
        child_node3 = LeafNode("a", "child3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><h1>child1</h1><p>child2</p><a>child3</a></div>")
if __name__ == "__main__":
    unittest.main()