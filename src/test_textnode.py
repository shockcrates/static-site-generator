import unittest
from htmlnode import text_node_to_html_node

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_none_default(self):
        node = TextNode("This is a test node", TextType.BOLD, None)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_content(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test a different node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_text_type(self):
        node = TextNode("This is a test node", TextType.TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_URLs(self):
        node = TextNode("This is a test node", TextType.TEXT, "yourmomshouse.com")
        node2 = TextNode("This is a test node", TextType.TEXT, "mydadshouse.net")
        self.assertNotEqual(node, node2)

    def test_same_URLs(self):
        node = TextNode("This is a test node", TextType.TEXT, "yourmomshouse.com")
        node2 = TextNode("This is a test node", TextType.TEXT, "yourmomshouse.com")
        self.assertEqual(node, node2)

    def test_TextNode_to_HTMLNode(self):
        node = TextNode("This is a test node", TextType.BOLD, None)
        HTML_node = text_node_to_html_node(node)
        check = HTML_node.to_html() == "<b>This is a test node</b>"

        node2 = TextNode("This is a test node", TextType.LINK, "mydadshouse.net")
        HTML_node2 = text_node_to_html_node(node2)
        check2 = HTML_node2.to_html() == '<a href="mydadshouse.net">This is a test node</a>'

        node3=TextNode("picture of cat in a tunnel", TextType.IMAGE, "https://tunnelcatsXXX.com")
        HTML_node3 = text_node_to_html_node(node3)
        check3 = HTML_node3.to_html() == '<img src="https://tunnelcatsXXX.com" alt="picture of cat in a tunnel"></img>'

        self.assertEqual(True, check and check2 and check3)
