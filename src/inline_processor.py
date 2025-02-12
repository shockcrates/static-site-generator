from textnode import TextNode, TextType


#gong to write this without escape character recognition
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            splitted = node.text.split(delimiter)
            if len(splitted) % 2 == 1:
                if node.text[0] == delimiter:
                    node_to_list(splitted, new_nodes, text_type)
                    splitted = splitted[1:]
                elif node.text[-1] == delimiter:
                    node_to_list(splitted, new_nodes, text_type)
                    splitted = splitted[:-1]
                else:
                    node_to_list(splitted, new_nodes, text_type)
            else:
                raise Exception(f"Invalid Markdown syntax: missing closing '{delimiter}'")

        else:
            return new_nodes.extend(node)
    return new_nodes

def node_to_list(splitted, new_nodes, text_type):
    for i in range(len(splitted)):
        if is_even(i):
            new_nodes.append(TextNode(splitted[i],TextType.TEXT))
        else:
            new_nodes.append(TextNode(splitted[i],text_type))
            


def is_even(number):
    return number % 2 == 0