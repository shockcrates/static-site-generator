

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
        return f'HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props_to_html}'
    

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
