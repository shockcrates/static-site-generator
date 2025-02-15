from textnode import TextNode, TextType
import re


def text_to_textnodes(text):
    delimiter_list = [(TextType.BOLD,'**'),(TextType.ITALIC, '*'),(TextType.CODE,'`')]

    node_list = [TextNode(text,TextType.TEXT)]
    for delimiter in delimiter_list:
        
        node_list = split_nodes_delimiter(node_list, delimiter[1], delimiter[0])

    node_list = split_node_image(node_list)
    node_list = split_node_link(node_list)
    
    return node_list

#gong to write this without escape character recognition
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        
        if node.text_type == TextType.TEXT:
            
            splitted = node.text.split(delimiter)
            
            if len(splitted) % 2 == 1:
                if node.text[0] == delimiter:
                    node_to_list(splitted, new_nodes, text_type)
                    new_nodes = new_nodes[1:]
                    
                elif node.text[-1] == delimiter:
                    node_to_list(splitted, new_nodes, text_type)
                    new_nodes = new_nodes[:-1]
                else:
                    node_to_list(splitted, new_nodes, text_type)
            else:
                raise Exception(f"Invalid Markdown syntax: missing closing '{delimiter}'")

        else:
            new_nodes.append(node)
    return new_nodes

def node_to_list(splitted, new_nodes, text_type, urls=None):
    url_count = 0
    
    for i in range(len(splitted)):
        if text_type ==TextType.IMAGE or text_type==TextType.LINK:
            if is_even(i):
                #print(len(splitted[i]))
                if len(splitted[i]) != 0:
                    new_nodes.append(TextNode(splitted[i],TextType.TEXT))
            else:
                if len(splitted[i]) != 0:
                    new_nodes.append(TextNode(splitted[i],text_type, urls[url_count][1]))
                    url_count += 1
            
        else:
            if is_even(i):
                if len(splitted[i]) != 0:
                    new_nodes.append(TextNode(splitted[i],TextType.TEXT))
            else:
                if len(splitted[i]) != 0:
                    new_nodes.append(TextNode(splitted[i],text_type))
            
def is_even(number):
    return number % 2 == 0

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_link(text):
    return re.findall(r" \[(.*?)\]\((.*?)\)", text)

def split_node_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue

        text = node.text

        for match in matches:
            sections = text.split(f'![{match[0]}]({match[1]})',1)

            if len(sections) != 2:
                raise ValueError("Image Not formatted correctly")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(
                match[0],
                TextType.IMAGE,
                match[1]
            ))

            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))

        """ else:
            text = node.text
            splitted = [text]
            
            #print("Looking for image: " + match[0] + "   LINK: " + match[1])
            #print("Text to be split: " + text)
            splitted = split_on_image(text, matches.copy())
            #text = splitted[-1]
            #splitted.insert(-1,f'![{match[0]}]({match[1]})')
            #print("splitted: " + repr(splitted))

                
            #print(splitted)
            node_to_list(splitted, new_nodes, TextType.IMAGE, matches) """
    return new_nodes

def split_node_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_link(node.text)
        if not matches:
            new_nodes.append(node)
            continue

        text = node.text
        for match in matches:
            sections = text.split(f'[{match[0]}]({match[1]})',1)

            if len(sections) != 2:
                raise ValueError("Link Not formatted correctly")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(
                match[0],
                TextType.LINK,
                match[1]))
            
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text,TextType.TEXT))

        """ else:
            text = node.text
            splitted = [text]
            
            
            #print("Text to be split: " + text)
            #print("mathces_list: " +repr(matches))
            splitted = split_on_link(text, matches.copy())
            
            #print("splitted: " + repr(splitted))

                
            #print(splitted)
            node_to_list(splitted, new_nodes, TextType.LINK, matches) """
    return new_nodes


def split_on_image(text, matches_list):
    #print("Text in recursive call start: " + text)
    if not matches_list:
        return [text]
    else:
        current_match = matches_list.pop(0)
        #print("current match = " + repr(current_match))
        splitted = text.split(f'![{current_match[0]}]({current_match[1]})')
        splitted.insert(-1,f'{current_match[0]}')
        text = splitted[-1]
        results = split_on_image(text, matches_list)
        #print("results of call (to be appended): " + repr(results))
        if results:
            splitted = splitted[:-1] + results
            #splitted[:-1].append(results)
        #print("splitted being passsed to higher level: " + repr(splitted))
        return splitted
    
def split_on_link(text, matches_list):
    #print("Text in recursive call start: " + text)
    #print("Length of matches_list: " + str(len(matches_list)))
    if len(matches_list) == 0:
        #print("Got here when len was zero")
        return [text]
    else:
        current_match = matches_list.pop(0)
        #print("current match = " + repr(current_match))
        splitted = text.split(f'[{current_match[0]}]({current_match[1]})')
        splitted.insert(-1,f'{current_match[0]}')
        text = splitted[-1]
        results = split_on_link(text, matches_list)
        #print("results of call (to be appended): " + repr(results))
        #print("Splitted check: " + repr(splitted))
        
        
        if results:
            splitted = splitted[:-1] + results
        
        #print("splitted being passsed to higher level: " + repr(splitted))
        return splitted
    