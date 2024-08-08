import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold, 
    text_type_italic, 
    text_type_code, 
    text_type_link, 
    text_type_image
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    old_nodes = old_nodes.copy()
    if text_type in [text_type_bold,text_type_italic,text_type_code]:
        for old_node in old_nodes:
            if old_node.text_type != text_type_text:
                new_nodes.append(old_node)
                continue
            split_nodes = []
            sections = old_node.text.split(delimiter)
            total_delim = len(sections) - 1
            if total_delim == 0:
                new_nodes.append(old_node)
                continue
            if total_delim % 2 != 0:
                raise ValueError("Invalid markdown format, formatted section not closed")
            for i in range(len(sections)):
                if i % 2 == 0:
                    if sections[i]:
                        split_nodes.append(TextNode(text = sections[i], text_type = text_type_text))
                else:
                    if sections[i]:
                        split_nodes.append(TextNode(text = sections[i], text_type = text_type))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        text_str = old_node.text
        for image in images:
            sections = text_str.split(f"![{image[0]}]({image[1]})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image sections are not closed")
            if sections[0]:
                new_nodes.append(TextNode(text=sections[0],text_type=text_type_text))
            new_nodes.append(TextNode(text=image[0],text_type=text_type_image,url=image[1]))
            text_str = sections[1]
        if text_str:
            new_nodes.append(TextNode(text=text_str,text_type=text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        text_str = old_node.text
        for link in links:
            sections = text_str.split(f"[{link[0]}]({link[1]})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image sections are not closed")
            if sections[0]:
                new_nodes.append(TextNode(text=sections[0],text_type=text_type_text))
            new_nodes.append(TextNode(text=link[0],text_type=text_type_link,url=link[1]))
            text_str = sections[1]
        if text_str:
            new_nodes.append(TextNode(text=text_str,text_type=text_type_text))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

def text_to_textnodes(text):
    node = TextNode(text=text, text_type='text')
    nodes = split_nodes_delimiter(old_nodes=[node], delimiter="**", text_type='bold')
    nodes = split_nodes_delimiter(old_nodes=nodes.copy(), delimiter="*", text_type='italic')
    nodes = split_nodes_delimiter(old_nodes=nodes.copy(), delimiter="`", text_type='code')
    nodes = split_nodes_image(old_nodes=nodes.copy())
    nodes = split_nodes_link(old_nodes=nodes.copy())
    return nodes
