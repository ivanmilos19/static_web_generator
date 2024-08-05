from htmlnode import HTMLNode, LeafNode, ParentNode

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    if text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid text type")
    

def main():
    test = TextNode("This is a text node", "text", None)
    print(text_node_to_html_node(test).to_html())

if __name__ == "__main__":
    main()