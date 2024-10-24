from markdown_generator.interfaces import MarkdownElementInterface
from markdown_generator.markdown_formatter import MarkdownFormatter

class TextBlock(MarkdownElementInterface):

    def __init__(self, text: str) -> None:

        self.content = ""
        # if text is empty, do nothing
        if not text:
            return

        # add one line break at
        self.content += text

    def add_empty_line(self):
        self.content += MarkdownFormatter.LINE_BREAK

    def add_text(self, text):
        self.content += text

    def __str__(self):

        # remove line at end of text
        self.content = self.content.rstrip()

        # add two line breaks at the end of the text
        return self.content + MarkdownFormatter.LINE_BREAK * 2
