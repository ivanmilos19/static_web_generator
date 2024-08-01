import unittest
from textnode import TextNode

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

if __name__ == "__main__":
    unittest.main()