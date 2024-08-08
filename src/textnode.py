from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    '''
    Intermediate representation of text (markdown->textnode->htmlnode)
    We're going to need a way to represent all the different types of inline text. 
    We're going to be parsing Markdown text, and outputting it to HTML, so we need an 
    intermediate representation of the text in our code.

    When I say "inline" I just mean text that is part of a larger block of text. For us, this includes:

    -Normal text
    -Bold text
    -Italic text
    -Code text
    -Links
    -Images

    Everything else we're considering block level, like headings, paragraphs, and bullet lists
    '''
    def __init__(self,text: str,text_type: str,url: str = None):
        self.text = text
        self.text_type = text_type #bold, italic, code, image, link 
        self.url = url

    def __eq__(self,TextNode):
        if (
            self.text == TextNode.text and
            self.text_type == TextNode.text_type and
            self.url == TextNode.url
        ):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == text_type_text:
        return LeafNode(tag = None, value = text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode(tag = "b", value = text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode(tag = "i", value = text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode(tag = "code", value = text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode(tag = "a", value = text_node.text, props = {"href":text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode(tag = "img", value = "", props = {"src":text_node.url,"alt":text_node.text})
    raise Exception(f"Invalid text type: {text_node.text_type}")
