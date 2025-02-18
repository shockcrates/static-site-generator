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
        #print(result)


    def test_check_heading(self):
        text = "#### This is a heading"
        result = check_heading(text)
        #print(result)
        self.assertEqual(result,True)

    def test_check_code(self):
        text = "```This is code i swear```"
        result = check_code(text)
        #print(result)
        self.assertEqual(result,True)

    def test_check_quotes(self):
        text = "> Very deep thought.\n> Another less deep but more based thought"
        result = check_quote(text)
        self.assertEqual(result, True)

    def test_block_to_blocktype(self):
        text = "#### This is a subheading"
        result = block_to_blocktype(text)
        text2 = """* Bullet 1\n* Bullet 2"""
        result2 = block_to_blocktype(text2)
        text3 = "1. Bullet 1\n2. Bullet 2"
        result3 = block_to_blocktype(text3)
        print(result)
        print(result2)
        print(result3)