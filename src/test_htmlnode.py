import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("p", 'this is value', ['object1', 'object2'])
        node2 = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
        props_truth = 'href="https://www.google.com" target="_blank"'
        props_test = node.props_to_html()
        self.assertEqual(props_test, props_truth)

    def test_LeafNode(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        truth = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(truth, node.to_html())

    def test_ParentNode_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text",None),
                LeafNode(None, "Normal text", None),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text", None),
            ],
        )
        self.assertEqual(node,node2)
    
    def test_ParentNode_not_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text",None),
                LeafNode(None, "Normal text", None),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("a", "Link text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Somethings different", None),
            ],
        )
        self.assertNotEqual(node,node2)

    def test_ParentNode_to_html_simple(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        truth = '<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(),truth)

    def test_ParentNode_to_html_2_layers(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        truth = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(),truth)

    def test_ParentNode_to_html_2_layers_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text", ),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "https://www.google.com", "target": "_blank"},
        )
        truth = '<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(),truth)