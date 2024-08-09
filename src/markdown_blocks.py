import re
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node
from markdown_to_textnode import text_to_textnodes
from logger import logger

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    for block in markdown.split("\n\n"):
        if block.strip():
            blocks.append(block.strip())
    logger.debug(f"blocks: {blocks}")
    return blocks

def block_to_block_type(block: str) -> str:
    if re.match(r"^#{1,6} ", block):
        return 'heading'
    elif block.startswith("```") and block.endswith("```"):
        return 'code'
    elif block.startswith(">"):
        for line in block.split('\n'):
            if not line.startswith('>'):
                raise Exception("Invalid block quote")
        return 'quote'
    elif block.startswith('* '):
        for line in block.split('\n'):
            if not line.startswith('* '):
                raise Exception("Invalid block unordered list")
        return 'unordered_list'
    elif block.startswith('- '):
        for line in block.split('\n'):
            if not line.startswith('- '):
                raise Exception("Invalid block unordered list")
        return 'unordered_list'
    elif re.match(r"^1\. ", block):
        cnt = 1
        for line in block.split("\n"):
            if not re.match(rf"^{cnt}\. ", line):
                raise Exception("Invalid block ordered list")
            cnt += 1
        return "ordered_list"
    return "paragraph"

def text_to_children(text: str) -> list[HTMLNode]:
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        if html_node:
            html_nodes.append(html_node)
    return html_nodes

def markdown_to_html_node(markdown: str) -> HTMLNode:
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == 'heading':
            html_children = block_heading_to_html_children(block)
            if html_children:
                children.extend(html_children)
        if block_type == 'quote':
            html_children = block_quote_to_html_children(block)
            if html_children:
                children.extend(html_children)
        if block_type == 'code':
            html_children = block_code_to_html_children(block)
            if html_children:
                children.extend(html_children)
        if block_type == 'unordered_list':
            html_children = block_ul_to_html_children(block)
            if html_children:
                children.extend(html_children)
        if block_type == 'ordered_list':
            html_children = block_ol_to_html_children(block)
            if html_children:
                children.extend(html_children)
        if block_type == 'paragraph':
            html_children = block_p_to_html_children(block)
            if html_children:
                children.extend(html_children)
    return ParentNode(tag='div',children=children)

def block_heading_to_html_children(block):
    children = []
    for line in block.split('\n'):
        heading_num = len(line.split(' ')[0])
        node_children = text_to_children(line[heading_num+1:])
        if node_children:
            html_node = ParentNode(tag=f"h{heading_num}",children=node_children)
            children.append(html_node)
    return children


def block_quote_to_html_children(block):
    children = []
    for line in block.split('\n'):
        node_children = text_to_children(line[2:])
        if node_children:
            html_node = ParentNode(tag="blockquote",children=node_children)
            children.append(html_node)
    return children

def block_code_to_html_children(block):
    children = []
    lines = block.split('\n')
    lines[0] = lines[0][3:]
    lines[-1] = lines[-1][:-3]
    for line in lines:
        node_children = text_to_children(f"`{line}`")
        if node_children:
            children.extend(node_children)
    return [ParentNode(tag="pre",children=children)]

def block_ul_to_html_children(block):
    children = []
    for line in block.split('\n'):
        node_children = text_to_children(line[2:])
        if node_children:
            html_node = ParentNode(tag="li",children=node_children)
            children.append(html_node)
    return [ParentNode(tag='ul',children=children)]

def block_ol_to_html_children(block):
    children = []
    line_cnt = 1
    for line in block.split('\n'):
        node_children = text_to_children(line[3:])
        if node_children:
            html_node = ParentNode(tag="li",children=node_children)
            children.append(html_node)
    return [ParentNode(tag='ol',children=children)]

def block_p_to_html_children(block):
    block = block.replace("\n","<br>")
    children = text_to_children(block)
    return [ParentNode(tag="p",children=children)]

# markdown = '''### This is a heading
# #### this is another heading
# # one more heading
# '''

# markdown = '''> This is a quote
# > this is another quote
# > one more quote
# '''

# markdown = '''```print('howdy')
# print('parnter')```'''

# markdown = '''* this is a
# * unordered list
# * do you like it?'''

# markdown = '''1. this is a
# 2. ordered list
# 3. do you like it?'''

# markdown = '''this is a
# paragraph
# do you like it?'''

# markdown = '''# Tolkien Fan Club

# **I like Tolkien**. Read my [first post here](/majesty)

# > All that is gold does not glitter
# '''

# html_node = markdown_to_html_node(markdown)
# if html_node:
#     print(html_node.to_html())
#     logger.error(html_node.to_html())