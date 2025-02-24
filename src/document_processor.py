from block_processor import *
from inline_processor import *
from htmlnode import *
from textnode import *

def markdown_to_htmlnode(markdown):
    blocks_markdown = markdown_to_blocks(markdown)

    div = ParentNode("div",[],None)

    print(blocks_markdown)
    for block in blocks_markdown:
        block_type = block_to_blocktype(block)
        print(block_type)
        new_node = block_type_to_HTMLNode(block, block_type)

        div.children.append(new_node)
    
    return div


        

def block_type_to_HTMLNode(block, block_type):
    if block_type == "Paragraph":
        ParaNode =  ParentNode("p",None,None)
        
        children = text_to_children(block)

        ParaNode.children = children

        return ParaNode

    if block_type == "Heading":
        sections = block.split(" ",1)

        count = len(sections[0])
        #print("Count = " + str(count))
        Heading_node = ParentNode(f'h{count}',None,None)
        
        children = text_to_children(sections[1])

        Heading_node.children = children
        return Heading_node
    
    if block_type == "Quote":
        QuoteNode = ParentNode("blockquote", [], None)

        lines = block.split("\n")
        new_lines = []

        for line in lines:
            new_lines.append(line.split(" ", 1)[1])

        section = "\n".join(new_lines)

        children = text_to_children(section)

        QuoteNode.children.extend(children)

        return QuoteNode
    
    if block_type == "Unordered List":
        UL_node = ParentNode("ul", [], None)

        lines = block.split("\n")
        list_items = lines_to_list_items(lines)


        UL_node.children.extend(list_items)

        return UL_node
    
    if block_type == "Ordered List":
        OL_node = ParentNode("ol", [], None)

        lines = block.split("\n")
        list_items = lines_to_list_items(lines)



        OL_node.children.extend(list_items)

        return OL_node
    
    if block_type == "Code":
        code_node = ParentNode('code',[],None)
        
        code_without_ticks = block[3:-3]
        pre_node = ParentNode('pre',[ParentNode('code', text_to_children(code_without_ticks),None)])

        code_node.children.append(pre_node)

        return code_node


def lines_to_list_items(lines):
    list_items = []
    for line in lines:
        if line != "":
            nodes = text_to_children(line.split(" ", 1)[1])
            list_item = ParentNode("li", nodes, None)
            list_items.append(list_item)
    return list_items


def text_to_children(text):
    children = []
    sections = text_to_textnodes(text)

    for sect in sections:
        new_node = text_node_to_html_node(sect)
        children.append(new_node)
    return children