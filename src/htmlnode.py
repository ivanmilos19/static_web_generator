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
            
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag argument")
        elif self.children is None:
            raise ValueError("missing children argument")
        
        html_elemt = f"<{self.tag}>"
        for node in self.children:
            html_elemt += f"{node.to_html()}"
        html_elemt += f"</{self.tag}>"
        
        return html_elemt
        
            

    
def main():
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

    print(node.to_html())

if __name__ == "__main__":
    main()  