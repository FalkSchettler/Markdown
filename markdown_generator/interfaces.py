# import exceptions for non implemented methods
from abc import ABC, abstractmethod

class MarkdownElementInterface(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

class ChapterInterface(MarkdownElementInterface):

    @abstractmethod
    def set_generate_chapter_achore_ids(self, activate: bool):
        pass

    @abstractmethod
    def get_level(self):
        pass

    @abstractmethod
    def get_subchapters(self) -> list:
        pass

    @abstractmethod
    def get_headline(self) -> str:
        pass

    # @abstractmethod
    # def get_table_of_content(self, indent_spaces, level_to_include) -> str:
    #     pass
