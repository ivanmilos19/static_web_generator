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
    
def main():
    node = HTMLNode("p", "Hello, World!", None, {"href": "https://www.google.com", "target": "_blank",})
    print(node)

if __name__ == "__main__":
    main()
    