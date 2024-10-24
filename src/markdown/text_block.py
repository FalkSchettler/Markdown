from markdown.interfaces import MarkdownElementInterface
from markdown.markdown_formatter import MarkdownFormatter


class TextBlock(MarkdownElementInterface):

    def __init__(self, text: str = "") -> None:

        self.content: str = ""

        # add one line break at
        self.content += text

    def add_empty_line(self):
        self.content += MarkdownFormatter.LINE_BREAK

    def add_text(self, text: str):
        self.content += text

    def __str__(self):

        # remove line at end of text
        beautified_content = self.content.rstrip()

        # add two line breaks at the end of the text
        beautified_content += MarkdownFormatter.LINE_BREAK * 2

        return beautified_content
