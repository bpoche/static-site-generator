import functools

class HTMLNode():
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
    def __init__(self,tag: str = None, value: str = None, props: dict = None):
        if not value:
            raise ValueError("Value is required for all LeafNodes")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"