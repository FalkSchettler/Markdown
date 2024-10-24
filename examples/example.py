from markdown_generator import MarkdownDocument, Chapter, TextBlock, Table, TableOfContents


if __name__ == "__main__":

    doc: MarkdownDocument = MarkdownDocument("Test Document")

    # add table of content
    toc: TableOfContents = doc.append_toc()
    toc.set_indent_spaces(2)
    toc.set_level_to_include(2)

    # create document structure

    chapter1: Chapter = doc.append_subchapter("Chapter 1")
    chapter2: Chapter = doc.append_subchapter("Chapter 2")

    chapter21: Chapter = chapter2.append_subchapter("Chapter 2.1")
    chapter21.append_toc()

    chapter211: Chapter = chapter21.append_subchapter("Chapter 2.1.1")
    chapter212: Chapter = chapter21.append_subchapter("Chapter 2.1.2")

    chapter22: Chapter = chapter2.append_subchapter("Chapter 2.2")

    chapter3: Chapter = doc.append_subchapter("Chapter 3")

    doc.append_toc()

    # add content to root chapter
    text_block: TextBlock = doc.insert_text_block("This is a first text block for this document, below the root chapter! (before toc)\n", 0 )
    text_block.add_text("add to text block first. \n\n\n\n")

    # add content to chapter 1
    chapter1.append_text_block("This is a first text block for this document!")
    chapter1.append_text_block("This is a second text block with many line breaks at the end of the text. \n\n\n\n")
    chapter1.append_text_block("This is a third text block\n" + "\nwith many line breaks at the end of the text. \n\n\n\n")


    text_block = chapter1.append_text_block("This is a fourth text block with many line breaks at the end of the text. \n\n\n\n")
    text_block.add_text("add to text block fourth. \n\n\n\n")
    text_block.add_empty_line()
    text_block.add_text("add to text block fourth. (last line breaks should be removed)\n\n\n\n")

    table: Table = chapter1.append_table(["Header 1", "Header 2"],
                                 [["Row 1 Col 1", "Row 1 Col 2"],
                                  ["Row 2 Col 1", "Row 2 Col 2"]])
    table.add_row(["Row 3 Col 1", "Row 3 Col 2"])
    table.add_row(["Row 4 Col 1", "Row 4 Col 2"])

    chapter1.append_table(["Header 1", "Header 2"],
                        [["Row 1 Col 1", "Row 1 Col 2"],
                         ["Row 2 Col 1", "Row 2 Col 2"]])

    # add content to chapter 2
    text_block: TextBlock = chapter2.append_text_block("This is a first text block for chapter 2!")


    # print to console
    print(doc)

    # write to file
    with open("example.md", "w") as file:
        file.write(str(doc))


