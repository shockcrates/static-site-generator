from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, html_node):
        if self.tag == html_node.tag and self.value == html_node.value and self.children == html_node.children and self.props == html_node.props:
            return True
        else:
            return False
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            temp = ''
            for prop in self.props:
                temp = temp + f'{prop}="{self.props[prop]}" '
            return temp[:-1]
        else:
            return ""
    
    def __repr__(self):
        return f'[HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}]'
    

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode has no value")
        if self.tag == None:
            return f'{self.value}'
        else:
            if self.props:
                return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'[LeafNode: {self.tag}, {self.value}, {self.props}]'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode has no children :^(")
        else:
            html_string = f'<{self.tag}'

            if self.props:
                html_string += " " + self.props_to_html()+ ">"
            else:
                html_string += ">"


            for child in self.children:

                html_string += child.to_html()

            html_string += f'</{self.tag}>'

            return html_string
        
def text_node_to_html_node(text_node):
	if text_node.text_type == TextType.BOLD:
		return LeafNode('b',text_node.text)
	elif text_node.text_type == TextType.TEXT:
		return LeafNode('',text_node.text)
	elif text_node.text_type == TextType.ITALIC:
		return LeafNode('i',text_node.text)
	elif text_node.text_type == TextType.CODE:
		return LeafNode('code',text_node.text)
	elif text_node.text_type == TextType.LINK:
		return LeafNode('a',text_node.text, {"href": text_node.url})
	elif text_node.text_type == TextType.IMAGE:
		return LeafNode('img','', {"src": text_node.url, "alt": text_node.text})
	else:
		raise Exception("TextNode cannot convert to HTMLNode becuase of invalid TextType")
