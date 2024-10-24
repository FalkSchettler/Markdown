import pytest
from markdown.markdown_formatter import MarkdownFormatter


def test_indent_text():
    text = "line1\nline2"
    expected = "    line1\n    line2\n"
    assert MarkdownFormatter.indent_text(text, 4) == expected


def test_create_table():
    headers = ["Header1", "Header2"]
    rows = [["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]]
    expected = (
        "| Header1 | Header2 |\n"
        "| --- | --- |\n"
        "| Row1Col1 | Row1Col2 |\n"
        "| Row2Col1 | Row2Col2 |\n\n"
    )
    assert MarkdownFormatter.create_table(headers, rows) == expected


def test_reduce_line_breaks():
    text = "line1\n\n\nline2\n\nline3"
    expected = "line1\nline2\nline3"
    assert MarkdownFormatter.reduce_line_breaks(text) == expected


def test_create_heading():
    text = "This is a heading"
    expected = "# This is a heading\n"
    assert MarkdownFormatter.create_heading(1, text) == expected


def test_bold():
    text = "bold text"
    expected = "**bold text**"
    assert MarkdownFormatter.bold(text) == expected


def test_italic():
    text = "italic text"
    expected = "*italic text*"
    assert MarkdownFormatter.italic(text) == expected


def test_code():
    text = "code"
    expected = "`code`"
    assert MarkdownFormatter.code(text) == expected


def test_code_block():
    text = "code block"
    expected = "```\ncode block\n```"
    assert MarkdownFormatter.code_block("", text) == expected


def test_chapter_link():
    headline = "Chapter 1"
    expected = "[Chapter 1](#Chapter-1)"
    assert MarkdownFormatter.chapter_link(headline) == expected


def test_chapter_anchor_id():
    headline = "Chapter 1"
    expected = '<a id="Chapter-1"></a>'
    assert MarkdownFormatter.chapter_anchor_id(headline) == expected


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
