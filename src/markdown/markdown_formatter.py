from markdown.formatter import Formatter

# Todo: check remove_empty_lines_and_breaks


class MarkdownFormatter:

    LINE_BREAK = "\n"

    @staticmethod
    def indent_text(text: str, indent_spaces: int) -> str:
        indent_str = " " * indent_spaces
        text = text.replace(MarkdownFormatter.LINE_BREAK, MarkdownFormatter.LINE_BREAK + indent_str)
        text = indent_str + text
        text = text.rstrip() + MarkdownFormatter.LINE_BREAK
        return text

    @staticmethod
    def create_table(headers, rows):

        # delete empty lines from rows
        header_row = "| " + " | ".join(headers) + " |"
        separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
        data_rows = ["| " + " | ".join(Formatter.remove_empty_lines_and_breaks(row)) + " |" for row in rows]

        table = MarkdownFormatter.LINE_BREAK.join([header_row, separator_row] + data_rows)
        table += MarkdownFormatter.LINE_BREAK * 2
        return table

    @staticmethod
    def reduce_line_breaks(text: str) -> str:
        """
        Remove multiple consecutive empty lines from the given text.
        Args:
            text (str): The input text from which to remove multiple empty lines.
        Returns:
            str: The text with multiple consecutive empty lines removed.
        """

        return MarkdownFormatter.LINE_BREAK.join([line for line in text.splitlines() if line.strip()])

    @staticmethod
    def create_heading(level, text):
        # remove line breaks from text
        text = ' '.join([line for line in text.splitlines() if line.strip()])
        return "#" * level + " " + text + MarkdownFormatter.LINE_BREAK

    @staticmethod
    def bold(text):
        return "**" + text + "**"

    @staticmethod
    def italic(text):
        return "*" + text + "*"

    @staticmethod
    def code(text):
        return "`" + text + "`"

    @staticmethod
    def code_block(language, text):
        if language == "":
            return "```" + MarkdownFormatter.LINE_BREAK + text + MarkdownFormatter.LINE_BREAK + "```"
        else:
            return "```" + language + MarkdownFormatter.LINE_BREAK + text + MarkdownFormatter.LINE_BREAK + "```"

    @staticmethod
    def chapter_link(headline: str):
        valid_id = Formatter.string_to_anchor_id(headline)
        return "[" + headline + "](#" + valid_id + ")"

    @staticmethod
    def chapter_anchor_id(headline: str):
        valid_id = Formatter.string_to_anchor_id(headline)
        return f'<a id="{valid_id}"></a>'
