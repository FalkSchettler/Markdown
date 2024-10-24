# Description: Test markdown module
# using Pytest

import pytest
from markdown_generator.text_block import *

class TestTextBlock:

    def test_add_text_block(self):
        text_block = TextBlock("Test Text Block")
        assert text_block == "Test Text Block"

    def test_markdown_document():
        pass





