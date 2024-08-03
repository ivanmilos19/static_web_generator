import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" ')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank" ')
    
class TestLeafNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode(value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_to_html_no_value(self):
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_single_prop(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" > href="https://www.google.com" <a>')

    def test_to_html_multiple_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank" > href="https://www.google.com" target="_blank" <a>')

if __name__ == "__main__":
    unittest.main()

