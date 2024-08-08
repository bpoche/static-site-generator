import unittest
from textnode import TextNode
from markdown_to_textnode import split_nodes_delimiter

class TestMarkdownToTextNode(unittest.TestCase):
    def test_bold_middle(self):
        md_str = "This is text with a **bolded phrase** in the middle"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text with a ", text_type = "text"),
            TextNode(text="bolded phrase", text_type = "bold"),
            TextNode(text=" in the middle", text_type = "text"),
        ]
        actual = split_nodes_delimiter(old_nodes, "**", 'bold')
        self.assertEqual(expected,actual)

    def test_bold_start(self):
        md_str = "**bolded phrase** at the start"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="bolded phrase", text_type = "bold"),
            TextNode(text=" at the start", text_type = "text")
        ]
        actual = split_nodes_delimiter(old_nodes, "**", 'bold')
        self.assertEqual(expected,actual)

    def test_bold_end(self):
        md_str = "This is text ends with a **bolded phrase**"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text ends with a ", text_type = "text"),
            TextNode(text="bolded phrase", text_type = "bold")
        ]
        actual = split_nodes_delimiter(old_nodes, "**", 'bold')
        self.assertEqual(expected,actual)
    def test_italic_middle(self):
        md_str = "This is text with a *italiced phrase* in the middle"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text with a ", text_type = "text"),
            TextNode(text="italiced phrase", text_type = "italic"),
            TextNode(text=" in the middle", text_type = "text"),
        ]
        actual = split_nodes_delimiter(old_nodes, "*", 'italic')
        self.assertEqual(expected,actual)

    def test_italic_start(self):
        md_str = "*italiced phrase* at the start"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="italiced phrase", text_type = "italic"),
            TextNode(text=" at the start", text_type = "text")
        ]
        actual = split_nodes_delimiter(old_nodes, "*", 'italic')
        self.assertEqual(expected,actual)

    def test_italic_end(self):
        md_str = "This is text ends with a *italiced phrase*"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text ends with a ", text_type = "text"),
            TextNode(text="italiced phrase", text_type = "italic")
        ]
        actual = split_nodes_delimiter(old_nodes, "*", 'italic')
        self.assertEqual(expected,actual)
    def test_code_middle(self):
        md_str = "This is text with a `code block` in the middle"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text with a ", text_type = "text"),
            TextNode(text="code block", text_type = "code"),
            TextNode(text=" in the middle", text_type = "text"),
        ]
        actual = split_nodes_delimiter(old_nodes, "`", 'code')
        self.assertEqual(expected,actual)

    def test_code_start(self):
        md_str = "`code block` at the start"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="code block", text_type = "code"),
            TextNode(text=" at the start", text_type = "text")
        ]
        actual = split_nodes_delimiter(old_nodes, "`", 'code')
        self.assertEqual(expected,actual)

    def test_code_end(self):
        md_str = "This is text ends with a `code block`"
        old_nodes = [TextNode(text = md_str,text_type = "text")]
        expected = [
            TextNode(text="This is text ends with a ", text_type = "text"),
            TextNode(text="code block", text_type = "code")
        ]
        actual = split_nodes_delimiter(old_nodes, "`", 'code')
        self.assertEqual(expected,actual)