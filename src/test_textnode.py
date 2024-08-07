import unittest

from textnode import TextNode

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