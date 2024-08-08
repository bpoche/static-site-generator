import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Test Nodery","bold")
        node2 = TextNode("Test Nodery","bold")
        self.assertEqual(node1,node2)

    def test_neq(self):
        node1 = TextNode("Test nodery","bold")
        node2 = TextNode("Test Nodery","italic")
        self.assertNotEqual(node1,node2)

    def test_url(self):
        url = "https://blah.com"
        node = TextNode("Test no url","bold",url)
        actual = node.url
        self.assertEqual(url,actual)

    def test_url_none(self):
        node = TextNode("Test no url","bold")
        expected = None
        actual = node.url
        self.assertEqual(expected,actual)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_bold(self):
        node1 = text_node_to_html_node(TextNode(text="Text",text_type="bold"))
        node2 = LeafNode(tag="b",value="Text")
        self.assertEqual(node1,node2)
    def test_italic(self):
        node1 = text_node_to_html_node(TextNode(text="Text",text_type="italic"))
        node2 = LeafNode(tag="i",value="Text")
        self.assertEqual(node1,node2)
    def test_code(self):
        node1 = text_node_to_html_node(TextNode(text="Text",text_type="code"))
        node2 = LeafNode(tag="code",value="Text")
        self.assertEqual(node1,node2)
    def test_link(self):
        node1 = text_node_to_html_node(TextNode(text="Anchor Text",text_type="link",url="https://blah.com"))
        node2 = LeafNode(tag="a",value="Anchor Text",props={"href":"https://blah.com"})
        self.assertEqual(node1,node2)
    def test_image(self):
        node1 = text_node_to_html_node(TextNode(text="Alt Text",text_type="image",url="https://blah.com"))
        node2 = LeafNode(tag="img",value="",props={"src":"https://blah.com","alt":"Alt Text"})
        self.assertEqual(node1,node2)