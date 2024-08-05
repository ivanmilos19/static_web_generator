import unittest
from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq_all_same(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold", "https://www.example.com")
        self.assertEqual(node, node2)

    def test_neq_different_text(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a different text node", "bold", "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_neq_different_text_type(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "italic", "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_neq_different_url(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold", "https://www.different.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_url_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_LeafNode_text(self):
        node = TextNode("This is a text node", "text", None)
        leaf = LeafNode(value="This is a text node")
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_LeafNode_bold(self):
        node = TextNode("This is a text node", "bold", None)
        leaf = LeafNode(tag="b", value="This is a text node")
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_LeafNode_italic(self):
        node = TextNode("This is a text node", "italic", None)
        leaf = LeafNode(tag="i", value="This is a text node")
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_LeafNode_code(self):
        node = TextNode("This is a text node", "code", None)
        leaf = LeafNode(tag="code", value="This is a text node")
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_LeafNode_link(self):
        node = TextNode("This is a text node", "link", "https://www.example.com")
        leaf = LeafNode(tag="a", value="This is a text node", props={"href": "https://www.example.com"})
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_LeafNode_image(self):
        node = TextNode("This is a text node", "image", "https://www.example.com")
        leaf = LeafNode(tag="img", value="", props={"src": "https://www.example.com", "alt": "This is a text node"})
        self.assertEqual(text_node_to_html_node(node).to_html(), leaf.to_html())

    def test_invalid_text_type(self):
        node = TextNode("This is a text node", "invalid", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()