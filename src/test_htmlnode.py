import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("b","testing")
        node2 = HTMLNode("b","testing")
        self.assertEqual(node1,node2)
    def test_neq(self):
        node1 = HTMLNode("b","testing")
        node2 = HTMLNode("i","testing")
        self.assertNotEqual(node1,node2)
    def test_children(self):
        children = [HTMLNode("i","testing")]
        node = HTMLNode("b","testing",children)
        actual = node.children
        self.assertEqual(children,actual)
    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("b","testing",props=props)
        actual = node.props
        self.assertEqual(props,actual)
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("b","testing",None,props=props)
        actual = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected,actual)