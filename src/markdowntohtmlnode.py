from src.parentnode import ParentNode
from src.blocktoblocktype import BlockType
from src.markdowntoblocks import markdown_to_blocks
from src.blocktoblocktype import block_to_block_type
from src.texttonode import text_to_textnodes
from src.texttohtml import text_node_to_html_node
from src.leafnode import LeafNode
from src.textnode import TextNode, TextType
import re

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    result = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            children = []
            cleaned_block = block.replace("\n", " ")
            nodes = text_to_textnodes(cleaned_block)
            for node in nodes:
                children.append(text_node_to_html_node(node))
            result.append(ParentNode("p", children))
        elif block_type == BlockType.CODE:
            cleaned_block = block.strip("```")
            if cleaned_block.startswith("\n"):
                cleaned_block = cleaned_block[1:]
            code_node = LeafNode("code", cleaned_block)
            result.append(ParentNode("pre", [code_node]))
        elif block_type == BlockType.HEADING:
            h_num = re.match(r"^#{1,6}", block)
            cleaned_block = block.replace(h_num.group(0), "", 1).strip()
            heading_text_nodes = text_to_textnodes(cleaned_block.strip())
            children = [text_node_to_html_node(n) for n in heading_text_nodes]
            result.append(ParentNode(f"h{len(h_num.group(0))}", children))
        elif block_type == BlockType.ORDERED_LIST:
            items = re.findall(r"^\d\.\s(.*)", block, flags=re.MULTILINE)
            children = []
            for item in items:
                nodes = text_to_textnodes(item.strip())
                li_children = [text_node_to_html_node(n) for n in nodes]
                children.append(ParentNode("li", li_children))
            result.append(ParentNode("ol", children))
        elif block_type == BlockType.UNORDERED_LIST:
            items = re.findall(r"^-\s(.*)", block, flags=re.MULTILINE)
            children = []
            for item in items:
                nodes = text_to_textnodes(item.strip())
                li_children = [text_node_to_html_node(n) for n in nodes]
                children.append(ParentNode("li", li_children))
            result.append(ParentNode("ul", children))
        elif block_type == BlockType.QUOTE:
            items = re.findall(r"^>(.*)$", block, flags=re.MULTILINE)
            quote = ""
            for item in items:
                item = item.strip()
                if item == "":
                    quote = quote + "\n"
                if quote == "":
                    quote = item
                else:
                    quote = quote + " " + item
            nodes = text_to_textnodes(quote)
            bq_children = [text_node_to_html_node(n) for n in nodes]
            result.append(ParentNode("blockquote", bq_children))
    result = ParentNode("div", result)
    return result
    