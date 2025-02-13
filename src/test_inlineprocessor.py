import unittest

from inline_processor import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInlineProcessor(unittest.TestCase):
    def test_split_nodes_delimiter_1_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_1_bold(self):
        node = TextNode("This is text with a *code block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_2_bold_front(self):
        node = TextNode("*This* is text with a *code block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This", TextType.BOLD),
            TextNode(" is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_split_nodes_delimiter_2_bold_back(self):
        node = TextNode("This is text with a *code* block *word*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.BOLD),
            TextNode(" block ", TextType.TEXT),
            TextNode("word", TextType.BOLD),
        ])
    
    def test_split_nodes_delimite_missing_closing_character(self):
        threw = False
        try:
            node = TextNode("This is text with a *code block word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        except:
            threw = True
            self.assertTrue(threw)