import functools

class HTMLNode():
    def __init__(self,tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children.copy() if children else None
        self.props = props.copy() if props else None

    def __eq__(self,HTMLNode):
        if (
            self.tag == HTMLNode.tag and
            self.value == HTMLNode.value and
            self.children == HTMLNode.children and
            self.props == HTMLNode.props
        ):
            return True
        return False

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_str = functools.reduce(lambda acc,item: f'{acc} {item[0]}="{item[1]}"',self.props.items(),"")
        return html_str
    