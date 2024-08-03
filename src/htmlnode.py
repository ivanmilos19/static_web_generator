class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            html = ""
            for key, value in self.props.items():
                html += f'{key}="{value}" '
            return html 
        return ""
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{(' ' + self.props_to_html()) if self.props else ''}>{self.value}</{self.tag}>"
            
            

    
def main():
    # node = HTMLNode("p", "Hello, World!", None, {"href": "https://www.google.com", "target": "_blank",})
    # print(node)
    node = LeafNode("p", "This is a paragraph of text.")
    print(node.to_html())

if __name__ == "__main__":
    main()  