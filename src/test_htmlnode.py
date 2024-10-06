import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("p", "This is a test node")
        node2 = HTMLNode("p", "This is a test node")
        
        self.assertEqual(node, node2)
    
    def test_props(self):
        node = HTMLNode("p", "This is a test node")
        node2 = HTMLNode("p", "This is a test node")
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_repr(self):
        node = HTMLNode("p", "This is a test node")
        self.assertEqual(
        "HTMLNode(p, This is a test node, None, None)", repr(node))

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parentnode(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")

    def test_parentnode_nested(self):
        node = ParentNode("h", [ParentNode("p", [LeafNode("b", "bold text"), LeafNode("i", "italic text")])])
        self.assertEqual(node.to_html(), "<h><p><b>bold text</b><i>italic text</i></p></h>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    
if __name__ == "__main__":
    unittest.main()


