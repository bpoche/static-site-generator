import unittest

from htmlnode import HTMLNode, LeafNode

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

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode(tag="b", value="testing")
        node2 = LeafNode(tag="b", value="testing")
        self.assertEqual(node1,node2)
    
    def test_neq(self):
        node1 = LeafNode(tag="b", value="testing")
        node2 = LeafNode(tag="i", value="testing")
        self.assertNotEqual(node1,node2)

    # Leaf nodes must have a value, check that an exception is raised if no value is provided
    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="b")

    def test_to_html(self):
        node = LeafNode("b","testing")
        actual = node.to_html()
        expected = "<b>testing</b>"
        self.assertEqual(expected,actual)

    def test_to_html_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a","Google",props)
        actual = node.to_html()
        expected = '<a href="https://www.google.com" target="_blank">Google</a>'
        self.assertEqual(expected,actual)

    def test_to_html_no_tag(self):
        node = LeafNode(None,"testing")
        actual = node.to_html()
        expected = "testing"
        self.assertEqual(expected,actual)

        