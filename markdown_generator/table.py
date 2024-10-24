from markdown_generator.interfaces import MarkdownElementInterface
from markdown_generator.markdown_formatter import MarkdownFormatter

class Table(MarkdownElementInterface):

    def __init__(self, headers, rows) -> None:
        self.headers = headers
        self.rows = rows

    def add_row(self, row):
        self.rows.append(row)

    def __str__(self):
        content: str = MarkdownFormatter.create_table(self.headers, self.rows)
        content += MarkdownFormatter.LINE_BREAK * 2
        return content

