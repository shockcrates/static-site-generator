import unittest

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
        node = TextNode("This is a test node", TextType.NORMAL)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_URLs(self):
        node = TextNode("This is a test node", TextType.NORMAL, "yourmomshouse.com")
        node2 = TextNode("This is a test node", TextType.NORMAL, "mydadshouse.net")
        self.assertNotEqual(node, node2)

    def test_same_URLs(self):
        node = TextNode("This is a test node", TextType.NORMAL, "yourmomshouse.com")
        node2 = TextNode("This is a test node", TextType.NORMAL, "yourmomshouse.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()