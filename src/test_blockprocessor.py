from block_processor import *
import unittest

class TestBlockProcessor(unittest.TestCase):
    def test_markdown_to_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        truth = ['# This is a heading','This is a paragraph of text. It has some **bold** and *italic* words inside of it.',"""* This is the first list item in a list block
* This is a list item
* This is another list item"""]
        print(result)