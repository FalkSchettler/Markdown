from markdown.interfaces import MarkdownElementInterface
from markdown.markdown_formatter import MarkdownFormatter


class Table(MarkdownElementInterface):

    def __init__(self, headers, rows) -> None:
        """
        Initializes the table with headers and rows.
        Args:
            headers (list): A list of column headers for the table.
            rows (list of lists): A list of rows, where each row is a list of column values.
        """
        self.headers = headers
        self.rows = rows

    def append_row(self, row):
        self.rows.append(row)

    def __str__(self):

        if not self.headers or not self.rows:
            return ""

        content: str = MarkdownFormatter.create_table(self.headers, self.rows)
        return content
