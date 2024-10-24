import pytest
from markdown import TextBlock


class TestTextBlock:

    def test_add_text_block(self):
        text_block = TextBlock("Test Text Block")
        assert str(text_block) == "Test Text Block\n\n"

    def test_add_empty_line(self):

        text_block = TextBlock("Test Text Block")
        text_block.add_empty_line()
        assert str(text_block) == "Test Text Block\n\n"

        text_block.add_empty_line()
        text_block.add_text("Test Text Block")

        assert str(text_block) == "Test Text Block\n\nTest Text Block\n\n"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
