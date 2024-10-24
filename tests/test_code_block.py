import pytest
from utils import link_to_requirement
from markdown import CodeBlock


class TestCodeBlock:

    @link_to_requirement("Req.1")
    def test_content_without_language(self):
        code = CodeBlock("Code without Language")
        assert str(code) == "```\nCode without Language\n```\n"

    @link_to_requirement("Req.1")
    def test_content_with_language(self):
        code = CodeBlock("Code without Language", "python")
        assert str(code) == "```python\nCode without Language\n```\n"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
