# import exceptions for non implemented methods
from abc import ABC, abstractmethod


class MarkdownElementInterface(ABC):  # pragma: no cover

    @abstractmethod
    def __str__(self) -> str:
        pass


class ChapterInterface(MarkdownElementInterface):  # pragma: no cover

    @abstractmethod
    def get_level(self):
        pass

    @abstractmethod
    def get_subchapters(self) -> list:
        pass

    @abstractmethod
    def get_headline(self) -> str:
        pass
