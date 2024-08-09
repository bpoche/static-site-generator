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