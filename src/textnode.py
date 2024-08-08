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
    
def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://boot.dev"
    textnode = TextNode(text,text_type,url)
    print(textnode)

if __name__ == "__main__":
    main()
   


