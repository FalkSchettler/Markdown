from markdown.interfaces import ChapterInterface
from markdown.markdown_formatter import MarkdownFormatter as MDF
from markdown.text_block import TextBlock
from markdown.table import Table
from markdown.lists import OrderedList, UnorderedList
from markdown.table_of_content import TableOfContents


class Chapter(ChapterInterface):

    def __init__(self, headline: str, level: int) -> None:
        self.__headline = headline
        self.__level = level
        self.__generate_chapter_anchor_id = False
        self.__sections = list()
        self.__toc: TableOfContents = None

    def get_headline(self):
        return self.__headline

    def get_level(self):
        return self.__level

    def get_subchapters(self):
        chapters: list = list()

        for sec in self.__sections:
            if isinstance(sec, Chapter):
                chapters.append(sec)
        return chapters

    def __str__(self):

        content: str = ""

        if TableOfContents.get_with_chapter_achor_id():
            content += MDF.chapter_anchor_id(self.__headline) + MDF.LINE_BREAK

        # add header to content
        content += MDF.create_heading(self.__level, self.__headline) + MDF.LINE_BREAK

        # add sections to content
        for i, section in enumerate(self.__sections):
            content += section.__str__()

        return content

    def add_text_block(self, text, position=None):
        text_block: TextBlock = TextBlock(text)
        if position is not None:
            self.__sections.insert(position, text_block)
        else:
            self.__sections.append(text_block)

        return text_block

    def add_table(self, headers, rows):
        table: Table = Table(headers, rows)
        self.__sections.append(table)
        return table

    def add_ordered_list(self, items=[]):
        enumeration: OrderedList = OrderedList(items)
        self.__sections.append(enumeration)
        return enumeration

    def add_unordered_list(self, items=[]):
        enumeration: UnorderedList = UnorderedList(items)
        self.__sections.append(enumeration)
        return enumeration

    def add_subchapter(self, subchapter):
        """
        Appends a subchapter to the current chapter.

        Args:
            subchapter (str): The title or name of the subchapter to be appended.

        Returns:
            Chapter: The newly created subchapter instance.
        """
        subchapter: Chapter = Chapter(subchapter, self.__level + 1)
        self.__sections.append(subchapter)
        return subchapter

    def add_toc(self, indent_spaces: int = 2):
        """
        Appends a Table of Contents (TOC) to the current document.
        Args:
            indent_spaces (int, optional): The number of spaces to use for indentation in the TOC. Defaults to 2.
        Returns:
            TableOfContents: The appended Table of Contents object.
        """
        if self.__toc is None:
            self.__toc: TableOfContents = TableOfContents(chapter=self)

        self.__toc.set_indent_spaces(indent_spaces)
        self.__sections.append(self.__toc)
        return self.__toc
