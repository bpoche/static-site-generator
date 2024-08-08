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
        for node in old_nodes:
            split_list = node.text.split(delimiter)
            total_delim = len(split_list) - 1
            if total_delim == 0:
                new_nodes.append(node)
                continue
            cnt = 0
            if total_delim % 2 != 0:
                raise ValueError(f"Invalid markdown format - odd number of delimiter: {delimiter}")
            for item in split_list:
                if cnt % 2 == 0:
                    if item:
                        new_nodes.append(TextNode(text = item, text_type = text_type_text))
                else:
                    if delimiter == '*':
                        new_nodes.append(TextNode(text = item, text_type = text_type_italic))
                    elif delimiter == "**":
                        new_nodes.append(TextNode(text = item, text_type = text_type_bold))
                    elif delimiter == "`":
                        new_nodes.append(TextNode(text = item, text_type = text_type_code))
                cnt+=1
    if text_type == text_type_link:
        pass
    if text_type == text_type_image:
        pass
    return new_nodes