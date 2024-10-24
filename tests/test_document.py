import pytest
import filecmp
from markdown import MarkdownDocument, TableOfContents, Table, Chapter


class TestDocument:

    def test_document(self):

        reference_file: str = './doc/arc42/example.md'
        generated_file: str = './tests/example.md'

        # read example.md
        with open(reference_file, 'r') as file:
            content = file.read()
        assert content is not None

        doc: MarkdownDocument = MarkdownDocument("Example")
        TableOfContents.set_with_chapter_anchor_id(False)

        # Text Blocks
        doc.add_subchapter("Text Blocks")

        doc.add_text_block("This is the first Text Block!")
        doc.add_text_block("This is the third Text Block!")
        doc.add_text_block(text="This is the second Text Block", position=2)

        # Tables
        chapter_tables: Chapter = doc.add_subchapter("Tables")

        table: Table = chapter_tables.add_table(["Header 1", "Header 2"],
                                                [["Row 1 Col 1", "Row 1 Col 2"],
                                                 ["Row 2 Col 1", "Row 2 Col 2"]])
        table.append_row(["Row 3 Col 1", "Row 3 Col 2"])
        table.append_row(["Row 4 Col 1", "Row 4 Col 2"])

        # Lists
        chapter_lists: Chapter = doc.add_subchapter("Lists")

        chapter_lists.add_ordered_list(["Ordered Item 1", "Ordered Item 2", "Ordered Item 3"])

        chapter_lists.add_unordered_list(["Unordered Item 1", "Unordered Item 2", "Unordered Item 3"])

        doc.write(generated_file)

        assert filecmp.cmp(reference_file, generated_file, shallow=False), "The files are not identical"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
