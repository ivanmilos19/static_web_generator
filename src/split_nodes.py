from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue  

        parts = node.text.split(delimiter)
        if len(parts) < 2:
            raise Exception('Delimiter not found')
        
        for index, part in enumerate(parts):
            if part == "":
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(part, "text"))
            else:
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes

def main():
    node1 = TextNode("Multiple delimiters like `code1` and `code2`", "text")
    new_nodes = split_nodes_delimiter([node1], "`", "code")
    for n in new_nodes:
        print(f"text: {n}\n")

if __name__ == "__main__":
    main()