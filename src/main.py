from textnode import *
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
	dummy = TextNode("We out here", TextType.BOLD, "sunny.com")
	node = HTMLNode("p", 'this is value', ['object1', 'object2'], {"href": "https://www.google.com", "target": "_blank"})
	print(repr(node)) 

main()