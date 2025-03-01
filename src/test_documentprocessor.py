import unittest
from document_processor import *

class TestDocumentProcessor(unittest.TestCase):
    def test_block_type_to_htmlnode(self):
        block1 = "### New Peptide *asonishes* Dermatologists with Wrinkle-Vanishing ability"
        blocktype1 = block_to_blocktype(block1)

        result1 = block_type_to_HTMLNode(block1, blocktype1)
        #print("Document blocktype: " + blocktype1)
        #print(result1)

        block2 = "> Very deep thought.\n> Another less **deep** but more based thought"
        blocktype2 = block_to_blocktype(block2)

        result2 = block_type_to_HTMLNode(block2, blocktype2)
        #print("Document blocktype: " + blocktype2)
        #print(block2)
        #print(result2)

        block3 = "1. Line1\n2. Line2\n3. Line**333**"
        blocktype3 = block_to_blocktype(block3)
        result3 = block_type_to_HTMLNode(block3, blocktype3)
        #print(blocktype3)

        block4 = "```\nCODE LOTS AND LOTS OF CODE\n```"
        blocktype4 = block_to_blocktype(block4)
        result4 = block_type_to_HTMLNode(block4, blocktype4)
        #print(result4)

    def test_markdown_to_htmlnode_simple(self):
        text = """
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

```
func main(){
    fmt.Println("Aiya, Ambar!")
}
```
"""
        result = markdown_to_htmlnode(text)
        print()
        print(result)
        print()
        print(result.to_html())