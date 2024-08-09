import unittest
from markdown_blocks import markdown_to_blocks,block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_1(self):
        markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        '''
        expected = [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected,actual)

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading(self):
        block = "# This is a heading"
        expected = 'heading'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
        
    def test_heading_multiple_hashes(self):
        block = "### This is a level 3 heading"
        expected = 'heading'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_code_block(self):
        block = "```\ncode block\n```"
        expected = 'code'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_valid_block_quote(self):
        block = "> This is a block quote\n> spanning multiple lines"
        expected = 'quote'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_invalid_block_quote(self):
        block = "> This is a block quote\nThis is invalid"
        with self.assertRaises(Exception) as context:
            block_to_block_type(block)
        self.assertTrue('Invalid block quote' in str(context.exception))
    
    def test_valid_unordered_list_asterisk(self):
        block = "* Item 1\n* Item 2"
        expected = 'unordered_list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_invalid_unordered_list_asterisk(self):
        block = "* Item 1\n- Item 2"
        with self.assertRaises(Exception) as context:
            block_to_block_type(block)
        self.assertTrue('Invalid block unordered list' in str(context.exception))
    
    def test_valid_unordered_list_dash(self):
        block = "- Item 1\n- Item 2"
        expected = 'unordered_list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_invalid_unordered_list_dash(self):
        block = "- Item 1\n* Item 2"
        with self.assertRaises(Exception) as context:
            block_to_block_type(block)
        self.assertTrue('Invalid block unordered list' in str(context.exception))
    
    def test_valid_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = 'ordered_list'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)
    
    def test_invalid_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n4. Item 3"
        with self.assertRaises(Exception) as context:
            block_to_block_type(block)
        self.assertTrue('Invalid block ordered list' in str(context.exception))
    
    def test_paragraph(self):
        block = "This is a paragraph."
        expected = 'paragraph'
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_heading(self):
        markdown = '''### This is a heading'''
        expected_html = '<div><h3>This is a heading</h3></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_multiple_headings(self):
        markdown = '''### This is a heading\n#### this is another heading\n# one more heading'''
        expected_html = '<div><h3>This is a heading</h3><h4>this is another heading</h4><h1>one more heading</h1></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_block_quote(self):
        markdown = '''> This is a quote\n> this is another quote\n> one more quote'''
        expected_html = '<div><blockquote>This is a quote</blockquote><blockquote>this is another quote</blockquote><blockquote>one more quote</blockquote></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_code_block(self):
        markdown = '''```print('howdy')\nprint('partner')```'''
        expected_html = '<div><pre><code>print(\'howdy\')</code><code>print(\'partner\')</code></pre></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_unordered_list(self):
        markdown = '''* this is a\n* unordered list\n* do you like it?'''
        expected_html = '<div><ul><li>this is a</li><li>unordered list</li><li>do you like it?</li></ul></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_ordered_list(self):
        markdown = '''1. this is a\n2. ordered list\n3. do you like it?'''
        expected_html = '<div><ol><li>this is a</li><li>ordered list</li><li>do you like it?</li></ol></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_paragraph(self):
        markdown = '''this is a\nparagraph\ndo you like it?'''
        expected_html = '<div><p>this is a<br>paragraph<br>do you like it?</p></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)

    def test_combined_markdown(self):
        markdown = '''### This is a heading\n> This is a quote\n```\nprint('code')\n```\n* list item 1\n1. ordered item 1\nthis is a paragraph'''
        expected_html = '<div><h3>This is a heading</h3><blockquote>This is a quote</blockquote><pre><code>print(\'code\')</code></pre><ul><li>list item 1</li></ul><ol><li>ordered item 1</li></ol><p>this is a paragraph</p></div>'
        html_node = markdown_to_html_node(markdown)
        actual_html = html_node.to_html()
        self.assertEqual(expected_html, actual_html)