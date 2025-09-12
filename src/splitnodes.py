from extractmarkdownlinks import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    result = []
    if not old_nodes:
        return "Error, no nodes"
    if len(old_nodes) == 1 and old_nodes[0].text_type != TextType.TEXT:
        return old_nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        node_result = []
        if not images:
            node_result.append(node)
        else:
            for alt, src in images:
                sections = node_text.split(f"![{alt}]({src})", 1)
                if sections[0] == "" and sections[1] != "" and extract_markdown_images(sections[1]):
                    node_text = sections[1]
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                elif sections[0] == "" and sections[1] != "" and not extract_markdown_images(sections[1]):
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                    node_result.append(TextNode(sections[1], TextType.TEXT))
                elif sections[0] != "" and sections[1] == "":
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                elif sections[0] == "" and sections[1] == "":
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                elif sections[0] != "" and sections[1] != "" and not extract_markdown_images(sections[1]):
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                    node_result.append(TextNode(sections[1], TextType.TEXT))
                elif sections[0] != "" and sections[1] != "" and extract_markdown_images(sections[1]):
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(alt, TextType.IMAGE, src))
                    node_text = sections[1]
        result.extend(node_result)
    return result
    
                        
def split_nodes_link(old_nodes):
    result = []
    if not old_nodes:
        return "Error, no nodes"
    if len(old_nodes) == 1 and old_nodes[0].text_type != TextType.TEXT:
        return old_nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)

        node_result = []
        if not links:
            node_result.append(node)
        else:
            for text_content, href in links:
                sections = node_text.split(f"[{text_content}]({href})", 1)
                if sections[0] == "" and sections[1] != "" and extract_markdown_links(sections[1]):
                    node_text = sections[1]
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                elif sections[0] == "" and sections[1] != "" and not extract_markdown_links(sections[1]):
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                    node_result.append(TextNode(sections[1], TextType.TEXT))
                elif sections[0] != "" and sections[1] == "":
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                elif sections[0] == "" and sections[1] == "":
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                elif sections[0] != "" and sections[1] != "" and not extract_markdown_links(sections[1]):
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                    node_result.append(TextNode(sections[1], TextType.TEXT))
                elif sections[0] != "" and sections[1] != "" and extract_markdown_links(sections[1]):
                    node_result.append(TextNode(sections[0], TextType.TEXT))
                    node_result.append(TextNode(text_content, TextType.LINK, href))
                    node_text = sections[1]
        result.extend(node_result)
    return result