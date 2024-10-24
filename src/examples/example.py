from markdown import MarkdownDocument, Chapter, TextBlock, Table, TableOfContents


if __name__ == "__main__":

    doc: MarkdownDocument = MarkdownDocument("Test Document")

    # add table of content
    toc: TableOfContents = doc.add_toc()
    toc.set_indent_spaces(2)
    toc.set_level_to_include(2)
    toc.configure()

    # create document structure

    chapter1: Chapter = doc.add_subchapter("Chapter 1 - Text")
    chapter2: Chapter = doc.add_subchapter("Chapter 2 - Text and Tables")
    chapter3: Chapter = doc.add_subchapter("Chapter 3 - Lists")

    chapter4: Chapter = doc.add_subchapter("Chapter 4 - Subchapters")
    chapter41: Chapter = chapter4.add_subchapter("Chapter 4.1")
    chapter41.add_toc()

    chapter411: Chapter = chapter41.add_subchapter("Chapter 4.1.1")
    chapter412: Chapter = chapter41.add_subchapter("Chapter 4.1.2")

    chapter42: Chapter = chapter4.add_subchapter("Chapter 4.2")

    doc.add_toc()

    # add content to root chapter
    text_block: TextBlock = doc.insert_text_block("This is a first text block for this document, below the root chapter! (before toc)\n", 0)
    text_block.add_text("add to text block first. \n\n\n\n")

    # add content to chapter 1
    chapter1.add_text_block("This is a first text block for this document!")
    chapter1.add_text_block("This is a second text block with many line breaks at the end of the text. \n\n\n\n")
    chapter1.add_text_block("This is a third text block\n" + "\nwith many line breaks at the end of the text. \n\n\n\n")

    text_block = chapter1.add_text_block("This is a fourth text block with many line breaks at the end of the text. \n\n\n\n")
    text_block.add_text("add to text block fourth. \n\n\n\n")
    text_block.add_empty_line()
    text_block.add_text("add to text block fourth. (last line breaks should be removed)\n\n\n\n")

    # add content to chapter 2
    text_block: TextBlock = chapter2.add_text_block("Text before table")

    table: Table = chapter2.add_table(["Header 1", "Header 2"],
                                      [["Row 1 Col 1", "Row 1 Col 2"],
                                       ["Row 2 Col 1", "Row 2 Col 2"]])

    table.append_row(["Row 3 Col 1", "Row 3 Col 2"])
    table.append_row(["Row 4 Col 1", "Row 4 Col 2"])

    chapter1.add_table(["Header 1", "Header 2"],
                       [["Row 1 Col 1", "Row 1 Col 2"],
                        ["Row 2 Col 1", "Row 2 Col 2"]])

    text_block = chapter2.add_text_block("Text after table")

    # add content to chapter 3
    text_block_3: TextBlock = chapter3.add_text_block("This is a first text block for chapter 3!")

    oe1 = chapter3.add_ordered_list(["item1", "item2", "item3"])
    oe1.add_item(["sub1", "sub2", "sub3"])

    chapter3.add_unordered_list(["item1", "item2", "item3"])

    # print to console
    content: str = str(doc)
    print(content)

    # write to file
    with open("example.md", "w") as file:
        file.write(str(doc))
