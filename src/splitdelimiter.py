from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            result.append(node)
        elif delimiter in node.text:
            raw = node.text.split(delimiter)
            if len(raw) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            for index, chunk in enumerate(raw):
                if index % 2 == 0:
                    if chunk:
                        result.append(TextNode(chunk, TextType.TEXT))
                else:
                    result.append(TextNode(chunk, text_type))
    return result

#split_nodes_delimiter([TextNode("This is text with a `code block` word. Watch out, another `code block` word!", TextType.TEXT)], "`", TextType.CODE)