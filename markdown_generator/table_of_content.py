from markdown_generator.interfaces import MarkdownElementInterface, ChapterInterface
from markdown_generator.markdown_formatter import MarkdownFormatter as MDF
from markdown_generator.markdown_formatter import Formater as Formater

# Todo:
#
# - [ ] add validation methode to check if chapter ids are unique

class TableOfContents(MarkdownElementInterface):

    def __init__(self, chapter: ChapterInterface) -> None:

        self.__chapter: ChapterInterface = chapter
        self.__indent_spaces=2
        self.__level_to_include=0

    def set_indent_spaces(self, indent_spaces: int):
        self.__indent_spaces = indent_spaces

    def set_level_to_include(self, level: int):
        self.__level_to_include = level

    def configure(self):
        self.__configure_sub_chapters(self.__chapter)

    def __configure_sub_chapters(self, chapter: ChapterInterface):

        if self.__is_level_condition(chapter):

            for sub_chapter in chapter.get_subchapters():

                sub_chapter.set_generate_chapter_achore_ids(True)
                self.__configure_sub_chapters(sub_chapter)

    def __str__(self):
        content = self.__generate_toc(self.__chapter)
        content += MDF.LINE_BREAK
        return content

    def __generate_toc(self,chapter: ChapterInterface) -> str:

        toc = ""

        if self.__is_level_condition(chapter):

            sub_chapter: ChapterInterface = None
            for sub_chapter in chapter.get_subchapters():

                headline: str = sub_chapter.get_headline()
                toc += "- " + MDF.chapter_link(headline) + MDF.LINE_BREAK

                toc_of_child_chapters: str = self.__generate_toc(sub_chapter)

                if toc_of_child_chapters != "":
                    toc_of_child_chapters = Formater.indent_text(text=toc_of_child_chapters, indent_spaces=self.__indent_spaces)
                    toc +=toc_of_child_chapters
        return toc

    def __is_level_condition(self, chapter: ChapterInterface) -> bool:
        if (self.__level_to_include==0) or (chapter.get_level() <= self.__level_to_include):
            return True
        else:
            return False
