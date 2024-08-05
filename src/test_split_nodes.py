import unittest
from textnode import TextNode
from split_nodes import split_nodes_delimiter  

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is text with a `code block` word", "text")
        result = split_nodes_delimiter([node], "`", "code")
        
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        
        self.assertEqual(len(result), len(expected))
        for res_node, exp_node in zip(result, expected):
            self.assertEqual(res_node.text, exp_node.text)
            self.assertEqual(res_node.text_type, exp_node.text_type)
    
    def test_no_delimiter(self):
        node = TextNode("This has no delimiter", "text")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", "code")

    def test_multiple_delimiters(self):
        node1 = TextNode("Multiple delimiters like `code1` and `code2`", "text")
        result = split_nodes_delimiter([node1], "`", "code")

        expected = [
            TextNode("Multiple delimiters like ", "text"),
            TextNode("code1", "code"),
            TextNode(" and ", "text"),
            TextNode("code2", "code"),
        ]

        self.assertEqual(len(result), len(expected))
        for res_node, exp_node in zip(result, expected):
            self.assertEqual(res_node.text, exp_node.text)
            self.assertEqual(res_node.text_type, exp_node.text_type)

if __name__ == "__main__":
    unittest.main()