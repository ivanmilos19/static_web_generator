import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" >Click me!</a>')

    def test_to_html_multiple_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank" >Click me!</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = ParentNode(children=[LeafNode(value="This is a paragraph of text.")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_single_child(self):
        node = ParentNode(tag="p", children=[LeafNode(value="This is a paragraph of text.")])
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_multiple_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(value="This is a paragraph of text."),
                LeafNode(value="This is another paragraph of text."),
            ]
        )
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.This is another paragraph of text.</p>")
    
    def test_to_html_nested_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(value="This is a paragraph of text."),
                ParentNode(
                    tag="div",
                    children=[
                        LeafNode(value="This is a paragraph of text."),
                        LeafNode(value="This is another paragraph of text."),
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.<div>This is a paragraph of text.This is another paragraph of text.</div></p>")

    def test_to_html_nested_children2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "div",
                    [
                        LeafNode("i", "Italic text within div"),
                        LeafNode(None, "Some more text"),
                    ]
                ),
                LeafNode("i", "Italic text outside div"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b><div><i>Italic text within div</i>Some more text</div><i>Italic text outside div</i></p>")
            

if __name__ == "__main__":
    unittest.main()

