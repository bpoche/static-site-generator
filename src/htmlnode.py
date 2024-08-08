import functools

class HTMLNode():
    '''
    HTMLNode class will represent a "node" in an HTML document tree 
    (like a <p> tag and its contents, or an <a> tag and its contents) 
    and is purpose-built to render itself as HTML.
    '''
    def __init__(self,tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children.copy() if children else []
        self.props = props.copy() if props else {}

    def __eq__(self,other):
        if not isinstance(other,HTMLNode):
            return False
        if (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        ):
            return True
        return False

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        html_str = functools.reduce(lambda acc,item: f'{acc} {item[0]}="{item[1]}"',self.props.items(),"")
        return html_str
    
class LeafNode(HTMLNode):
    '''
    LeafNode is a type of HTMLNode that represents a single HTML tag with no children. 
    For example, a simple <p> tag with some text inside of it:
    '''
    def __init__(self,tag: str = None, value: str = None, props: dict = None):
        if not value:
            raise ValueError("Value is required for all LeafNodes")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    '''
    ParentNode class will handle the nesting of HTML nodes inside of one another. 
    Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
    '''
    def __init__(self,tag: str = None, children: list = None, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided for ParentNode")
        if not self.children:
            raise ValueError("Children are required for all ParentNodes")
        html_children =  functools.reduce(lambda acc,item: acc + f"{item.to_html()}",self.children,"")
        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"