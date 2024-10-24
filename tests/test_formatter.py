import pytest
from markdown.formatter import Formatter


class TestFormatter:
    def test_remove_empty_lines_and_breaks(self):
        row = ["This is a line.\n\nThis is another line.", "\n\nThis is a third line.\n"]
        expected = ["This is a line. This is another line.", "This is a third line."]
        assert Formatter.remove_empty_lines_and_breaks(row) == expected

    def test_string_to_anchor_id(self):
        name = "This is a Test Name!"
        expected = "This-is-a-Test-Name"
        assert Formatter.string_to_anchor_id(name) == expected

        name = "Another_Test-Name"
        expected = "Another_Test-Name"
        assert Formatter.string_to_anchor_id(name) == expected

    def test_remove_line_breaks(self):
        text = "This is a text with a line break.\nThis is the second line.\n\n\nThis is the fourth line."
        expected = "This is a text with a line break. This is the second line. This is the fourth line."
        assert Formatter.remove_line_breaks(text) == expected

        text = "\n\nThis is a single line.\n\n"
        expected = "This is a single line."
        assert Formatter.remove_line_breaks(text) == expected


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
