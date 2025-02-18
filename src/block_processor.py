import re

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")

    #lines = list(filter(lambda x: x != "",lines))
    lines = list(map(lambda x: x.strip(),lines))

    blocks = []
    block_start = 0
    for i in range(len(lines)):
        if lines[i] == "":              #Split blocks on blank lines
            block_length = i - block_start
            if block_length > 0:
                block = ""
                for j in range(block_start, i):
                    block += lines[j] + '\n'
                blocks.append(block)
            block_start = i + 1
        else:                           #Save last block
            if i == len(lines) - 1:
                block = ""
                for j in range(block_start, i+1):
                    block += lines[j] + '\n'
                blocks.append(block)
    
    return blocks

def block_to_blocktype(block):
    if check_heading(block):
        return "Heading"
    elif check_code(block):
        return "code"
    elif check_quote(block):
        return "Quote"
    elif check_unordered_list(block):
        return "Unordered List"
    elif check_ordered_list(block):
        return "Ordered List"
    else:
        return "Paragraph"

def check_heading(text):
    pattern = r'(?<!#)#{1,6}(?!#) '
    match = re.search( pattern, text)
    #print("match: " + repr(match))
    return bool(match)

def check_code(text):
    if text[0:3] == "```" and  text[-3:] == "```":
        return True
    return False

def check_quote(text):
    lines = text.split("\n")
    print(repr(lines))
    is_list = True
    for line in lines:
        if line[0:2] != "> ":
            is_list =  False
    return is_list

def check_unordered_list(text):
    lines = text.split("\n")
    is_list = True
    
    for line in lines:
        if line[0:2] != "* " and line[0:2] != "- ":
            is_list = False
    return is_list



def check_ordered_list(text):
    lines = text.split("\n")
    
    is_list = True
    for i in range(len(lines)):
        if lines[i][0:3] != f'{i + 1}. ':
            is_list = False
    return is_list