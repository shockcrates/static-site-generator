

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