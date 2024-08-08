import unittest
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold, 
    text_type_italic, 
    text_type_code, 
    text_type_link, 
    text_type_image
)
from markdown_to_textnode import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

class TestSplitNodesDelimiter(unittest.TestCase):
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

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected,actual)
    def test_no_images(self):
        text = "This is text with no images."
        expected = []
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
    def test_image_without_alt_text(self):
        text = "Here is an image ![](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("", "https://i.imgur.com/aKaOqIh.gif")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
    def test_image_with_special_characters_in_alt_text(self):
        text = "Check this out ![rick & morty](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("rick & morty", "https://i.imgur.com/aKaOqIh.gif")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
    def test_multiple_images_same_url(self):
        text = "![img1](https://i.imgur.com/aKaOqIh.gif) and ![img2](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("img1", "https://i.imgur.com/aKaOqIh.gif"), ("img2", "https://i.imgur.com/aKaOqIh.gif")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
    def test_multiple_images_same_url(self):
        text = "![img1](https://i.imgur.com/aKaOqIh.gif) and ![img2](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("img1", "https://i.imgur.com/aKaOqIh.gif"), ("img2", "https://i.imgur.com/aKaOqIh.gif")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected,actual)
    def test_no_links(self):
        text = "This is text with no links."
        expected = []
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)
    def test_link_without_anchor_text(self):
        text = "Here is a link [](https://www.boot.dev)"
        expected = [("", "https://www.boot.dev")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)
    def test_link_with_special_characters_in_anchor_text(self):
        text = "Check this out [boot & dev](https://www.boot.dev)"
        expected = [("boot & dev", "https://www.boot.dev")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)
    def test_multiple_links_same_url(self):
        text = "[link1](https://www.boot.dev) and [link2](https://www.boot.dev)"
        expected = [("link1", "https://www.boot.dev"), ("link2", "https://www.boot.dev")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)
    def test_link_url_with_query_parameters(self):
        text = "[query link](https://www.boot.dev?user=test)"
        expected = [("query link", "https://www.boot.dev?user=test")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)
    def test_extract_markdown_images_and_links(self):
        text = "Here is an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to boot dev](https://www.boot.dev)"
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        expected_links = [("to boot dev", "https://www.boot.dev")]
        actual_images = extract_markdown_images(text)
        actual_links = extract_markdown_links(text)
        self.assertEqual(expected_images, actual_images)
        self.assertEqual(expected_links, actual_links)

class TestSplitNodesImages(unittest.TestCase):
    def test_image(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="This is text with a link ", text_type=text_type_text),
            TextNode(text="to boot dev", text_type=text_type_image, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=text_type_text),
            TextNode(text="to youtube", text_type=text_type_image, url="https://www.youtube.com/@bootdotdev"),
        ]
        return self.assertEqual(expected, new_nodes)
    
    def test_no_images(self):
        node = TextNode(
            "This is text with no images.",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="This is text with no images.", text_type=text_type_text),
        ]
        self.assertEqual(expected, new_nodes)
    
    def test_single_image_at_beginning(self):
        node = TextNode(
            "![start image](https://example.com/start.png) This is text.",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="start image", text_type=text_type_image, url="https://example.com/start.png"),
            TextNode(text=" This is text.", text_type=text_type_text),
        ]
        self.assertEqual(expected, new_nodes)

    def test_single_image_at_end(self):
        node = TextNode(
            "This is text with an image at the end ![end image](https://example.com/end.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="This is text with an image at the end ", text_type=text_type_text),
            TextNode(text="end image", text_type=text_type_image, url="https://example.com/end.png"),
        ]
        self.assertEqual(expected, new_nodes)

    def test_multiple_images(self):
        node = TextNode(
            "Here is ![first image](https://example.com/first.png) and another ![second image](https://example.com/second.png).",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="Here is ", text_type=text_type_text),
            TextNode(text="first image", text_type=text_type_image, url="https://example.com/first.png"),
            TextNode(text=" and another ", text_type=text_type_text),
            TextNode(text="second image", text_type=text_type_image, url="https://example.com/second.png"),
            TextNode(text=".", text_type=text_type_text),
        ]
        self.assertEqual(expected, new_nodes)

    def test_adjacent_images(self):
        node = TextNode(
            "Two images in a row ![first](https://example.com/first.png)![second](https://example.com/second.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="Two images in a row ", text_type=text_type_text),
            TextNode(text="first", text_type=text_type_image, url="https://example.com/first.png"),
            TextNode(text="second", text_type=text_type_image, url="https://example.com/second.png"),
        ]
        self.assertEqual(expected, new_nodes)

    def test_image_without_alt_text(self):
        node = TextNode(
            "This is an image without alt text ![](https://example.com/noalt.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="This is an image without alt text ", text_type=text_type_text),
            TextNode(text="", text_type=text_type_image, url="https://example.com/noalt.png"),
        ]
        self.assertEqual(expected, new_nodes)

    def test_image_with_special_characters_in_alt_text(self):
        node = TextNode(
            "This is an image with special characters ![alt & text](https://example.com/special.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode(text="This is an image with special characters ", text_type=text_type_text),
            TextNode(text="alt & text", text_type=text_type_image, url="https://example.com/special.png"),
        ]
        self.assertEqual(expected, new_nodes)

class TestTextToTextNodes(unittest.TestCase):
    def test_many(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_no_formatting(self):
        text = "This is plain text with no formatting."
        expected = [
            TextNode("This is plain text with no formatting.", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_multiple_bold_sections(self):
        text = "This is **bold** and this is also **bold**."
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and this is also ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(".", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_multiple_italic_sections(self):
        text = "This is *italic* and this is also *italic*."
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and this is also ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(".", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_image_without_alt_text(self):
        text = "This is an image without alt text ![](https://i.imgur.com/noalt.png)."
        expected = [
            TextNode("This is an image without alt text ", text_type_text),
            TextNode("", text_type_image, "https://i.imgur.com/noalt.png"),
            TextNode(".", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_link_without_anchor_text(self):
        text = "Here is a link without anchor text [](https://www.boot.dev)."
        expected = [
            TextNode("Here is a link without anchor text ", text_type_text),
            TextNode("", text_type_link, "https://www.boot.dev"),
            TextNode(".", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_multiple_links(self):
        text = "Here are two links [link1](https://www.boot.dev) and [link2](https://www.example.com)."
        expected = [
            TextNode("Here are two links ", text_type_text),
            TextNode("link1", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("link2", text_type_link, "https://www.example.com"),
            TextNode(".", text_type_text),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)